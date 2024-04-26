from typing import Any
from pydantic import BaseModel

from vortexasdk.api import ID

from vortexasdk.api.shared_types import (
    IDName,
    ISODate,
    Node,
    Tag,
    Scrubber,
    Flag,
    VesselClassEntry,
)


class VesselEntityCorporateEntity(BaseModel):
    id: ID
    label: str | None = None
    layer: str | None = None
    end_timestamp: ISODate | None = None
    start_timestamp: ISODate | None = None


class VesselEntityCorporateEntityWithConfidence(BaseModel):
    probability: float | None = None
    source: str | None = None
    id: ID | None = None
    label: str | None = None
    layer: str | None = None
    end_timestamp: ISODate | None = None
    start_timestamp: ISODate | None = None


class Vessel(Node):
    """
    Represent a Vessel reference record returned by the API.

    [Vessels Further Documentation](https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D)
    """

    related_names: list[str] | None = None
    mmsi: int | None = None
    layer: list[str] | None = None

    tags: list[Tag] | None = None
    current_product_type: list[Any] | None = None

    vessel_class: str | None = None
    classes: list[VesselClassEntry] | None = None
    vessel_status: str | None = None

    corporate_entities: list[VesselEntityCorporateEntity] | None = None
    dead_weight: int | None = None
    cubic_capacity: int | None = None
    to_bow: int | None = None
    to_stern: int | None = None
    to_port: int | None = None
    to_starboard: int | None = None
    call_sign: str | None = None
    year: int | None = None
    imo: int | None = None
    gross_tonnage: int | None = None

    scrubber: list[Scrubber] | None = None
    flag: list[Flag] | None = None
    ice_class: str | None = None
    propulsion: str | None = None


class VesselEntity(IDName):
    """
    A VesselEntity represents a vessel record used in CargoMovements.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: ID
    name: str | None = None
    mmsi: int | None = None
    imo: int | None = None

    dwt: int | None = None

    vessel_class: str | None = None
    classes: list[VesselClassEntry] | None = None
    corporate_entities: (
        list[VesselEntityCorporateEntityWithConfidence] | None
    ) = None
    tags: list[Tag] | None = None
    status: str | None = None
    year: int | None = None

    start_timestamp: ISODate | None = None

    cubic_capacity: int | None = None
    voyage_id: str | None = None
    fixture_fulfilled: bool | None = None
    end_timestamp: ISODate | None = None
    fixture_id: str | None = None

    scrubber: list[Scrubber] | None = None
    flag: list[Flag] | None = None
    ice_class: str | None = None
    propulsion: str | None = None
