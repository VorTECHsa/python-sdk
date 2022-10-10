from pydantic import BaseModel
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
    label: Optional[str] = None
    layer: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    start_timestamp: Optional[ISODate] = None


class VesselEntityCorporateEntityWithConfidence(BaseModel):
    probability: Optional[float] = None
    source: Optional[str] = None
    id: Optional[ID] = None
    label: Optional[str] = None
    layer: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    start_timestamp: Optional[ISODate] = None


class Vessel(Node):
    """
    Represent a Vessel reference record returned by the API.

    [Vessels Further Documentation](https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D)
    """

    related_names: Optional[List[str]] = None
    mmsi: Optional[int] = None
    layer: Optional[List[str]] = None

    tags: Optional[List[Tag]] = None
    current_product_type: Optional[List] = None

    vessel_class: Optional[str] = None
    vessel_status: Optional[str] = None

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


class VesselEntity(IDName):
    """
    A VesselEntity represents a vessel record used in CargoMovements and VesselMovements.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: Optional[str] = None
    mmsi: Optional[int] = None
    imo: Optional[int] = None

    dwt: Optional[int] = None

    vessel_class: Optional[str] = None
    corporate_entities: Optional[
        List[VesselEntityCorporateEntityWithConfidence]
    ] = None
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None
    year: Optional[int] = None

    start_timestamp: Optional[ISODate] = None

    cubic_capacity: Optional[int] = None
    voyage_id: Optional[str] = None
    fixture_fulfilled: Optional[bool] = None
    end_timestamp: Optional[ISODate] = None
    fixture_id: Optional[str] = None

    scrubber: Optional[List[Scrubber]] = None
    flag: Optional[List[Flag]] = None
    ice_class: Optional[str] = None
    propulsion: Optional[str] = None
