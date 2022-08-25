from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

from vortexasdk.api.id import ID

from vortexasdk.api.shared_types import (
    IDName,
    ISODate,
    Node,
    Tag,
    Scrubber,
    Flag,
)


class VesselEntityCorporateEntity(BaseModel):
    id: ID
    label: str
    layer: str
    end_timestamp: Optional[datetime] = None
    start_timestamp: Optional[datetime] = None


class VesselEntityCorporateEntityWithConfidence(BaseModel):
    probability: float
    source: str
    id: ID
    label: str
    layer: str
    end_timestamp: Optional[datetime] = None
    start_timestamp: Optional[datetime] = None


class Vessel(Node, BaseModel):
    """
    Represent a Vessel reference record returned by the API.

    [Vessels Further Documentation](https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D)
    """

    related_names: List[str]
    mmsi: int
    layer: List[str]

    tags: List[Tag]
    current_product_type: List

    vessel_class: str
    vessel_status: str

    corporate_entities: Optional[List[VesselEntityCorporateEntity]] = None
    dead_weight: Optional[int] = None
    cubic_capacity: Optional[int] = None
    to_bow: Optional[str] = None
    to_stern: Optional[str] = None
    to_port: Optional[str] = None
    to_starboard: Optional[str] = None
    call_sign: Optional[str] = None
    year: Optional[int] = None
    imo: Optional[int] = None
    gross_tonnage: Optional[int] = None

    scrubber: Optional[List[Scrubber]] = None
    flag: Optional[List[Flag]] = None
    ice_class: Optional[str] = None
    propulsion: Optional[str] = None


class VesselEntity(IDName, BaseModel):
    """
    A VesselEntity represents a vessel record used in CargoMovements and VesselMovements.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: str
    mmsi: int
    imo: Optional[int]

    dwt: int

    vessel_class: str
    corporate_entities: List[VesselEntityCorporateEntityWithConfidence]
    tags: List[Tag]
    status: str
    year: Optional[int] = None

    start_timestamp: Optional[ISODate] = None

    cubic_capacity: Optional[int] = None
    voyage_id: Optional[str] = None
    fixture_fulfilled: Optional[bool] = None
    end_timestamp: Optional[ISODate] = None
    fixture_id: Optional[str] = None

    scrubber: List[Scrubber] = Field(default_factory=list)
    flag: List[Flag] = Field(default_factory=list)
    ice_class: Optional[str] = None
    propulsion: Optional[str] = None
