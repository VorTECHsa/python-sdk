"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Futilisation_timeseries.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union
from vortexasdk.endpoints.breakdown_result import BreakdownResult
from vortexasdk.endpoints.endpoints import FLEET_UTILISATION_TIMESERIES
from vortexasdk.api.shared_types import Tag, to_ISODate

from vortexasdk.api import ID
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list, sts_param_value


class FleetUtilisationTimeseries(Search):
    """
    _<span style="color:red">DEPRECATION NOTE: This endpoint is deprecated. Please refer to Freight Metrics for the new endpoint</span>._

    Please note: you will require a subscription to our Freight module to access this endpoint.
    """

    def __init__(self):
        Search.__init__(self, FLEET_UTILISATION_TIMESERIES)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        timeseries_frequency: str = None,
        timeseries_property: str = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_charterers: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_effective_controllers: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_vessel_flags: Union[ID, List[ID]] = None,
        filter_vessel_ice_class: Union[ID, List[ID]] = None,
        filter_vessel_propulsion: Union[ID, List[ID]] = None,
        filter_vessel_tags: Union[List[Tag], Tag] = None,
        filter_vessel_risk_levels: Union[str, List[str]] = None,
        filter_ship_to_ship: bool = None,
        filter_charterer_exists: bool = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_dwt_min: int = None,
        filter_vessel_dwt_max: int = None,
        filter_activity: str = None,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        filter_vessel_status: Union[str, List[str]] = None,
        exclude_origins: Union[ID, List[ID]] = None,
        exclude_destinations: Union[ID, List[ID]] = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[ID, List[ID]] = None,
        exclude_charterers: Union[ID, List[ID]] = None,
        exclude_owners: Union[ID, List[ID]] = None,
        exclude_effective_controllers: Union[ID, List[ID]] = None,
        exclude_vessel_flags: Union[ID, List[ID]] = None,
        exclude_vessel_ice_class: Union[ID, List[ID]] = None,
        exclude_vessel_propulsion: Union[ID, List[ID]] = None,
        exclude_vessel_tags: Union[List[Tag], Tag] = None,
        exclude_vessel_risk_levels: Union[ID, List[ID]] = None,
    ) -> BreakdownResult:
        """

        Daily average count of unique vessels. For frequencies other than ‘day’, the values returned are
        calculated by summing the average counts per day within the frequency specified, and returning
        the average count per day.

        # Arguments
            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of the following: ['day', 'week', 'doe_week', 'month', 'quarter', 'year'].

            timeseries_property: Property on the vessel movement used to build the value of the aggregation. By default it is “quantity”. Must be one of the following: `'quantity’`, `‘vessel_class’`,
            `‘vessel_flag’`, `‘origin_region’`, `‘origin_trading_region’`, `‘origin_trading_sub_region’`, `‘origin_country’`,
            `‘origin_port’`, `‘origin_terminal’`, `‘destination_region’`, `‘destination_trading_region’`,
            `‘destination_trading_sub_region’`, `‘destination_country’`, `‘destination_port’`, `‘destination_terminal’`,
            `'product_group'`, `'product_group_product'`, `'product_category'`, `'product_grade'`.

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_charterers: A charterer entity ID, or list of product IDs to filter on.

            filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessel_flags: A vessel flag ID, or list of vessel flag IDs to filter on.

            filter_vessel_ice_class: A vessel ice class ID, or list of vessel ice class IDs to filter on.

            filter_vessel_propulsion: A vessel propulsion ID, or list of vessel propulsion IDs to filter on.

            filter_vessel_tag: A time bound vessel tag, or list of time bound vessel tags to filter on.

            filter_vessel_risk_levels: A vessel risk level, or list of vessel risk levels to filter on.

            filter_vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

            filter_vessel_age_min: A number between 1 and 100 (representing years).

            filter_vessel_age_max: A number between 1 and 100 (representing years).

            filter_vessel_age_min: A number between 0 and 550000.

            filter_vessel_age_max: A number between 0 and 550000.

            filter_activity: Movement activity on which to base the time filter. Must be one of: `'loading_state'`,
             `'oil_on_water_state'`, `'unloading_state'`, `'ship_to_ship'`, `'storing_state'`, `'transiting_state'`

            filter_vessel_status: The vessel status on which to base the filter. Enter 'vessel_status_ballast' for ballast vessels, 'vessel_status_laden_known' for laden vessels with known cargo (i.e. a type of cargo that Vortexa currently tracks) or 'any_activity' for any other vessels.

            filter_charterer_exists: A boolean to include or exclude the records to those that have a charterer.

            filter_ship_to_ship: A boolean to include or exclude the records to those that are involved in an STS.

            exclude_products: A product ID, or list of product IDs to exclude.

            exclude_charterers: A charterer entity ID, or list of product IDs to exclude.

            exclude_effective_controllers: An effective controller ID, or list of effective controller IDs to exclude.

            exclude_origins: A geography ID, or list of geography IDs to exclude.

            exclude_destinations: A geography ID, or list of geography IDs to exclude.

            exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

            exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

            exclude_vessel_flags: A vessel flag ID, or list of vessel flag IDs to filter on.

            exclude_vessel_ice_class: A vessel ice class ID, or list of vessel ice class IDs to exclude.

            exclude_vessel_propulsion: A vessel propulsion ID, or list of vessel propulsion IDs to exclude.

            exclude_vessel_tags: A time bound vessel tag, or list of time bound vessel tags to exclude.

            exclude_vessel_risk_levels: A vessel risk level, or list of vessel risk levels to exclude.

        # Returns
        `BreakdownResult`

        # Example
        _Utilisation of laden vessels carrying Crude/Condensate, between Middle East and China over the last 7 days, by vessel_class breakdown._

        ```python
        >>> from vortexasdk import FleetUtilisationTimeseries
        >>> from datetime import datetime
        >>> search_result = FleetUtilisationTimeseries().search(
        ...    filter_vessel_status="vessel_status_laden_known",
        ...    filter_products="54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11",
        ...    filter_origins="80aa9e4f3014c3d96559c8e642157edbb2b684ea0144ed76cd20b3af75110877",
        ...    filter_destinations="934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2",
        ...    filter_time_min=datetime(2021, 1, 11),
        ...    filter_time_max=datetime(2021, 1, 18),
        ...    timeseries_frequency="day",
        ...    timeseries_property="vessel_class")
        >>> df = search_result.to_df()

        ```

        Gives the following:

        |    | key                      |     value |     count |   breakdown.0.label | breakdown.0.value |breakdown.0.count |
        |---:|:-------------------------|----------:|----------:|--------------------:|------------------:|-----------------:|
        |  0 | 2021-01-11 00:00:00+00:00| 76        | 76        | "vlcc_plus"         | 70                | 70               |
        |  1 | 2021-01-12 00:00:00+00:00| 74        | 74        | "vlcc_plus"         | 68                | 68               |
        |  2 | 2021-01-13 00:00:00+00:00| 76        | 76        | "vlcc_plus"         | 69                | 69               |
        |  3 | 2021-01-14 00:00:00+00:00| 76        | 76        | "vlcc_plus"         | 68                | 68               |
        |  4 | 2021-01-15 00:00:00+00:00| 76        | 76        | "vlcc_plus"         | 68                | 68               |
        |  5 | 2021-01-16 00:00:00+00:00| 76        | 76        | "vlcc_plus"         | 68                | 68               |
        |  6 | 2021-01-17 00:00:00+00:00| 75        | 75        | "vlcc_plus"         | 67                | 67               |
        |  7 | 2021-01-18 00:00:00+00:00| 74        | 74        | "vlcc_plus"         | 66                | 66               |

        """

        sts_filter = sts_param_value(filter_ship_to_ship)

        crossfilters = {
            "filter_ship_to_ship": sts_filter["x_filter"],
            # if charterer toggle is True, apply cross filter
            # else make it false
            "filter_charterer_exists": filter_charterer_exists == True,
        }

        exclude_params: Dict[str, Any] = {
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_owners": convert_to_list(exclude_owners),
            "filter_effective_controllers": convert_to_list(
                exclude_effective_controllers
            ),
            "filter_origins": convert_to_list(exclude_origins),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_vessel_flags": convert_to_list(exclude_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                exclude_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                exclude_vessel_propulsion
            ),
            "filter_vessel_risk_levels": convert_to_list(
                exclude_vessel_risk_levels
            ),
            "filter_ship_to_ship": sts_filter["exclude"],
        }

        api_params: Dict[str, Any] = {
            "timeseries_frequency": timeseries_frequency,
            "timeseries_property": timeseries_property,
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_dwt_min": filter_vessel_dwt_min,
            "filter_vessel_dwt_max": filter_vessel_dwt_max,
            "filter_vessel_status": convert_to_list(filter_vessel_status),
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_effective_controllers": convert_to_list(
                filter_effective_controllers
            ),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessel_flags": convert_to_list(filter_vessel_flags),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_vessel_ice_class": convert_to_list(
                filter_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                filter_vessel_propulsion
            ),
            "vessel_tags": convert_to_list(filter_vessel_tags),
            "vessel_tags_excluded": convert_to_list(exclude_vessel_tags),
            "filter_vessel_risk_levels": convert_to_list(
                filter_vessel_risk_levels
            ),
            "filter_ship_to_ship": filter_ship_to_ship,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "exclude": exclude_params,
            "crossfilters": crossfilters,
        }

        response = super().search_with_client(**api_params)

        return BreakdownResult(
            records=response["data"], reference=response["reference"]
        )
