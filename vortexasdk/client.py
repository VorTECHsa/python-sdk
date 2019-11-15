import os
from abc import ABC
from typing import List

import requests
from requests import Response

from vortexasdk.api.shared_types import ID
from vortexasdk.endpoints.endpoints import API_URL


class AbstractVortexaClient(ABC):
    """Base client."""

    def get_reference(self, resource: str, id: ID) -> str:
        """Lookup reference data."""
        raise NotImplementedError

    def search(self, resource: str, **data) -> List:
        """Search."""
        raise NotImplementedError


class VortexaClient(AbstractVortexaClient):
    """The API client responsible for calling Vortexa's Public API."""

    _DEFAULT_PAGE_LOAD_SIZE = 10000

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource: str, id: ID) -> str:
        """Lookup reference data."""
        url = self._create_url(f'{resource}/{id}')
        response = requests.get(url)
        return self._handle_response(response)['data']

    def search(self, resource: str, **data) -> List:
        """Search using `resource` using `**data` as filter params."""
        url = self._create_url(resource)

        payload = {k: v for k, v in data.items() if v is not None}

        offset = 0
        more = True
        responses = []

        while more:
            response = self._sent_post_request(url, payload, offset)
            offset += payload.get('size', self._DEFAULT_PAGE_LOAD_SIZE)
            responses += response['data']
            print(f'Adding {len(response["data"])} records to responses. len(all_responses): {len(responses)}')

            if offset > response['total']:
                print(f'Finishing. offset: {offset}, total_records: {response["total"]}')
                more = False

        return responses

    def _create_url(self, path: str) -> str:
        return f'{API_URL}{path}?apikey={self.api_key}'

    def _sent_post_request(self, url, payload, offset):
        print(f'Sending post request, offset: {offset}')
        payload["offset"] = offset
        payload["cm_offset"] = offset

        response = requests.post(url, json=payload)

        return self._handle_response(response, payload)

    @staticmethod
    def _handle_response(response: Response, payload=None):
        if response.ok:
            return response.json()
        else:
            print(response.reason)
            print(response.json())
            print(f'payload: {payload}')
            raise Exception(response)


__client__ = None


def default_client() -> VortexaClient:
    """Instantiate VortexaClient as global variable."""
    global __client__

    if __client__ is None:

        try:
            api_key = os.environ["VORTEXA_API_KEY"]
        except KeyError:
            raise KeyError("VORTEXA_API_KEY environment variable is required to use the VortexaSDK")

        __client__ = VortexaClient(api_key=api_key)

    return __client__


def set_client(client) -> None:
    """Set the global client, used by all endpoints."""
    global __client__
    __client__ = client
    print(f'global __client__ has been set {__client__.__class__.__name__}')
