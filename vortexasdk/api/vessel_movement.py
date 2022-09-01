from pydantic import BaseModel
from typing import List, Optional

from vortexasdk.api.geography import GeographyEntity
from vortexasdk.api.id import ID
from vortexasdk.api.product import ProductEntityWithSingleLayer

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.vessel import VesselEntity


class VesselEvent(BaseModel):
    """Represent an event that occurred to a vessel during a vessel movement."""

    event_type: Optional[str] = None
    location: Optional[List[GeographyEntity]] = None
    pos: Optional[List[float]] = None

    event_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


class VesselMovementCargo(BaseModel):
    cargo_movement_id: Optional[ID] = None
    quantity: Optional[float] = None
    product: Optional[List[ProductEntityWithSingleLayer]] = None


class VesselMovement(BaseModel):
    """
    [Vessel Movement Further Documentation](https://docs.vortexa.com/reference/intro-vessel-movement)

    """

    vessel_movement_id: Optional[ID] = None
    voyage_id: Optional[ID] = None
    vessel: Optional[VesselEntity] = None

    origin: Optional[VesselEvent] = None
    destination: Optional[VesselEvent] = None
    cargoes: Optional[List[VesselMovementCargo]] = None

    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
