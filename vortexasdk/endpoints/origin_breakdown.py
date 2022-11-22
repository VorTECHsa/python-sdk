"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Forigin_breakdown.ipynb)
"""
from typing import Any, Dict, List, Union
from datetime import datetime
from vortexasdk.api.shared_types import Tag, to_ISODate
from vortexasdk.endpoints.reference_breakdown_result import (
    ReferenceBreakdownResult,
)

from vortexasdk.api import ID
from vortexasdk.endpoints.endpoints import ORIGIN_BREAKDOWN_RESOURCE
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class OriginBreakdown(Search):

    _INCLUDE_REFERENCE_DATA = True

    def __init__(self):
        Search.__init__(self, ORIGIN_BREAKDOWN_RESOURCE)

    def search(
        self,
        breakdown_geography: str = "country",
        breakdown_unit_average_basis: str = None,
        filter_activity: str = "any_activity",
        breakdown_unit: str = "b",
        disable_geographic_exclusion_rules: bool = None,
        breakdown_size: int = None,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        filter_products: Union[ID, List[ID]] = None,
        filter_charterers: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_effective_controllers: Union[ID, List[ID]] = None,
        filter_vessel_flags: Union[ID, List[ID]] = None,
        filter_vessel_ice_class: Union[ID, List[ID]] = None,
        filter_vessel_propulsion: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_storage_locations: Union[ID, List[ID]] = None,
        filter_waypoints: Union[ID, List[ID]] = None,
        filter_ship_to_ship_locations: Union[ID, List[ID]] = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_vessel_tags: Union[List[Tag], Tag] = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[str, List[str]] = None,
        exclude_owners: Union[ID, List[ID]] = None,
        exclude_effective_controllers: Union[ID, List[ID]] = None,
        exclude_charterers: Union[ID, List[ID]] = None,
        exclude_vessel_flags: Union[ID, List[ID]] = None,
        exclude_destinations: Union[ID, List[ID]] = None,
        exclude_origins: Union[ID, List[ID]] = None,
        exclude_waypoints: Union[ID, List[ID]] = None,
        exclude_storage_locations: Union[ID, List[ID]] = None,
        exclude_ship_to_ship_locations: Union[ID, List[ID]] = None,
        exclude_vessel_ice_class: Union[ID, List[ID]] = None,
        exclude_vessel_propulsion: Union[ID, List[ID]] = None,
        exclude_vessel_tags: Union[List[Tag], Tag] = None,
    ) -> ReferenceBreakdownResult:

        """
         Origin locations breakdown aggregation by geographic area

         # Arguments

             breakdown_unit_average_basis: Per day metrics only - movement activity on which to base the average metric. Can be one of state properties of a cargo movement: `identified_for_loading_state`, `loading_state`, `transiting_state`, `storing_state`, `ship_to_ship`, `unloading_state`, `unloaded_state`, `oil_on_water_state`, `unknown_state`, or one of time properties of a cargo movement: `identified_for_loading_at`, `loading_start`, `loading_end`, `storing_start`, `storing_end`, `ship_to_ship_start`, `ship_to_ship_end`, `unloading_start`, `unloading_end`.

             breakdown_unit: Units to aggregate upon. Must be one of the following: `'b'`, `'t'`, `'cbm'`, `'bpd'`, `'tpd'`, `'mpd'`.

             breakdown_geography: Geography hierarchy of the origin to aggregate upon. Must be one of the following: `'terminal'`, `'port'`,`'country'`, `'shipping_region'`,
             `'region'`,`'trading_block'`,`'trading_region'`,`'trading_subregion'`,`'sts_zone'`,`'waypoint'`.

             breakdown_size: Number of top geographies to return. Default is 5.

             disable_geographic_exclusion_rules: A boolean which specifies whether certain movements should be excluded, based on a combination of their origin and destination.

             filter_activity: Cargo movement activity on which to base the time filter. The endpoint only includes cargo
             movements matching that match this filter in the aggregations. Must be one of ['loading_state',
              'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
               'unloading_end', 'storing_state', 'storing_start', 'storing_end', 'transiting_state'].

             filter_time_min: The UTC start date of the time filter.

             filter_time_max: The UTC end date of the time filter.

             filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

             filter_vessel_flags: A vessel flag ID, or list of vessel flag IDs to filter on.

             filter_vessel_ice_class: An ice class ID, or list of ice class IDs to filter on.

             filter_vessel_propulsion: An propulsion means ID, or list of propulsion means IDs to filter on.

             filter_charterers: An commercial entity ID, or list of commercial entity IDs to filter on.

             filter_origins: A geography ID, or list of geography IDs to filter on.

             filter_destinations: A geography ID, or list of geography IDs to filter on.

             filter_storage_locations: A geography ID, or list of geography IDs to filter on.

             filter_waypoints: A geography ID, or list of geography IDs to filter on.

             filter_ship_to_ship_locations: A geography ID, or list of geography IDs to filter on.

             filter_products: A product ID, or list of product IDs to filter on.

             filter_vessels: A vessel ID, or list of vessel IDs to filter on.

             filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

             filter_vessel_age_min: A number between 1 and 100 (representing years).

             filter_vessel_age_max: A number between 1 and 100 (representing years).

             filter_vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

             filter_vessel_tags: A time bound vessel tag, or list of time bound vessel tags to filter on.

             exclude_products: A product ID, or list of product IDs to exclude.

             exclude_vessel_flags: A vessel flag ID, or list of vessel flag IDs to exclude.

             exclude_vessel_ice_class: An ice class ID, or list of ice class IDs to exclude.

             exclude_vessel_propulsion: An propulsion means ID, or list of propulsion means IDs to exclude.

             exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

             exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

             exclude_effective_controllers: An effective controller ID, or list of effective controller IDs to exclude.

             exclude_vessel_location: A location ID, or list of location IDs to exclude.

             exclude_destinations: A location ID, or list of location IDs to exclude.

             exclude_origins: A location ID, or list of location IDs to exclude.

             exclude_storage_locations: A location ID, or list of location IDs to exclude.

             exclude_waypoints: A location ID, or list of location IDs to exclude.

             exclude_ship_to_ship_locations: A location ID, or list of location IDs to exclude.

             exclude_vessel_tags: A time bound vessel tag, or list of time bound vessel tags to exclude.

         # Returns
         `ReferenceBreakdownResult`


         # Example
        _Breakdown by origin terminal of cargoes departing from the port of origin over the last 5 days, in tonnes._

         ```python
         >>> from vortexasdk import OriginBreakdown, Geographies
         >>> start = datetime(2019, 11, 10)
         >>> end = datetime(2019, 11, 15)
         >>> df = OriginBreakdown().search(
         ...        filter_activity="loading_end",
         ...        breakdown_geography="terminal",
         ...        breakdown_unit="t",
         ...        breakdown_size=5,
         ...        filter_time_min=start,
         ...        filter_time_max=end
         ... ).to_df()

         ```

         Gives the following:

         |    | key                                                             | label                                    | value    | count     |
         |---:|:----------------------------------------------------------------|-----------------------------------------:|---------:|----------:|
         |  0 | c3daea3cc9c5b3bd91c90882d42c2a418c4cf17b90ff12da3ac78444282a238a| Juaymah Crude Oil Terminal               | 3009799  | 24        |
         |  1 | 3a39cf841ece0c7cb879f72af01cb634191142e0de8010d5ef877fd66c2e8605| Houston Enterprise Terminal              | 776599   | 17        |
         |  2 | 345b7661310bc82a04e0a4edffd02c286c410c023b53edfb90ed3386640c0476| Arzew GL1Z/GL2Z LNG Terminal             | 381359   | 24        |
         |  3 | 9dfa3be1b42d1f5e80361b6f442b5217b486876ad0c25e382055887c9e231ad2| SabTank (PCQ-1) Al Jubail                | 238723   | 21        |
         |  4 | 4813dd7209e85b128cc2fbc7c08fef08d26259550210f28a5c7ff3ccd7b2ba61| Mailiao Industrial Park-Formosa Plastics | 118285   | 18        |

        """
        exclude_params: Dict[str, Any] = {
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_owners": convert_to_list(exclude_owners),
            "filter_effective_controllers": convert_to_list(
                exclude_effective_controllers
            ),
            "filter_origins": convert_to_list(exclude_origins),
            "filter_flags": convert_to_list(exclude_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                exclude_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                exclude_vessel_propulsion
            ),
            "filter_storage_locations": convert_to_list(
                exclude_storage_locations
            ),
            "filter_waypoints": convert_to_list(exclude_waypoints),
            "filter_ship_to_ship": convert_to_list(
                exclude_ship_to_ship_locations
            ),
        }

        api_params: Dict[str, Any] = {
            "breakdown_unit_average_basis": breakdown_unit_average_basis,
            "breakdown_unit": breakdown_unit,
            "breakdown_size": breakdown_size,
            "breakdown_geography": breakdown_geography,
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "filter_activity": filter_activity,
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessel_flags": convert_to_list(filter_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                filter_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                filter_vessel_propulsion
            ),
            "filter_owners": convert_to_list(filter_owners),
            "filter_effective_controllers": convert_to_list(
                filter_effective_controllers
            ),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_waypoints": convert_to_list(filter_waypoints),
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_storage_locations": convert_to_list(
                filter_storage_locations
            ),
            "filter_ship_to_ship_locations": convert_to_list(
                filter_ship_to_ship_locations
            ),
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "vessel_tags": convert_to_list(filter_vessel_tags),
            "vessel_tags_excluded": convert_to_list(exclude_vessel_tags),
            "exclude": exclude_params,
            "include_reference": self._INCLUDE_REFERENCE_DATA,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return ReferenceBreakdownResult(
            records=response["data"], reference=response["reference"]
        )
