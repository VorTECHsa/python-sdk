from dataclasses import dataclass
from typing import List, Optional
from vortexasdk.api.id import ID

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import Flag, ISODate, Scrubber, Tag


@dataclass(frozen=True)
class ReferenceEntry:
    """
    """
    id: str
    label: str
    layer: str


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
    location_details: List[ReferenceEntry]


@dataclass(frozen=True)
class VoyagesVesselEntity(FromDictMixin):
    """
    A VoyagesVesselEntity represents a vessel record used in Voyages.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: str
    imo: Optional[int]
    mmsi: int
    call_sign: str
    cubic_capacity: int
    dead_weight: int
    vessel_class: str
    year: Optional[int]
    flag: List[Flag]
    scrubber: List[Scrubber]
    ice_class: Optional[str]
    propulsion: Optional[str]
    tags: List[Tag]
    vessel_risk_level: Optional[str]


@dataclass(frozen=True)
class VoyageEnrichedEvent(FromDictMixin):
    """
    A voyage event represents an action / event that occurred during a voyage. It allows you to get a full picture of the sequence of activities.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """
    # shared event properties
    event_id: str
    start_timestamp: Optional[ISODate]
    end_timestamp: Optional[ISODate]
    event_group: str
    event_type: str
    event_activity: Optional[str]
    odometer_start: Optional[int]
    odometer_end: Optional[int]
    # vessel event properties
    location_id: Optional[str]
    location_layer: Optional[List[str]]
    cargo_movement_id: Optional[List[str]]
    sts_event_counterparty_vessel_id: Optional[str]
    waiting_event_target_geography_id: Optional[str]
    fixture_event_fixing_timestamp: Optional[ISODate]
    tags: Optional[List[Tag]]
    probability: Optional[int]
    location_details: Optional[List[ReferenceEntry]]
    waiting_event_target_geography_details: Optional[List[ReferenceEntry]]
    # cargo event properties
    cargo_movement_id: Optional[str]
    cargo_origin_id: Optional[str]
    cargo_destination_id: Optional[str]
    product_id: Optional[str]
    product_details: Optional[List[ReferenceEntry]]
    quantity_tonnes: Optional[int]
    quantity_barrels: Optional[int]
    quantity_cubic_metres: Optional[int]
    tonne_miles: Optional[int]
    cargo_origin_details: Optional[List[ReferenceEntry]]
    cargo_destination_details: Optional[List[ReferenceEntry]]
    # status event properties
    value: Optional[str]
    source_event_id: Optional[str]


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
    corporate_entities: List[ReferenceEntry]
    odometer_start: Optional[int]
    odometer_end: Optional[int]
    events: List[VoyageEnrichedEvent]
    latest_product_details: List[ReferenceEntry]
