from typing import List

import pandas as pd

from python_sdk.api.entities import CargoMovementEntity
from python_sdk.constants import CARGO_MOVEMENTS_RESOURCE
from python_sdk.operations import Search
from python_sdk.search_result import SearchResult


class CargoMovementsSearchResult(SearchResult):

    def to_list(self) -> List[CargoMovementEntity]:
        """Represent cargo movements as a list of dictionaries."""
        return super().to_list()

    def to_df(self, columns) -> pd.DataFrame:

        if columns is None:
            columns = ['cargo_movement_id', 'quantity']

        df = pd.DataFrame(self._result)

        if columns == 'all':
            return df
        else:
            return df


class CargoMovements(Search):
    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_MOVEMENTS_RESOURCE)

    def search(self,
               filter_activity: str = "loading_state",
               filter_time_min: str = "2019-10-01T00:00:00.000Z",
               filter_time_max: str = "2019-10-01T01:00:00.000Z",
               include_definition: bool = True,
               cm_unit: str = 'b',

               filter_charterers: List[str] = None,
               filter_destinations: List[str] = None,
               filter_origins: List[str] = None,
               filter_owners: List[str] = None,
               filter_products: List[str] = None,
               filter_vessels: List[str] = None,
               filter_storage_locations: List[str] = None,
               filter_ship_to_ship_locations: List[str] = None,
               filter_waypoints: List[str] = None,
               disable_geographic_exclusion_rules: bool = None,
               ) -> CargoMovementsSearchResult:
        """

        # Arguments
            filter_activity: Movement activity on which to base the time filter. It can be a filter for a
             specific timestamp, which looks for it within the specified time-frame.

            filter_time_min: The start date of the time filter.

            filter_time_max: The end date of the time filter.

            include_definition: A list of grade or grade group identifiers to filter by.

            cm_unit:

            filter_charterers:

            filter_destinations: A list of geographical identifiers to apply to the destination filter.

            filter_origins: A list of geographical identifiers to apply to the origin filter.

            filter_owners:

            filter_products:

            filter_vessels: A list of vessel identifiers to filter by.

            filter_storage_locations:

            filter_ship_to_ship_locations:

            filter_waypoints: A list of geographical identifiers to apply to the waypoint filter.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
            List of cargo movements matching all the search parameters.


        # Example
        Let's search for all VLCCs that loaded from `Rotterdam [NL]` on the morning of 1st December 2018.

        ```python

        >>> result = CargoMovements().search(
            filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
            filter_activity='loading_state',
            filter_time_min="2018-12-01T00:00:00.000Z",
            filter_time_max="2018-12-01T12:00:00.000Z",
        )
        ```

        """
        search_params = {
            # Compulsory search parameters
            'filter_activity': filter_activity,
            'filter_time_min': filter_time_min,
            'filter_time_max': filter_time_max,
            'include_definition': include_definition,
            'cm_unit': cm_unit,
            'size': self._MAX_PAGE_RESULT_SIZE,
            'cm_size': self._MAX_PAGE_RESULT_SIZE,
            # cm_size is used by the api https://docs.vortexa.com/reference/POST/cargo-movements/search

            "filter_charterers": filter_charterers,
            "filter_destinations": filter_destinations,
            "filter_origins": filter_origins,
            "filter_owners": filter_owners,
            "filter_products": filter_products,
            "filter_vessels": filter_vessels,
            "filter_storage_locations": filter_storage_locations,
            "filter_ship_to_ship_locations": filter_ship_to_ship_locations,
            "filter_waypoints": filter_waypoints,
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules
        }

        return CargoMovementsSearchResult(super().search(**search_params))
