from typing import List

from python_sdk.api.resources.vessel import VesselClass
from python_sdk.constants import CARGO_MOVEMENTS_RESOURCE
from python_sdk.operations import Search


class CargoMovements(Search):
    def __init__(self):
        Search.__init__(self, CARGO_MOVEMENTS_RESOURCE)

    def search(self,
               filter_activity: str = "loading_state",
               filter_time_min: str = "2018-10-30T00:00:00.000Z",
               filter_time_max: str = "2019-10-30T23:59:59.999Z",
               include_definition: bool = True,
               cm_unit: str = 'b',
               cm_size: int = 1,

               filter_charterers: List[str] = None,
               filter_destinations: List[str] = None,
               filter_origins: List[str] = None,
               filter_owners: List[str] = None,
               filter_products: List[str] = None,
               filter_vessels: List[VesselClass] = None,
               filter_storage_locations: List[str] = None,
               filter_ship_to_ship_locations: List[str] = None,
               filter_waypoints: List[str] = None,
               disable_geographic_exclusion_rules: bool = None,
               ):
        search_params = {
            # Compulsory search parameters
            'filter_activity': filter_activity,
            'filter_time_min': filter_time_min,
            'filter_time_max': filter_time_max,
            'include_definition': include_definition,
            'cm_unit': cm_unit,
            'cm_size': cm_size,

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

        return super().search(**search_params)
