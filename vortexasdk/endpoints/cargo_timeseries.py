"""Time Series Endpoint."""
from datetime import datetime
from typing import List, Union

from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.conversions import (
    convert_to_corporation_ids,
    convert_to_geography_ids,
    convert_to_product_ids,
    convert_to_vessel_ids,
)
from vortexasdk.endpoints.endpoints import CARGO_TIMESERIES_RESOURCE
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.operations import Search


class CargoTimeSeries(Search):
    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_TIMESERIES_RESOURCE)

    def search(
        self,
        filter_activity: str,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        cm_unit: str = "b",
        filter_charterers: Union[str, List[str]] = None,
        filter_destinations: Union[str, List[str]] = None,
        filter_origins: Union[str, List[str]] = None,
        filter_owners: Union[str, List[str]] = None,
        filter_products: Union[str, List[str]] = None,
        filter_vessels: Union[str, List[str]] = None,
        filter_storage_locations: Union[str, List[str]] = None,
        filter_ship_to_ship_locations: Union[str, List[str]] = None,
        filter_waypoints: Union[str, List[str]] = None,
        disable_geographic_exclusion_rules: bool = None,
    ) -> TimeSeriesResult:
        """

        Find CargoMovements matching the given search parameters.

        # Arguments
            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'unloaded_state', 'storing_state', 'storing_start', 'storing_end', 'transiting_state',
               'any_activity'].

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            cm_unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_corporations: A corporation, or list of corporations to filter on.

            filter_destinations: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_origins: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_owners: An owner, or list of owners to filter on. Both charterer/owner names or IDs can be entered here.

            filter_products: A product, or list of products to filter on. Both product names or IDs can be entered here.

            filter_vessels: A vessel, or list of vessels to filter on. Vessel name, imo, mmsi, vessel class, or vessel IDs can be entered here,

            filter_storage_locations: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            filter_ship_to_ship_locations: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            filter_waypoints: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
        `CargoMovementsResult`, containing all the cargo movements matching the given search terms.


        # Example

        * _Which cargoes were loaded from Rotterdam on the morning of 1st December 2018?_

        """
        params = {
            "filter_confidence": "high",
            "timeseries_frequency": "day",
            "timeseries_unit": "b",
            "timeseries_activity": filter_activity,
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "cm_unit": cm_unit,
            "size": self._MAX_PAGE_RESULT_SIZE,
            "filter_charterers": convert_to_corporation_ids(filter_charterers),
            "filter_owners": convert_to_corporation_ids(filter_owners),
            "filter_products": convert_to_product_ids(filter_products),
            "filter_vessels": convert_to_vessel_ids(filter_vessels),
            "filter_destinations": convert_to_geography_ids(
                filter_destinations
            ),
            "filter_origins": convert_to_geography_ids(filter_origins),
            "filter_storage_locations": convert_to_geography_ids(
                filter_storage_locations
            ),
            "filter_ship_to_ship_locations": convert_to_geography_ids(
                filter_ship_to_ship_locations
            ),
            "filter_waypoints": convert_to_geography_ids(filter_waypoints),
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules,
        }

        return TimeSeriesResult(super().search(**params))
