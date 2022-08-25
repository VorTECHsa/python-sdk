from pydantic import BaseModel
from typing import List, Optional

from vortexasdk.api.geography import GeographyEntity
from vortexasdk.api.id import ID
from vortexasdk.api.product import ProductEntityWithSingleLayer

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.vessel import VesselEntity



class VesselEvent(BaseModel):
    """Represent an event that occurred to a vessel during a vessel movement."""

    event_type: str
    location: List[GeographyEntity]
    pos: Optional[List[float]] = None

    event_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None



class VesselMovementCargo(BaseModel):
    cargo_movement_id: ID
    quantity: float
    product: List[ProductEntityWithSingleLayer]



class VesselMovement(BaseModel):
    """
    [Vessel Movement Further Documentation](https://docs.vortexa.com/reference/intro-vessel-movement)

    """

    vessel_movement_id: ID
    voyage_id: ID
    vessel: VesselEntity

    origin: VesselEvent
    destination: VesselEvent
    cargoes: List[VesselMovementCargo]

    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
