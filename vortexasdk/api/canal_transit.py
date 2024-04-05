from pydantic import BaseModel
from typing import List, Optional

from vortexasdk.api.geography import GeographyEntity

from vortexasdk.api.shared_types import (
    EntityWithSingleLayer,
    ISODate,
    VesselClassEntry,
)
from vortexasdk.api.id import ID


class CargoEntity(BaseModel):
    cargo_movement_id: ID
    quantity_barrels: Optional[int]
    quantity_tonnes: Optional[int]
    quantity_cubic_metres: Optional[int]
    product: Optional[List[EntityWithSingleLayer]]


class GeographyRecord(BaseModel):
    id: ID
    layer: Optional[List[str]] = None
    label: Optional[str] = None
    aliases: Optional[List[str]] = None


class CorporateRecord(BaseModel):
    id: ID
    label: str


class CanalTransitRecord(BaseModel):
    """

    The canal transits dataset contains information about ships waiting to cross major global canals.

    An entry in this dataset records information about a vessels transit through a canal, including the the actual queue arrival time, the planned canal entry time, the actual canal entry time, and the actual canal exit time.

    [Canal Transit Further Documentation](https://docs.vortexa.com/reference/intro-canal-transit)

    """

    id: ID
    voyage_id: Optional[ID] = None
    vessel_id: Optional[ID] = None
    vessel_name: Optional[str] = None
    vessel_imo: Optional[int] = None
    vessel_mmsi: Optional[int] = None
    vessel_class: Optional[List[VesselClassEntry]] = None
    vessel_cubic_capacity: Optional[int] = None
    vessel_dead_weight: Optional[int] = None
    canal: str
    direction: str
    lock: str
    queue_arrival_time: Optional[ISODate] = None
    canal_entry_time: Optional[ISODate] = None
    canal_exit_time: Optional[ISODate] = None
    booked_time: Optional[ISODate] = None
    voyage_status: Optional[str] = None
    cargoes: Optional[List[CargoEntity]]
    origin: Optional[List[GeographyEntity]]
    destination: Optional[List[GeographyEntity]]
    charterer: Optional[CorporateRecord] = None
    effective_controller: Optional[CorporateRecord] = None
