import copy
import csv
import functools
import getpass
import os
from json import JSONDecodeError
from multiprocessing.pool import ThreadPool
from random import shuffle
from typing import Dict, List, Optional
from urllib.parse import urlencode
import uuid

from requests import Response
from tqdm import tqdm
from warnings import warn

from vortexasdk.search_response import SearchResponse
from vortexasdk.api.id import ID
from vortexasdk.endpoints.endpoints import API_URL
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import (
    _HEADERS as default_headers,
    retry_get,
    retry_post,
)
from vortexasdk.utils import filter_empty_values
from vortexasdk.version_utils import is_sdk_version_outdated
from vortexasdk.version import __version__
from vortexasdk import __name__ as sdk_pkg_name

logger = get_logger(__name__)


class VortexaClient:
    """The API client responsible for calling Vortexa's Public API."""

    _DEFAULT_PAGE_LOAD_SIZE = int(1e4)
    _N_THREADS = 6
    _MAX_ALLOWED_TOTAL = int(1e6)

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource: str, id: ID) -> List[Dict]:
        """Lookup reference data."""
        url = self._create_url(f"{resource}/{id}")
        response = retry_get(url)
        return _handle_response(response)["data"]

    def get_record(self, resource: str, id: ID) -> Dict:
        """Lookup single record data."""
        url = self._create_url(f"{resource}/{id}")
        response = retry_get(url)
        return _handle_response(response)["data"]

    def get_record_with_params(
        self, resource: str, id: ID, params: Dict
    ) -> Dict:
        """Lookup single record data."""
        url = self._create_url_with_params(f"{resource}/{id}", params)
        response = retry_get(url)
        return _handle_response(response)["data"]

    def search(
        self, resource: str, response_type: Optional[str], **data
    ) -> SearchResponse:
        """Search using `resource` using `**data` as filter params."""
        url = self._create_url(resource)
        payload = self._cleanse_payload(data)
        # use default headers if none are provided
        headers = (
            payload["headers"] if "headers" in payload else default_headers
        )
        logger.info(f"Payload: {payload}")
        # breakdowns do not support paging, the breakdown size is specified explicitly as a request parameter
        if response_type == "breakdown":
            size = payload.get("breakdown_size", 1000)
            response = _send_post_request(
                url, payload, size=size, offset=0, headers=headers
            )

            ref = response.get("reference", {})
            return {"reference": ref, "data": response["data"]}

        probe_response = _send_post_request(
            url, payload, size=1, offset=0, headers=headers
        )
        total = self._calculate_total(probe_response)

        if total > self._MAX_ALLOWED_TOTAL:
            raise Exception(
                f"Attempting to query too many records at once. Attempted records: {total}, Max allowed records: {self._MAX_ALLOWED_TOTAL} . "
                f"Try reducing the date range to return fewer records."
            )
        elif total == 1:
            # Only one page response, no need to send another request, so return flattened response
            return {"reference": {}, "data": probe_response["data"]}
        else:
            # Multiple pages available, create offsets and fetch all responses
            responses = self._process_multiple_pages(
                total=total,
                url=url,
                payload=payload,
                data=data,
                headers=headers,
            )

            flattened = self._flatten_response(responses)

            if len(flattened) != total:
                warn(
                    f"Incorrect number of records returned from API. This could be because data upstream updated during your request."
                )
                warn(f"Actual: {len(flattened)}, expected: {total}")

            return {"reference": {}, "data": flattened}

    def _create_url(self, path: str) -> str:
        return (
            f"{API_URL}{path}?_sdk=python_v{__version__}&apikey={self.api_key}"
        )

    def _create_url_with_params(self, path: str, params: Dict) -> str:
        stringParams = urlencode(params)
        if len(stringParams) > 0:
            return f"{API_URL}{path}?_sdk=python_v{__version__}&apikey={self.api_key}&{stringParams}"
        else:
            return f"{API_URL}{path}?_sdk=python_v{__version__}&apikey={self.api_key}"

    def _process_multiple_pages(
        self, total: int, url: str, payload: Dict, data: Dict, headers
    ) -> List:
        size = data.get("size", 1000)
        offsets = list(range(0, total, size))
        shuffle(offsets)

        with tqdm(
            total=total, desc="Loading from API", disable=(len(offsets) == 1)
        ) as pbar:
            with ThreadPool(self._N_THREADS) as pool:
                logger.info(
                    f"{total} Results to retrieve."
                    f" Sending {len(offsets)}"
                    f" post requests in parallel using {self._N_THREADS} threads."
                )

                func = functools.partial(
                    _send_post_request_data,
                    url=url,
                    payload=payload,
                    size=size,
                    progress_bar=pbar,
                    headers=headers,
                )

                return pool.map(func, offsets)

    @staticmethod
    def _cleanse_payload(payload: Dict) -> Dict:
        exclude_params = payload.get("exclude", {})
        payload["exclude"] = filter_empty_values(exclude_params)

        return filter_empty_values(payload)

    @staticmethod
    def _calculate_total(response: Dict) -> int:
        """Get total number of pages, if total key does not exist, return 1"""
        return response.get("total", 1)

    @staticmethod
    def _flatten_response(response) -> List:
        return [x for y in response for x in y]


def _send_post_request_data(
    offset, url, payload, size, progress_bar: tqdm, headers
) -> List:
    # noinspection PyBroadException
    try:
        progress_bar.update(size)
    except Exception:
        logger.warn("Could not update progress bar")

    dict_response = _send_post_request(url, payload, size, offset, headers)

    return dict_response.get("data", [])


def _send_post_request(url, payload, size, offset, headers) -> Dict:
    logger.debug(f"Sending post request, offset: {offset}, size: {size}")

    payload_with_offset = copy.deepcopy(payload)

    payload_with_offset["offset"] = offset
    payload_with_offset["cm_offset"] = offset
    payload_with_offset["size"] = size
    payload_with_offset["cm_size"] = size

    response = retry_post(url, json=payload_with_offset, headers=headers)

    return _handle_response(response, headers, payload_with_offset)


def _handle_response(
    response: Response, headers: Dict = None, payload: Dict = None
) -> Dict:
    if not response.ok:
        logger.error(response.reason)
        logger.error(response.status_code)
        logger.error(response)

        # noinspection PyBroadException
        try:
            logger.error(response.json())
            message = response.json()["message"]
        except Exception:
            message = ""
            pass

        logger.error(f"payload: {payload}")
        error = f"[{response.status_code} {response.reason}]"

        raise ValueError(f"{error} {message}")

    else:
        try:
            if (
                headers is not None
                and "accept" in headers
                and headers["accept"] == "text/csv"
            ):
                # decode
                raw = response.content.decode("utf-8")

                # convert to dictionaries
                reader = csv.DictReader(raw.splitlines())

                # convert to JSON
                data = [dict(line) for line in reader]

                decoded = {
                    "data": data,
                    "total": int(response.headers["x-total"]),
                }

            else:
                decoded = response.json()
        except JSONDecodeError:
            logger.error("Could not decode response")
            decoded = {}
        except Exception as e:
            logger.error(e)
            decoded = {}

    return decoded


__client__ = None


def default_client() -> VortexaClient:
    """Instantiate VortexaClient as global variable."""
    global __client__

    if __client__ is None:
        __client__ = create_client()

    return __client__


def create_client() -> VortexaClient:
    """Create new VortexaClient."""
    logger.info("Creating new VortexaClient")

    api_key = _load_api_key()
    verify_api_key_format(api_key)
    _warn_user_if_sdk_version_outdated()

    return VortexaClient(api_key=api_key)


def set_client(client) -> None:
    """Set the global client, used by all endpoints."""
    global __client__
    __client__ = client
    logger.debug(
        f"global __client__ has been set {__client__.__class__.__name__} \n"
    )


def _warn_user_if_sdk_version_outdated() -> None:
    """Warn users if their SDK version is outdated"""
    try:
        latest_sdk_version, sdk_outdated_check = is_sdk_version_outdated()
        if sdk_outdated_check:
            logger.warning(
                f"You are using {sdk_pkg_name} version {__version__}, however version {latest_sdk_version} is available.\n"
                f"You should consider upgrading via the 'pip install {sdk_pkg_name} --upgrade' command."
            )
    except Exception:
        logger.warning(
            f"Outdated SDK version check could not be completed. \n"
        )


def _load_api_key():
    """Read API Key from environment variables else user input"""
    try:
        return os.environ["VORTEXA_API_KEY"]
    except KeyError:
        return getpass.getpass("Vortexa API Key: ")
    except Exception:
        raise KeyError(
            "You must either set the VORTEXA_API_KEY environment variable, or interactively enter your Vortexa API key."
            " Your API key can be found at https://docs.vortexa.com"
        )


def verify_api_key_format(api_key: str) -> None:
    """Verify that the api_key is a valid UUID string"""
    try:
        uuid.UUID(api_key)
    except ValueError:
        raise ValueError(
            "Incorrect API key set. The Vortexa API key must be of the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx "
            " Your API key can be found at https://docs.vortexa.com"
        )
