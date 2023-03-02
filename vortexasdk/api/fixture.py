from pydantic import BaseModel
from typing import Optional
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


class Entity(BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None


class Fixture(BaseModel):
    """Represent a Fixture record returned by the API."""

    id: ID
    vessel: Optional[VesselEntity] = None
    laycan_from: Optional[str] = None
    laycan_to: Optional[str] = None
    tones: Optional[int] = None
    fixing_timestamp: Optional[str] = None
    fulfilled: Optional[bool] = None
    vtx_fulfilled: Optional[bool] = None
    origin: Optional[Entity] = None
    destination: Optional[Entity] = None
    product: Optional[Entity] = None
    charterer: Optional[Entity] = None
