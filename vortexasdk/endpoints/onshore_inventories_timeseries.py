"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fonshore_inventories_timeseries.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import CRUDE_ONSHORE_INVENTORIES_TIMESERIES
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class OnshoreInventoriesTimeseries(Search):
    """
    Please note: you will require a subscription to our Crude Onshore Inventories module to access this endpoint.
    """

    def __init__(self):
        Search.__init__(self, CRUDE_ONSHORE_INVENTORIES_TIMESERIES)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        corporate_entity_ids: Union[ID, List[ID]] = None,
        crude_confidence: List[str] = None,
        location_ids: Union[ID, List[ID]] = None,
        storage_types: List[str] = None,
        asset_tank_ids: Union[ID, List[ID]] = None,
        time_max: datetime = None,
        time_min: datetime = None,
        timeseries_frequency: str = None,
        timeseries_split_property: str = None,
        timeseries_unit: str = None,
        timeseries_unit_operator: str = None,
        exclude_corporate_entity_ids: List[str] = None,
        exclude_crude_confidence: List[str] = None,
        exclude_location_ids: Union[ID, List[ID]] = None,
        exclude_storage_types: List[str] = None,
    ) -> TimeSeriesResult:
        """

        Sum of crude onshore inventories storage and total capacity updated weekly. For frequencies other than 'week', the values returned are
        calculated by returning the final weekly onshore inventories 'quantity' bucket for the specified period.


        # Arguments

            corporate_entity_ids: An array of owner ID(s) to filter on.
            crude_confidence: An array of confidence metrics to filter on. Possible values are: `'confirmed’`, `‘probable’`, `‘unlikely’`
            location_ids: An array of geography ID(s) to filter on.
            storage_types: An array of storage types to filter on. Possible values are: `'refinery'`, `'commercial'`, `'spr'`
            asset_tank_ids: An array of unique Asset Tanks ID(s) to filter on - linked to the Asset Tank Reference data.
            time_min: The UTC start date of the time filter.
            time_max: The UTC end date of the time filter.
            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of the following: `'day'`, `'week'`, `'doe_week'`, `'month'`, `'year'`.
            timeseries_split_property: Property used to breakdown the aggregation. By default 'quantity' is used which returns only the total, but aggregations can be broken down
            by either `'crude_confidence'`, `'storage_type'`, `'location_country'`, `'location_port'`, `'location_region'`, `'location_shipping_region'`, `'location_trading_region'`,
            `'location_trading_subregion'`

            timeseries_unit: A numeric metric to be calculated for each time bucket. Must be either `'b'`, `'t'`, `'cbm'` corresponding to barrels, metric tonnes, cubic meters.
            timeseries_unit_operator: Argument must be either 'fill' (total in storage) or 'capacity' (total capacity).

            exclude_corporate_entity_ids: An array of owner ID(s) to exclude from the results,
            exclude_crude_confidence: An array of confidence metrics to exclude from the results
            exclude_location_ids: An array of geography ID(s) to exclude from the results
            exclude_storage_types: An array of storage types to exclude from the results

        # Returns
        `BreakdownResult`

        # Example
        _Total storage capacity across Europe for the first week of January 2021._

        ```python
        >>> from vortexasdk import OnshoreInventoriesTimeseries
        >>> from datetime import datetime
        >>> search_result = OnshoreInventoriesTimeseries().search(
        ...    location_ids=["f39d455f5d38907394d6da3a91da4e391f9a34bd6a17e826d6042761067e88f4"],
        ...    time_min=datetime(2021, 1, 5),
        ...    time_max=datetime(2021, 1, 12),
        ...    timeseries_frequency="week",
        ...    timeseries_split_property="location_country",
        ...    timeseries_unit="b",
        ...    timeseries_unit_operator="capacity",
        ...    ).to_list()

        ```
        Gives the following result:

        ```
        [
            BreakdownItem(key='2021-09-09T14:00:00.000Z',
            count=3769,
            value=994621677,
            breakdown=[
                {
                    'id': 'ee1de4914cc26e8f1326b49793b089131870d478714c07e0c99c56cb307704c5',
                    'label': 'Italy',
                    'value': 204482432,
                    'count': 762
                },
                {
                    'id': '2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3',
                    'label': 'UnitedKingdom',
                    'value': 113001186,
                    'count': 415
                },
                {
                    'id': '284c8d9831e1ac59c0cb714468856d561af722c8a2432c13a001f909b97e6b71',
                    'label': 'Germany',
                    'value': 93583672,
                    'count': 405
                },
                {
                    'id': 'e9e556620469f46a4dc171aef71073f5286a288da35c5883cac760446b0ceb46',
                    'label': 'France',
                    'value': 86652291,
                    'count': 327
                },
                ...
            ])
        ]
        ```
        """

        exclude_params: Dict[str, Any] = {
            "corporate_entity_ids": convert_to_list(
                exclude_corporate_entity_ids
            ),
            "crude_confidence": convert_to_list(exclude_crude_confidence),
            "location_ids": convert_to_list(exclude_location_ids),
            "storage_types": convert_to_list(exclude_storage_types),
        }

        api_params: Dict[str, Any] = {
            "corporate_entity_ids": corporate_entity_ids,
            "crude_confidence": crude_confidence,
            "location_ids": location_ids,
            "storage_types": storage_types,
            "asset_tank_ids": asset_tank_ids,
            "time_max": to_ISODate(time_max) if time_max else None,
            "time_min": to_ISODate(time_min) if time_min else None,
            "timeseries_frequency": timeseries_frequency,
            "timeseries_split_property": timeseries_split_property,
            "timeseries_unit": timeseries_unit,
            "timeseries_unit_operator": timeseries_unit_operator,
            "exclude": exclude_params,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return TimeSeriesResult(
            records=response["data"], ref=response["reference"]
        )
