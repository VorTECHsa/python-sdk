"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fvoyages_product_breakdown.ipynb)
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

from vortexasdk.endpoints.endpoints import VOYAGES_BREAKDOWN
from vortexasdk.endpoints.voyages_breakdown_result import (
    VoyagesBreakdownResult,
)

from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

# noinspection PyUnresolvedReferences


class VoyagesProductBreakdown(Search):
    """
    VoyagesProductBreakdown class has an optional _second_breakdown_ property.

    Please note: you will require a subscription to our Freight module to access this endpoint.

    # Arguments

        second_breakdown: An optional second breakdown property. Can be: `'status'`.
    """

    def __init__(
        self,
        second_breakdown: str = None,  # path parameter
    ):
        product_property = "product"

        if second_breakdown:
            endpoint = (
                f"{VOYAGES_BREAKDOWN}/{product_property}/{second_breakdown}"
            )
        else:
            endpoint = f"{VOYAGES_BREAKDOWN}/{product_property}"

        Search.__init__(self, endpoint)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        breakdown_product: str,
        breakdown_size: int = None,
        time_min: datetime = datetime(2024, 1, 1, 0),
        time_max: datetime = datetime(2024, 3, 31, 1),
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
        voyage_origins: Union[ID, List[ID]] = None,
        voyage_origins_excluded: Union[ID, List[ID]] = None,
        voyage_destinations: Union[ID, List[ID]] = None,
        voyage_destinations_excluded: Union[ID, List[ID]] = None,
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
        has_ship_to_ship: bool = None,
        has_charterer: bool = None,
        vessel_owners: Union[ID, List[ID]] = None,
        vessel_owners_excluded: Union[ID, List[ID]] = None,
        time_charterer: Union[ID, List[ID]] = None,
        time_charterer_excluded: Union[ID, List[ID]] = None,
        intra_movements: str = None,
        voyage_date_range_activity: VoyageDateRangeActivity = None,
        origin_behaviour: OriginBehaviour = None,
        destination_behaviour: DestinationBehaviour = None,
    ) -> VoyagesBreakdownResult:
        """

        Returns buckets by frequency of specified metric, each bucket includes breakdown by specified breakdown_property of a metric.

        # Arguments

            breakdown_product: Determines the product layer of the breakdown.

            breakdown_size: Optional number of top hits to return.

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

            time_charterer: A time charterer ID, or list of time charterer IDs to filter on.

            time_charterer_excluded: A time charterer ID, or list of time charterer IDs to exclude.

            effective_controllers: A vessel effective controller ID, or list of vessel effective controller IDs to filter on.

            effective_controllers_excluded: A effective controller ID, or list of effective controller IDs to exclude.

            vessel_owners: A vessel owner ID, or list of vessel owners IDs to filter on.

            vessel_owners_excluded: A vessel owner ID, or list of vessel owners IDs to exclude.

            origins: An origin ID, or list of origin IDs for all the cargoes of a voyage to filter on.

            origins_excluded: An origin ID, or list of origin IDs for all the cargoes of a voyage to exclude.

            destinations: A destination ID, or list of destination IDs for all the cargoes of a voyage to filter on.

            destinations_excluded: A destination ID, or list of destination IDs for all the cargoes of a voyage to exclude.

            voyage_origins: An origin ID, or list of origin IDs for the first origin of voyage to filter on.

            voyage_origins_excluded: An origin ID, or list of origin IDs for the first origin of voyage to exclude.

            voyage_destinations: A destination ID, or list of destination IDs for the last destination of a voyage to filter on.

            voyage_destinations_excluded: A destination ID, or list of destination IDs for the final destination of a voyage to exclude.

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
        `BreakdownResult`

        # Example
        _Vessels breakdown by product and status between 1st of January 2024 - 29th of Fabuary 2024 with a "category" layer breakdown._

        ```python
        >>> from vortexasdk import VoyagesProductBreakdown
        >>> from datetime import datetime
        >>> search_result = VoyagesProductBreakdown(
        ...    second_breakdown="status",
        ... ).search(
        ...    time_min=datetime(2024, 1, 1),
        ...    time_max=datetime(2024, 2, 29, 23, 59),
        ...    breakdown_product="category",
        ...    origins=["c4b606ff15bd9b86c37e4fbccf8b5f7e57890c6f675e7a250538e297b4c1303e"],
        ... ).to_df()

        ```
        Gives the following result:

        ```
        |    | id               | label                           |   value | breakdown.0.id   | breakdown.0.label   | breakdown.0.value   | breakdown.1.id   | breakdown.1.label   | breakdown.1.value   |
        |---:|:-----------------|:--------------------------------|--------:|:-----------------|:--------------------|:--------------------|:-----------------|:--------------------|:--------------------|
        |  0 | 903edb3eea470524 | Chemicals                       |      23 | ballast          | ballast             | 1                   | laden            | laden               | 22                  |
        |  1 | 9d52ede1cff0421a | Biodiesel Feedstock             |      22 | ballast          | ballast             | 1                   | laden            | laden               | 20                  |
        |  2 | 46c5395c665a4dc1 | Other Biodiesel/ Edible Oils    |       5 | ballast          | ballast             | 1                   | laden            | laden               | 4                   |
        |  3 | b2034f1ad3a4ac26 | Gasoil                          |       4 | ballast          | ballast             | 3                   | laden            | laden               | 1                   |
        |  4 | 3c227f964d804a12 | ULSD (Ultra Low Sulphur Diesel) |       3 | ballast          | ballast             | 3                   | laden            | laden               |                     |
        |  5 | 1854369f995f26cb | Blending Components             |       1 | ballast          | ballast             |                     | laden            | laden               | 1                   |
        |  6 | c76d43ed46524d62 | Finished Gasoline               |       1 | ballast          | ballast             |                     | laden            | laden               | 1                   |
        ```
        """
        api_params: Dict[str, Any] = {
            "breakdown_product": breakdown_product,
            "breakdown_size": breakdown_size,
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
            "time_charterer": convert_to_list(time_charterer),
            "effective_controllers": convert_to_list(effective_controllers),
            "vessel_owners": convert_to_list(vessel_owners),
            "origins": convert_to_list(origins),
            "destinations": convert_to_list(destinations),
            "voyage_origins": convert_to_list(voyage_origins),
            "voyage_destinations": convert_to_list(voyage_destinations),
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
            "intra_movements": intra_movements,
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
            "time_charterer_excluded": convert_to_list(
                time_charterer_excluded
            ),
            "effective_controllers_excluded": convert_to_list(
                effective_controllers_excluded
            ),
            "vessel_owners_excluded": convert_to_list(vessel_owners_excluded),
            "origins_excluded": convert_to_list(origins_excluded),
            "destinations_excluded": convert_to_list(destinations_excluded),
            "voyage_origins_excluded": convert_to_list(
                voyage_origins_excluded
            ),
            "voyage_destinations_excluded": convert_to_list(
                voyage_destinations_excluded
            ),
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
        }

        response = super().search_with_client(**api_params)

        return VoyagesBreakdownResult(
            records=response["data"], reference=response["reference"]
        )
