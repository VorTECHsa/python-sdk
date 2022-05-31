from dataclasses import dataclass
from enum import Flag
from typing import List, Optional
from vortexasdk.api.corporation import CorporateEntity
from vortexasdk.api.id import ID

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import ISODate, Scrubber, Tag


@dataclass(frozen=True)
class LocationDetails:
    """
    """
    id: str
    label: str
    layer: List[str]


@dataclass(frozen=True)
class ProductDetails:
    """
    """
    id: str
    label: str
    layer: List[str]


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
    location_details: List[LocationDetails]


@dataclass(frozen=True)
class VoyagesVesselEntity():
    """
    A VoyagesVesselEntity represents a vessel record used in Voyages.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: str
    imo: int
    mmsi: int
    call_sign: str
    cubic_capacity: int
    dead_weight: int
    vessel_class: str
    year: int
    flag: List[Flag]
    scrubber: List[Scrubber]
    ice_class: str
    propulsion: str
    tags: List[Tag]
    vessel_risk_level: Optional[str]


@dataclass(frozen=True)
class VoyageEnrichedEvent():
    """
    A voyage event represents an action / event that occurred during a voyage. It allows you to get a full picture of the sequence of activities.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """


@dataclass(frozen=True)
class VoyageEnrichedItem(FromDictMixin):
    """

    A voyage is defined as a continuous period of time when the vessel is either laden or ballast.

    Each voyage is made up of multiple voyage events which describe the activity of the vessel while it is laden or ballast.

    [Voyages Further Documentation](https://docs.vortexa.com/reference/intro-voyages)

    """

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
    odometer_start: Optional[int]
    odometer_end: Optional[int]
    corporate_entities: List[CorporateEntity]
    events: List[VoyageEnrichedEvent]
    latest_product_details: List[ProductDetails]
