from pydantic import BaseModel
from typing import Optional
from vortexasdk.api import ID

from vortexasdk.api.shared_types import ISODate


class VesselPositions(BaseModel):
    """
    Represents an AIS Vessel Position record returned by the API.
    """

    vessel_id: Optional[ID] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    timestamp: Optional[ISODate] = None
    speed: Optional[float] = None
    heading: Optional[float] = None
