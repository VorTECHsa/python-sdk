"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fvoyages_top_hits.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import (
    Tag,
    to_ISODate,
    VoyageDateRangeActivity,
    OriginBehaviour,
    DestinationBehaviour,
)
from vortexasdk.endpoints.aggregation_breakdown_result import (
    AggregationBreakdownResult,
)
from vortexasdk.endpoints.endpoints import VOYAGES_TOP_HITS

from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class VoyagesTopHits(Search):
    """
    Please note: you will require a subscription to our Freight module to access this endpoint.
    """

    def __init__(self):
        Search.__init__(self, VOYAGES_TOP_HITS)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        breakdown_property: str = None,
        breakdown_split_property: str = None,
        breakdown_size: int = None,
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
        exclude_overlapping_entries: bool = None,
        products: Union[ID, List[ID]] = None,
        products_excluded: Union[ID, List[ID]] = None,
        latest_products: Union[ID, List[ID]] = None,
        latest_products_excluded: Union[ID, List[ID]] = None,
        charterers: Union[ID, List[ID]] = None,
        charterers_excluded: Union[ID, List[ID]] = None,
        effective_controllers: Union[ID, List[ID]] = None,
        effective_controllers_excluded: Union[ID, List[ID]] = None,
        origins: Union[ID, List[ID]] = None,
        origins_excluded: Union[ID, List[ID]] = None,
        destinations: Union[ID, List[ID]] = None,
        destinations_excluded: Union[ID, List[ID]] = None,
        locations: Union[ID, List[ID]] = None,
        locations_excluded: Union[ID, List[ID]] = None,
        congestion_target_location: Union[str, List[str]] = None,
        congestion_target_location_excluded: Union[str, List[str]] = None,
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
        vessel_cbm_min: int = None,
        vessel_cbm_max: int = None,
        vessel_wait_time_min: int = None,
        vessel_wait_time_max: int = None,
        vessel_scrubbers: str = None,
        vessel_tags: Union[Tag, List[Tag]] = None,
        vessel_tags_excluded: Union[Tag, List[Tag]] = None,
        vessel_risk_level: Union[str, List[str]] = None,
        vessel_risk_level_excluded: Union[str, List[str]] = None,
        has_ship_to_ship: str = None,
        has_charterer: str = None,
        intra_movements: str = None,
        voyage_date_range_activity: VoyageDateRangeActivity = None,
        origin_behaviour: OriginBehaviour = None,
        destination_behaviour: DestinationBehaviour = None,
    ) -> AggregationBreakdownResult:
        """

        Returns a count of voyages aggregated by a chosen `breakdown_property`.


        # Arguments
            breakdown_size: Number of top records to return.

            breakdown_property: Property to aggregate upon. Must be `vessel_count` or not provided.

            breakdown_split_property: Property to split results by. Can be one of: `'vessel_status'`, `'vessel_class_group'`, `'vessel_class_coarse'`, `'vessel_class_granular'`, `'vessel_flag'`,`'fixture_status'`, `'origin_region'`,
            `'origin_shipping_region'`,`'origin_trading_region'`,`'origin_trading_sub_region'`,`'origin_trading_block'`,`'origin_country'`,`'origin_port'`,
            `'origin_terminal'`,`'destination_region'`,`'destination_shipping_region'`,`'destination_trading_region'`,`'destination_trading_sub_region'`,`'destination_trading_block'`,
            `'destination_country'`,`'destination_port'`,`'destination_terminal'`,`'location_port'`,`'location_country'`,`'location_shipping_region'`,
            `'congestion_location_port'`,`'congestion_location_country'`,`'congestion_location_shipping_region'`,`'product_group'`,`'product_group_product'`,`'product_category'`, `'product_grade'`.

            time_min: The UTC start date of the time filter.

            time_max: The UTC end date of the time filter.

            voyage_id: An array of unique voyage ID(s) to filter on.

            cargo_movement_id: An array of unique cargo movement ID(s) to filter on.

            voyage_status: A voyage status, or list of voyage statuses to filter on. Can be one of: `'ballast'`, `'laden'`.

            voyage_status_excluded: A voyage status, or list of voyage statuses to exclude.

            movement_status: A movement status, or list of movement statuses to filter on. Can be one of: `'moving'`, `'stationary'`, `'waiting'`, `'congestion'`, `'slow'`.

            movement_status_excluded: A movement status, or list of movement statuses to exclude.

            cargo_status: A cargo status, or list of cargo statuses to filter on. Can be one of: `'in-transit'`, `'floating-storage'`, `'loading'`, `'discharging'`.

            cargo_status_excluded: A cargo status, or list of cargo statuses to exclude.

            location_status: A location status, or list of location statuses to filter on. Can be one of: `'berth'`, `'anchorage-zone'`, `'dry-dock'`, `'on-the-sea'`.

            location_status_excluded: A location status, or list of location statuses to exclude.

            commitment_status: A commitment status, or list of commitment statuses to filter on. Can be one of: `'committed'`, `'uncommitted'`, `'open'`, `'unknown'`.

            commitment_status_excluded: A commitment status, or list of commitment statuses to exclude.

            exclude_overlapping_entries: A boolean to only consider the latest voyage in days where two or more Voyages overlap.

            products: A product ID, or list of product IDs to filter on.

            products_excluded: A product ID, or list of product IDs to exclude.

            latest_products: A product ID, or list of product IDs of the latest cargo on board to filter on.

            latest_products_excluded: A product ID, or list of product IDs of the latest cargo on board to exclude.

            charterers: A charterer ID, or list of charterer IDs to filter on.

            charterers_excluded: A charterer ID, or list of charterer IDs to exclude.

            effective_controllers: A vessel effective controller ID, or list of vessel effective controller IDs to filter on.

            effective_controllers_excluded: A vessel effective controller ID, or list of vessel effective controller IDs to exclude.

            origins: An origin ID, or list of origin IDs for all the cargoes of a voyage to filter on.

            origins_excluded: An origin ID, or list of origin IDs for all the cargoes of a voyage to exclude.

            destinations: A destination ID, or list of destination IDs for all the cargoes of a voyage to filter on.

            destinations_excluded: A destination ID, or list of destination IDs for all the cargoes of a voyage to exclude.

            locations: A location ID, or list of location IDs to filter on.

            locations_excluded: A location ID, or list of location IDs to exclude.

            congestion_target_location: A congestion location ID, or list of congestion location IDs to filter on.

            congestion_target_location_excluded: A congestion location ID, or list of congestion location IDs to exclude.

            vessels: A vessel ID or vessel class, or list of vessel IDs/vessel classes to filter on.

            vessels_excluded: A vessel ID or vessel class, or list of vessel IDs/vessel classes to exclude.

            flags: A flag, or list of flags to filter on.

            flags_excluded: A flag, or list of flags to exclude.

            ice_class: An ice class, or list of ice classes to filter on.

            ice_class_excluded: An ice class, or list of ice classes to ęxclude.

            vessel_propulsion: A propulsion method, or list of propulsion methods to filter on.

            vessel_propulsion_excluded: A propulsion method, or list of propulsion methods to ęxclude.

            vessel_age_min: A number between 1 and 100 (representing years).

            vessel_age_max: A number between 1 and 100 (representing years).

            vessel_dwt_min: A number representing minimum deadweight tonnage of a vessel.

            vessel_dwt_max: A number representing maximum deadweight tonnage of a vessel.

            vessel_cbm_min: A number representing minimum cubic capacity of a vessel.

            vessel_cbm_max: A number representing maximum cubic capacity of a vessel.

            vessel_wait_time_min: A number representing a minimum number of days until a vessel becomes available.

            vessel_wait_time_max: A number representing a maximum number of days until a vessel becomes available.

            vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

            vessel_tags: A time bound vessel tag, or list of time bound vessel tags to filter on.

            vessel_tags_excluded: A time bound vessel tag, or list of time bound vessel tags to exclude.

            vessel_risk_level: A vessel risk level, or list of vessel risk levels to filter on.

            vessel_risk_level_excluded: A vessel risk level, or list of vessel risk levels to exclude.

            has_ship_to_ship: Filter data where at least one STS transfer occurs, or none. - one of: `'disabled'`, `'inc'`, `'exc'`. Passing disabled means the filter is not active.

            has_charterer: Filter data where at least one charterer is specified, or none. - one of: `'disabled'`, `'inc'`, `'exc'`. Passing disabled means the filter is not active.

            intra_movements: Filter movements based on whether the vessel started and ended in the same country, or geographical layer.

            voyage_date_range_activity: Filter to determine how the voyages should be counted. Must be one of [`active`, `departures`, `arrivals`]

            origin_behaviour: The origin behaviour determines which departure mode the `voyage_date_range_activity` should count, must be one of  [`first_load`, `any_load`].

            destination_behaviour: The destination behaviour determines which arrival mode the voyage_date_range_activity should count, must be one of [last_discharge, any_discharge].

        # Returns
        `AggregationBreakdownResult`

        # Example
        _Top oritin countries for crude imports to Rotterdam on 8th August 2021._

        ```python
        >>> from vortexasdk import VoyagesTopHits, Geographies, Products
        >>> from datetime import datetime
        >>> rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        >>> crude = [p.id for p in Products().search("crude").to_list() if "Crude" == p.name]
        >>> start = datetime(2021, 8, 1)
        >>> end = datetime(2021, 8, 1, 23, 59)
        >>> search_result = VoyagesTopHits().search(
        ...    time_min=start,
        ...    time_max=end,
        ...    destinations=rotterdam,
        ...    products=crude,
        ...    breakdown_size=5,
        ...    breakdown_split_property="origin_country"
        ... ).to_list()

        ```
        Gives the following result:

        ```
        [
            AggregationBreakdownItem(
                id='b996521be9c996db',
                count=8,
                value=8.0,
                label='Russia'
            ),
            AggregationBreakdownItem(
                id='2d92cc08f22524db',
                count=7,
                value=7.0,
                label='United States'
            ),
            AggregationBreakdownItem(
                id='2aaad41b89dfad19',
                count=4,
                value=4.0,
                label='United Kingdom'
            ),
            AggregationBreakdownItem(
                id='430f0e467f3a408f',
                count=2,
                value=2.0,
                label='Nigeria'
            ),
            AggregationBreakdownItem(
                id='3eac69e760d9ec57',
                count=1,
                value=1.0,
                label='Egypt'
            )
        ]
        ```
        """
        api_params: Dict[str, Any] = {
            "voyage_id": convert_to_list(voyage_id),
            "cargo_movement_id": convert_to_list(cargo_movement_id),
            "voyage_status": convert_to_list(voyage_status),
            "cargo_status": convert_to_list(cargo_status),
            "location_status": convert_to_list(location_status),
            "commitment_status": convert_to_list(commitment_status),
            "movement_status": convert_to_list(movement_status),
            "products": convert_to_list(products),
            "latest_products": convert_to_list(latest_products),
            "charterers": convert_to_list(charterers),
            "effective_controllers": convert_to_list(effective_controllers),
            "origins": convert_to_list(origins),
            "destinations": convert_to_list(destinations),
            "locations": convert_to_list(locations),
            "congestion_target_location": convert_to_list(
                congestion_target_location
            ),
            "flags": convert_to_list(flags),
            "ice_class": convert_to_list(ice_class),
            "vessel_propulsion": convert_to_list(vessel_propulsion),
            "vessels": convert_to_list(vessels),
            "vessel_tags": convert_to_list(vessel_tags),
            "vessel_risk_level": convert_to_list(vessel_risk_level),
            "vessel_age_min": vessel_age_min,
            "vessel_age_max": vessel_age_max,
            "vessel_dwt_min": vessel_dwt_min,
            "vessel_dwt_max": vessel_dwt_max,
            "vessel_cbm_min": vessel_cbm_min,
            "vessel_cbm_max": vessel_cbm_max,
            "vessel_wait_time_min": vessel_wait_time_min,
            "vessel_wait_time_max": vessel_wait_time_max,
            "vessel_scrubbers": vessel_scrubbers,
            "has_charterer": has_charterer,
            "has_ship_to_ship": has_ship_to_ship,
            "exclude_overlapping_entries": exclude_overlapping_entries,
            "time_max": to_ISODate(time_max) if time_max else None,
            "time_min": to_ISODate(time_min) if time_min else None,
            "breakdown_property": breakdown_property,
            "breakdown_split_property": breakdown_split_property,
            "breakdown_size": breakdown_size,
            "voyage_status_excluded": convert_to_list(voyage_status_excluded),
            "cargo_status_excluded": convert_to_list(cargo_status_excluded),
            "location_status_excluded": convert_to_list(
                location_status_excluded
            ),
            "commitment_status_excluded": convert_to_list(
                commitment_status_excluded
            ),
            "movement_status_excluded": convert_to_list(
                movement_status_excluded
            ),
            "products_excluded": convert_to_list(products_excluded),
            "latest_products_excluded": convert_to_list(
                latest_products_excluded
            ),
            "charterers_excluded": convert_to_list(charterers_excluded),
            "effective_controllers_excluded": convert_to_list(
                effective_controllers_excluded
            ),
            "origins_excluded": convert_to_list(origins_excluded),
            "destinations_excluded": convert_to_list(destinations_excluded),
            "locations_excluded": convert_to_list(locations_excluded),
            "congestion_target_location_excluded": convert_to_list(
                congestion_target_location_excluded
            ),
            "flags_excluded": convert_to_list(flags_excluded),
            "ice_class_excluded": convert_to_list(ice_class_excluded),
            "vessel_propulsion_excluded": convert_to_list(
                vessel_propulsion_excluded
            ),
            "vessels_excluded": convert_to_list(vessels_excluded),
            "vessel_tags_excluded": convert_to_list(vessel_tags_excluded),
            "vessel_risk_level_excluded": convert_to_list(
                vessel_risk_level_excluded
            ),
            "voyage_date_range_activity": voyage_date_range_activity,
            "origin_behaviour": origin_behaviour,
            "destination_behaviour": destination_behaviour,
            "intra_movements": intra_movements,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return AggregationBreakdownResult(
            records=response["data"], reference=response["reference"]
        )
