from typing import Dict

from vortexasdk.api.id import ID
from vortexasdk.client import default_client
from vortexasdk.exceptions import InvalidAPIDataResponseException
from vortexasdk.logger import get_logger
from vortexasdk.search_response import SearchResponse
from vortexasdk.utils import filter_exact_match

logger = get_logger(__name__)


class Reference:
    """Lookup Vortexa Reference Data using an entity ID."""

    def __init__(self, resource):
        """
        Init.

        # Arguments
            resource: The vortexa endpoint used for reference lookups.

        """
        self._resource = resource

    def reference(self, id: ID) -> Dict:
        """
        Lookup reference data using ID.

        # Arguments
            id: ID of the entity we're looking up

        # Returns
        An entity matching the ID

        # Examples

        >>> Reference("/reference/geographies").reference(id='cfb8c4ef76585c3a37792b643791a0f4ff6d5656d5508927d8017319e21f2fca') # doctest: +SKIP

        """
        logger.info(
            f"Looking up {self.__class__.__name__} reference data with id: {id}"
        )

        data = default_client().get_reference(self._resource, id)

        assert len(data) <= 1, InvalidAPIDataResponseException(
            f"Server error: more than one record returned matching ID {id}"
        )
        try:
            return data[0]
        except IndexError:
            return {}


class Search:
    """Search Vortexa Reference Data."""

    def __init__(self, resource):
        """
        Init.

        # Arguments
            resource: Appropriate search resource

        """
        self._resource = resource

    # This method has been renamed from `search` to `search_with_client` to avoid type signature
    # issues with the `search` method in each endpoint class.
    def search_with_client(
        self,
        exact_term_match: bool = None,
        response_type: str = None,
        headers: dict = None,
        **api_params,
    ) -> SearchResponse:
        """
        Search Reference data filtering on `params`.

        # Arguments
            exact_term_match: Optional argument to filter names on exact matches
            api_params: Search parameters to be passed on to the API
            response_type: Optional type of the response - to handle endpoints which do not support paging

        # Returns
        Result of VortexaAPI call from hitting querying the `resource` endpoint filtering with `params`.

        # Examples

        >>> Search("/reference/vessels").search(term="DHT") # doctest: +SKIP

        """
        logger.info(f"Searching {self.__class__.__name__}")
        api_result = default_client().search(
            self._resource,
            response_type=response_type,
            headers=headers,
            **api_params,
        )

        logger.debug(
            f"{len(api_result)} results received from {self._resource}"
        )

        if exact_term_match:
            logger.debug("Filtering results on exact term match")
            return {
                "reference": api_result["reference"],
                "data": filter_exact_match(
                    api_params["term"], api_result["data"]
                ),
            }
        else:
            return api_result


class Record:
    """Lookup Vortexa Data using an record ID."""

    def __init__(self, resource):
        """
        Init.

        # Arguments
            resource: The Vortexa endpoint used for record lookups.

        """
        self._api_resource = resource

    def record(self, id: ID) -> Dict:
        """
        Lookup for single record using ID.

        # Arguments
            id: ID of the record we're looking up

        # Returns
        A record matching the ID

        # Examples

        >>> Record("/cargo-movement/").record(id='cfb8c4ef76585c3a37792b643791a0f4ff6d5656d5508927d8017319e21f2fca') # doctest: +SKIP

        """
        logger.info(
            f"Looking up {self.__class__.__name__} single record data with id: {id}"
        )

        data = default_client().get_record(self._api_resource, id)

        assert len(data) <= 1, InvalidAPIDataResponseException(
            f"Server error: more than one record returned matching ID {id}"
        )
        try:
            return data[0]
        except IndexError:
            return {}

    def record_with_params(self, id: ID, params: Dict) -> Dict:
        """
        Lookup for single record using ID and search params.

        # Arguments
            id: Cargo movement ID to lookup (long_id or short_id)

            params: Supported search params:
                'unit': enter 'b' for barrels, 't' for tonnes and 'cbm' for cubic meters

        # Returns
        A record matching the ID

        # Examples

        >>> Record("/cargo-movement").record(id='cfb8c4ef76585c3a37792b643791a0f4ff6d5656d5508927d8017319e21f2fca', {'unit': 'b'}) # doctest: +SKIP

        """
        logger.info(
            f"Looking up {self.__class__.__name__} single record data with id: {id}"
        )

        data = default_client().get_record_with_params(
            self._api_resource, id, params
        )

        assert len(data) <= 1, InvalidAPIDataResponseException(
            f"Server error: more than one record returned matching ID {id}"
        )
        try:
            return data[0]
        except IndexError:
            return {}
