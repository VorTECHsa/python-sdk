from pydantic import BaseModel
from typing import Optional
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


class Entity(BaseModel):
    id: str = None
    label: str = None


class Fixture(BaseModel):
    """Represent a Fixture record returned by the API."""
    id: ID
    vessel: VesselEntity = None
    laycan_from: str = None
    laycan_to: str = None
    tones: int = None
    fixing_timestamp: str = None
    fulfilled: bool = None
    vtx_fulfilled: bool = None
    origin: Optional[Entity] = None
    destination: Optional[Entity] = None
    product: Optional[Entity] = None
    charterer: Optional[Entity] = None
    origin: Optional[Entity] = None
