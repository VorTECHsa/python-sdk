"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Futilisation_destination_breakdown.ipynb)
"""
from typing import Any, Dict, List, Union
from datetime import datetime
from vortexasdk.endpoints.endpoints import (
    FLEET_UTILISATION_DESTINATION_BREAKDOWN,
)
from vortexasdk.endpoints.reference_breakdown_result import (
    ReferenceBreakdownResult,
)

from vortexasdk.api import ID
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list, sts_param_value
from vortexasdk.api.shared_types import to_ISODate


class FleetUtilisationDestinationBreakdown(Search):
    """
    _<span style="color:red">DEPRECATION NOTE: This endpoint is deprecated. Please refer to Freight Metrics for the new endpoint</span>._

    Please note: you will require a subscription to our Freight module to access this endpoint.
    """

    def __init__(self):
        Search.__init__(self, FLEET_UTILISATION_DESTINATION_BREAKDOWN)

    def search(
        self,
        breakdown_unit: str = None,
        breakdown_size: int = None,
        breakdown_geography: str = None,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        unit: str = "b",
        filter_activity: str = None,
        filter_charterers: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_effective_controllers: Union[ID, List[ID]] = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_vessel_status: str = None,
        filter_ship_to_ship: bool = None,
        filter_charterer_exists: bool = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_dwt_min: int = None,
        filter_vessel_dwt_max: int = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_vessel_flags: Union[ID, List[ID]] = None,
        filter_vessel_ice_class: Union[ID, List[ID]] = None,
        filter_vessel_propulsion: Union[ID, List[ID]] = None,
        exclude_origins: Union[ID, List[ID]] = None,
        exclude_destinations: Union[ID, List[ID]] = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[str, List[str]] = None,
        exclude_charterers: Union[ID, List[ID]] = None,
        exclude_owners: Union[ID, List[ID]] = None,
        exclude_effective_controllers: Union[ID, List[ID]] = None,
        exclude_vessel_flags: Union[ID, List[ID]] = None,
        exclude_vessel_ice_class: Union[ID, List[ID]] = None,
        exclude_vessel_propulsion: Union[ID, List[ID]] = None,
    ) -> ReferenceBreakdownResult:
        """
        Number of unique vessels by destination.

        # Arguments
            breakdown_unit: Units to aggregate upon. Must be one of the following: `'b'`, `'t'`, `'cbm'`, `'bpd'`, `'tpd'`, `'mpd'`.

            breakdown_size: Number of top geographies to return.

            breakdown_geography: Geography hierarchy of the destination to aggregate upon. Must be one of the following: `'berth'`, `'terminal'`, `'port'`,`'country'`, `'shipping_region'`,
            `'region'`,`'trading_block'`,`'trading_region'`,`'trading_subregion'`,`'sts_zone'`,`'waypoint'`.

            filter_activity: Movement activity on which to base the time filter. Must be one of: `'loading_state'`,
             `'loading_start'`, `'loading_end'`, `'identified_for_loading_state'`, `'unloading_state'`, `'unloading_start'`,
              `'unloading_end'`, `'unloaded_state'`, `'storing_state'`, `'storing_start'`, `'storing_end'`, `'transiting_state'`,
               `'any_activity'`.

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            unit: Unit of measurement. Enter `'b'` for barrels or `'t'` for tonnes.

            filter_charterers: A charterer ID, or list of charterer IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessel_status: The vessel status on which to base the filter. Enter `'vessel_status_ballast'` for ballast vessels, `'vessel_status_laden_known'` for laden vessels with known cargo (i.e. a type of cargo that Vortexa currently tracks) or `'vessel_status_laden_unknown'` for laden vessels with unknown cargo (i.e. a type of cargo that Vortexa currently does not track).

            filter_vessel_age_min: A number between 1 and 100 (representing years).

            filter_vessel_age_max: A number between 1 and 100 (representing years).

            filter_vessel_dwt_min: A number representing minimum deadweight tonnage of a vessel.

            filter_vessel_dwt_max: A number representing maximum deadweight tonnage of a vessel.

            filter_vessel_scrubbers: Either inactive `'disabled'`, or included `'inc'` or excluded `'exc'`.

            filter_vessel_flags: A geography ID, or list of geography IDs to filter on.

            filter_vessel_ice_class: An attribute ID, or list of attribute IDs to filter on.

            filter_vessel_propulsion: An attribute ID, or list of attribute IDs to filter on.

            filter_charterer_exists: A boolean to include or exclude the records to those that have a charterer.

            filter_ship_to_ship: A boolean to include or exclude the records to those that are involved in an STS.

            exclude_origins: A geography ID, or list of geography IDs to exclude.

            exclude_destinations: A geography ID, or list of geography IDs to exclude.

            exclude_products: A product ID, or list of product IDs to exclude.

            exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

            exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

            exclude_charterers: A charterer ID, or list of charterer IDs to exclude.

            exclude_effective_controllers: An effective controller ID, or list of effective controller IDs to exclude.

            exclude_vessel_flags: A geography ID, or list of geography IDs to exclude.

            exclude_vessel_ice_class: An attribute ID, or list of attribute IDs to exclude.

            exclude_vessel_propulsion: An attribute ID, or list of attribute IDs to exclude.


        # Returns
        `ReferenceBreakdownResult`

        # Example
        _Top 5 countries by number of unique vessels by destination country breakdown, in the last quarter._

        ```python
        >>> from vortexasdk import FleetUtilisationDestinationBreakdown, Vessels
        >>> from datetime import datetime
        >>> search_result = FleetUtilisationDestinationBreakdown().search(
        ...    breakdown_geography='country',
        ...    breakdown_size='5',
        ...    filter_time_min=datetime(2020, 10, 18),
        ...    filter_time_max=datetime(2021, 1, 18))
        >>> df = search_result.to_df()

        ```

        returns

        |      |key                                                               | label         |value       |count |
        |-----:|:-----------------------------------------------------------------|:--------------|:-----------|-----:|
        |0     | 934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2 | China         |3305        |16226 |
        |1     | 50182d9d05051a6c8d24f0514d4ee828da6eaa29eacbb11cfe368f51526328ce | Japan         |1248        |10683 |
        |2     | 2d92cc08f22524dba59f6a7e340f132a9da0ce9573cca968eb8e3752ef17a963 | United States |2017        |6092  |
        |3     | bcd7dddaf951959ebf6076a3a594b426a246d3bffe13339b10d04e45f222e011 | South Korea   |1543        |4883  |
        |4     | 3267ef2a83a749052c87e981f1bb12c6396acf590b4b1cd3316cf8f8c5aeb7bc | Malaysia      |1539        |4495  |

        """

        sts_filter = sts_param_value(filter_ship_to_ship)

        crossfilters = {
            "filter_ship_to_ship": sts_filter["x_filter"],
            # if charterer toggle is True, apply cross filter
            # else make it false
            "filter_charterer_exists": filter_charterer_exists == True,
        }

        exclude_params: Dict[str, Any] = {
            "filter_origins": convert_to_list(exclude_origins),
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_owners": convert_to_list(exclude_owners),
            "filter_effective_controllers": convert_to_list(
                exclude_effective_controllers
            ),
            "filter_vessel_flags": convert_to_list(exclude_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                exclude_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                exclude_vessel_propulsion
            ),
        }

        api_params: Dict[str, Any] = {
            "breakdown_unit": breakdown_unit,
            "breakdown_size": breakdown_size,
            "breakdown_geography": breakdown_geography,
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "unit": unit,
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_effective_controllers": convert_to_list(
                filter_effective_controllers
            ),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessel_status": filter_vessel_status,
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_dwt_min": filter_vessel_dwt_min,
            "filter_vessel_dwt_max": filter_vessel_dwt_max,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "filter_vessel_flags": convert_to_list(filter_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                filter_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                filter_vessel_propulsion
            ),
            "crossfilters": crossfilters,
            "exclude": exclude_params,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return ReferenceBreakdownResult(
            records=response["data"], reference=response["reference"]
        )
