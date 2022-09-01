from dataclasses import dataclass
from typing import Any, List, Optional, Union
from vortexasdk.api.id import ID

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import Entity, Flag, ISODate, Scrubber, Tag


@dataclass(frozen=True)
class CongestionBreakdownItem(FromDictMixin):
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
    location_details: List[Entity]


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
    imo: Optional[int]
    mmsi: Optional[int]
    call_sign: Optional[str]
    cubic_capacity: Optional[int]
    year: Optional[int]
    flag: List[Flag]
    scrubber: List[Scrubber]
    ice_class: Optional[str]
    propulsion: Optional[str]
    tags: List[Tag]
    vessel_risk_level: Optional[str]


@dataclass(frozen=True)
class VoyageVesselEvent:
    """
    A vessel event represents an activity that a vessel has performed during a voyage

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """
    event_id: str
    start_timestamp: Optional[ISODate]
    end_timestamp: Optional[ISODate]
    event_group: str
    event_type: str
    activity: Optional[str]
    odometer_start: Optional[int]
    odometer_end: Optional[int]
    location_id: str
    location_layer: List[str]
    cargo_movement_id: Optional[List[str]]
    sts_event_counterparty_vessel_id: Optional[str]
    waiting_event_target_geography_id: Optional[str]
    fixture_event_fixing_timestamp: Optional[ISODate]
    tags: List[Tag]
    probability: Optional[int]
    location_details: List[Entity]
    waiting_event_target_geography_details: Optional[List[Entity]]


@dataclass(frozen=True)
class VoyageCargoEvent:
    """
    Cargo events relate to the movement of cargo during the voyage.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """
    event_id: str
    start_timestamp: Optional[ISODate]
    end_timestamp: Optional[ISODate]
    event_group: str
    event_type: str
    activity: None
    odometer_start: Optional[int]
    odometer_end: Optional[int]
    cargo_movement_id: str
    cargo_origin_id: str
    cargo_destination_id: Optional[str]
    product_id: str
    quantity_tonnes: int
    quantity_barrels: int
    quantity_cubic_metres: int
    tonne_miles: Optional[int]
    product_details: List[Entity]
    cargo_origin_details: List[Entity]
    cargo_destination_details: List[Entity]


@dataclass(frozen=True)
class VoyageStatusEvent:
    """
    Status events describe the status of the voyage at a given period.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """
    event_id: str
    start_timestamp: Optional[ISODate]
    end_timestamp: Optional[ISODate]
    event_group: str
    event_type: str
    activity: str
    value: str
    source_event_id: str


@dataclass(frozen=True)
class VoyageEnrichedItem(FromDictMixin):
    """

    A voyage is defined as a continuous period of time when the vessel is either laden or ballast.

    Each voyage is made up of multiple voyage events which describe the activity of the vessel while it is laden or ballast.

    [Voyages Further Documentation](https://docs.vortexa.com/reference/intro-voyages)

    """

    schema_version: str
    voyage_id: ID
    start_timestamp: Optional[ISODate]
    end_timestamp: Optional[ISODate]
    start_event_id: ID
    end_event_id: Optional[ID]
    vessel_id: ID
    previous_voyage_id: Optional[ID]
    next_voyage_id: Optional[ID]
    latest_product_ids: List[ID]
    tags: List[Tag]
    tonne_miles: Optional[int]
    vessel: VoyagesVesselEntity
    corporate_entities: List[Entity]
    odometer_start: Optional[int]
    odometer_end: Optional[int]
    events: List[Optional[Union[VoyageStatusEvent, VoyageVesselEvent, VoyageCargoEvent]]]
    latest_product_details: List[Entity]
