from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from typing_extensions import Literal
from vortexasdk.api.id import ID
from dataclasses import field

from vortexasdk.api.shared_types import (
    EntityWithListLayer,
    EntityWithSingleLayer,
    EntityWithSingleLayerAndTimespan,
    Flag,
    ISODate,
    Scrubber,
    Tag,
)


@dataclass(frozen=True)
class CongestionBreakdownItem:
    """

    Congestion breakdown shows various stats of vessels in congestion.

    """

    avg_waiting_time: int
    vessel_dwt: int
    vessel_cubic_capacity: int
    vessel_count: int
    cargo_quantity: int
    avg_waiting_time_laden: int
    vessel_dwt_laden: int
    vessel_cubic_capacity_laden: int
    vessel_count_laden: int
    avg_waiting_time_ballast: int
    vessel_dwt_ballast: int
    vessel_cubic_capacity_ballast: int
    vessel_count_ballast: int
    location_details: List[EntityWithListLayer] = field(default_factory=list)


@dataclass(frozen=True)
class VoyagesVesselEntity:
    """
    A VoyagesVesselEntity represents a vessel record used in Voyages.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: str
    dead_weight: int
    vessel_class: str
    imo: Optional[int] = None
    mmsi: Optional[int] = None
    call_sign: Optional[str] = None
    cubic_capacity: Optional[int] = None
    year: Optional[int] = None
    flag: List[Flag] = field(default_factory=list)
    scrubber: List[Scrubber] = field(default_factory=list)
    ice_class: Optional[str] = None
    propulsion: Optional[str] = None
    tags: List[Tag] = field(default_factory=list)
    vessel_risk_level: Optional[str] = None


@dataclass(frozen=True)
class VoyageVesselEvent:
    """
    A vessel event represents an activity that a vessel has performed during a voyage

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """

    event_id: str
    event_group: str
    event_type: str
    location_id: str
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
    activity: Optional[str] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    location_layer: List[str] = field(default_factory=list)
    cargo_movement_id: Optional[List[str]] = None
    sts_event_counterparty_vessel_id: Optional[str] = None
    waiting_event_target_geography_id: Optional[str] = None
    fixture_event_fixing_timestamp: Optional[ISODate] = None
    tags: List[Tag] = field(default_factory=list)
    probability: Optional[int] = None
    location_details: List[EntityWithSingleLayer] = field(default_factory=list)
    is_open_event: Optional[bool] = None
    waiting_event_target_geography_details: Optional[
        List[EntityWithSingleLayer]
    ] = None


@dataclass(frozen=True)
class VoyageCargoEvent:
    """
    Cargo events relate to the movement of cargo during the voyage.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """

    event_id: str
    event_group: Literal["derived"]
    event_type: str
    cargo_movement_id: str
    cargo_origin_id: str
    product_id: str
    quantity_tonnes: int
    quantity_barrels: int
    quantity_cubic_metres: int
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
    activity: Optional[str] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    cargo_destination_id: Optional[str] = None
    tonne_miles: Optional[int] = None
    product_details: List[EntityWithSingleLayer] = field(default_factory=list)
    cargo_origin_details: List[EntityWithSingleLayer] = field(
        default_factory=list
    )
    cargo_destination_details: List[EntityWithSingleLayer] = field(
        default_factory=list
    )
    is_open_event: Optional[bool] = None


@dataclass(frozen=True)
class VoyageStatusEvent:
    """
    Status events describe the status of the voyage at a given period.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """

    event_id: str
    event_group: Literal["derived"]
    event_type: str
    activity: str
    value: str
    source_event_id: str
    end_timestamp: Optional[ISODate] = None
    start_timestamp: Optional[ISODate] = None
    is_open_event: Optional[bool] = None


@dataclass(frozen=True)
class VoyageEnrichedItem:
    """

    A voyage is defined as a continuous period of time when the vessel is either laden or ballast.

    Each voyage is made up of multiple voyage events which describe the activity of the vessel while it is laden or ballast.

    [Voyages Further Documentation](https://docs.vortexa.com/reference/intro-voyages)

    """

    schema_version: str
    voyage_id: ID
    start_event_id: ID
    vessel_id: ID
    vessel: VoyagesVesselEntity
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
    end_event_id: Optional[ID] = None
    previous_voyage_id: Optional[ID] = None
    next_voyage_id: Optional[ID] = None
    latest_product_ids: List[ID] = field(default_factory=list)
    tags: List[Tag] = field(default_factory=list)
    tonne_miles: Optional[int] = None
    corporate_entities: List[EntityWithSingleLayerAndTimespan] = field(
        default_factory=list
    )
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    events: List[
        Optional[Union[VoyageVesselEvent, VoyageCargoEvent, VoyageStatusEvent]]
    ] = field(default_factory=list)
    latest_product_details: List[EntityWithSingleLayer] = field(
        default_factory=list
    )
