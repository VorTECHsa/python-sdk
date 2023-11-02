from pydantic import BaseModel
from typing import Optional

from vortexasdk.api.id import ID

from vortexasdk.api.shared_types import ISODate


class VesselSummary(BaseModel):
    """
    Represents a Vessel Summary record returned by the API.

    [Vessel Summary Further Documentation](https://docs.vortexa.com/reference/POST/signals/vessel-summary)
    """

    vessel_id: Optional[ID] = None
    timestamp: Optional[ISODate] = None
    lat: Optional[str] = None
    lon: Optional[str] = None
    speed: Optional[float] = None
    draught: Optional[float] = None
    declared_destination: Optional[str] = None
    declared_eta: Optional[ISODate] = None
