"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fvoyages_search.ipynb)
"""
from datetime import datetime
from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import Tag, to_ISODate
from vortexasdk.endpoints.endpoints import VOYAGES_SEARCH
from vortexasdk.endpoints.voyages_search_result import VoyagesSearchResult

from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class VoyagesSearch(Search):
    """
    Please note: you will require a subscription to our Freight module to access this endpoint.
    """

    _MAX_PAGE_RESULT_SIZE = 500
    _HEADERS = {"Content-Type": "application/json", "accept": "text/csv"}

    def __init__(self):
        Search.__init__(self, VOYAGES_SEARCH)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        order: str = None,
        order_direction: str = None,
        offset: int = None,
        unit: str = None,
        csv_columns: Union[str, List[str]] = "all",

        time_min: datetime = datetime(2022, 1, 1, 0),
        time_max: datetime = datetime(2022, 1, 1, 1),
        voyage_id: Union[ID, List[ID]] = None,
        cargo_movement_id: Union[ID, List[ID]] = None,
        voyage_status: Union[str, List[str]] = None,
        voyage_status_excluded: Union[str, List[str]] = None,
        movement_status: Union[str, List[str]] = None,
        movement_status_excluded: Union[str, List[str]] = None,
        cargo_status: Union[str, List[str]] = None,
        cargo_status_excluded: Union[str, List[str]] = None,
        location_status: Union[str, List[str]] = None,
        location_status_excluded: Union[str, List[str]] = None,
        commitment_status: Union[str, List[str]] = None,
        commitment_status_excluded: Union[str, List[str]] = None,
        origin_behaviour: str = None,
        destination_behaviour: str = None,
        exclude_overlapping_entries: bool = None,
        products: Union[ID, List[ID]] = None,
        products_excluded: Union[ID, List[ID]] = None,
        latest_products: Union[ID, List[ID]] = None,
        latest_products_excluded: Union[ID, List[ID]] = None,
        charterers: Union[ID, List[ID]] = None,
        charterers_excluded: Union[ID, List[ID]] = None,
        vessel_owners: Union[ID, List[ID]] = None,
        vessel_owners_excluded: Union[ID, List[ID]] = None,
        origins: Union[ID, List[ID]] = None,
        origins_excluded: Union[ID, List[ID]] = None,
        destinations: Union[ID, List[ID]] = None,
        destinations_excluded: Union[ID, List[ID]] = None,
        locations: Union[ID, List[ID]] = None,
        locations_excluded: Union[ID, List[ID]] = None,
        vessels: Union[ID, List[ID]] = None,
        vessels_excluded: Union[ID, List[ID]] = None,
        flags: Union[ID, List[ID]] = None,
        flags_excluded: Union[ID, List[ID]] = None,
        ice_class: Union[ID, List[ID]] = None,
        ice_class_excluded: Union[ID, List[ID]] = None,
        vessel_propulsion: Union[ID, List[ID]] = None,
        vessel_propulsion_excluded: Union[ID, List[ID]] = None,
        vessel_age_min: int = None,
        vessel_age_max: int = None,
        vessel_dwt_min: int = None,
        vessel_dwt_max: int = None,
        vessel_wait_time_min: int = None,
        vessel_wait_time_max: int = None,
        vessel_scrubbers: str = None,
        vessels_tags: Union[Tag, List[Tag]] = None,
        vessels_tags_excluded: Union[Tag, List[Tag]] = None,
        vessel_risk_level: Union[str, List[str]] = None,
        vessel_risk_level_excluded: Union[str, List[str]] = None,
        has_ship_to_ship: bool = None,
        has_charterer: bool = None
    ) -> VoyagesSearchResult:
        """

        Returns voyages aggregation for the selected property and frequency.


        # Arguments
            breakdown_unit_operator: An array of owner ID(s) to filter on.
            breakdown_frequency: An array of confidence metrics to filter on. Possible values are: `'confirmed’`, `‘probable’`, `‘unlikely’`
            breakdown_property: Property to aggregate upon. Must be one of the following: `'b'`, `'t'`, `'cbm'`, `'bpd'`, `'tpd'`, `'mpd'`.
            breakdown_split_property: An array of storage types to filter on. Possible values are: `'refinery'`, `'non-refinery'`, `'commercial'`, `'spr'`, `'tbd'`
            time_min: The UTC start date of the time filter.
            time_max: The UTC end date of the time filter.
            voyage_id: An array of unique Asset Tanks ID(s) to filter on - linked to the Asset Tank Reference data.
            cargo_movement_id: Frequency denoting the granularity of the time series. Must be one of the following: `'week'`, `'month'`, `'year'`.
            voyage_status:
            voyage_status_excluded: 
            movement_status: 
            movement_status_excluded: 
            cargo_status: 
            cargo_status_excluded: 
            location_status: 
            location_status_excluded: 
            commitment_status: 
            commitment_status_excluded: 
            origin_behaviour:
            destination_behaviour:
            exclude_overlapping_entries:
            products: 
            products_excluded: 
            latest_products: 
            latest_products_excluded: 
            charterers: 
            charterers_excluded: 
            vessel_owners: 
            vessel_owners_excluded: 
            origins: 
            origins_excluded: 
            destinations: 
            destinations_excluded: 
            locations: 
            locations_excluded: 
            vessels: 
            vessels_excluded: 
            flags: 
            flags_excluded: 
            ice_class: 
            ice_class_excluded: 
            vessel_propulsion: 
            vessel_propulsion_excluded: 
            vessel_age_min: 
            vessel_age_max: 
            vessel_dwt_min: 
            vessel_dwt_max: 
            vessel_wait_time_min: 
            vessel_wait_time_max: 
            vessel_scrubbers:
            vessels_tags:
            vessels_tags_excluded:
            vessel_risk_level: 
            vessel_risk_level_excluded: 
            has_ship_to_ship: 
            has_charterer: 

        # Returns
        `BreakdownResult`

        # Example
        _Total storage capacity across Europe for the first week of January 2021._

        ```python
        >>> from vortexasdk import VoyagesTimeseries
        >>> from datetime import datetime
        >>> search_result = VoyagesTimeseries().search(
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
        api_params = {
            "voyage_id": convert_to_list(voyage_id),
            "cargo_movement_id": convert_to_list(cargo_movement_id),
            "voyage_status": convert_to_list(voyage_status),
            "cargo_status": convert_to_list(cargo_status),
            "location_status": convert_to_list(location_status),
            "commitment_status": convert_to_list(commitment_status),
            "movement_status": convert_to_list(movement_status),
            "origin_behaviour": origin_behaviour,
            "destination_behaviour": destination_behaviour,
            "products": convert_to_list(products),
            "latest_products": convert_to_list(latest_products),
            "charterers": convert_to_list(charterers),
            "vessel_owners": convert_to_list(vessel_owners),
            "origins": convert_to_list(origins),
            "destinations": convert_to_list(destinations),
            "locations": convert_to_list(locations),
            "flags": convert_to_list(flags),
            "ice_class": convert_to_list(ice_class),
            "vessel_propulsion": convert_to_list(vessel_propulsion),
            "vessels": convert_to_list(vessels),
            "vessels_tags": convert_to_list(vessels_tags),
            "vessel_risk_level": convert_to_list(vessel_risk_level),
            "vessel_age_min": vessel_age_min,
            "vessel_age_max": vessel_age_max,
            "vessel_dwt_min": vessel_dwt_min,
            "vessel_dwt_max": vessel_dwt_max,
            "vessel_wait_time_min": vessel_wait_time_min,
            "vessel_wait_time_max": vessel_wait_time_max,
            "vessel_scrubbers": vessel_scrubbers,
            "has_charterer": has_charterer,
            "has_ship_to_ship": has_ship_to_ship,
            "exclude_overlapping_entries": exclude_overlapping_entries,
            "time_max": to_ISODate(time_max) if time_max else None,
            "time_min": to_ISODate(time_min) if time_min else None,
            "order_direction": order_direction,
            "order": order,
            "offset": offset,
            "size": self._MAX_PAGE_RESULT_SIZE,
            "unit": unit,
            "csv_columns": csv_columns,
            "voyage_status_excluded": convert_to_list(voyage_status_excluded),
            "cargo_status_excluded": convert_to_list(cargo_status_excluded),
            "location_status_excluded": convert_to_list(location_status_excluded),
            "commitment_status_excluded": convert_to_list(commitment_status_excluded),
            "movement_status_excluded": convert_to_list(movement_status_excluded),
            "products_excluded": convert_to_list(products_excluded),
            "latest_products_excluded": convert_to_list(latest_products_excluded),
            "charterers_excluded": convert_to_list(charterers_excluded),
            "vessel_owners_excluded": convert_to_list(vessel_owners_excluded),
            "origins_excluded": convert_to_list(origins_excluded),
            "destinations_excluded": convert_to_list(destinations_excluded),
            "locations_excluded": convert_to_list(locations_excluded),
            "flags_excluded": convert_to_list(flags_excluded),
            "ice_class_excluded": convert_to_list(ice_class_excluded),
            "vessel_propulsion_excluded": convert_to_list(vessel_propulsion_excluded),
            "vessels_excluded": convert_to_list(vessels_excluded),
            "vessels_tags_excluded": convert_to_list(vessels_tags_excluded),
            "vessel_risk_level_excluded": convert_to_list(vessel_risk_level_excluded),
        }

        return VoyagesSearchResult(super().search(headers=self._HEADERS, **api_params))
