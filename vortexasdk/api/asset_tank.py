from pydantic import BaseModel
from typing import List, Optional


from vortexasdk.api.shared_types import ISODate


class CorporateEntity(BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    layer: Optional[str] = None


class LocationDetails(BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    layer: Optional[str] = None


class AssetTank(BaseModel):
    """
    Represents an Asset Tank reference record returned by the API.
    """

    id: Optional[str] = None
    capacity_bbl: Optional[int] = None
    capacity_cbm: Optional[int] = None
    capacity_ton: Optional[int] = None
    corporate_entity_details: Optional[CorporateEntity] = None
    corporate_entity_id: Optional[str] = None
    leaf: Optional[bool] = None
    location_id: Optional[str] = None
    location_details: Optional[List[LocationDetails]] = None
    name: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    radius: Optional[int] = None
    ref_type: Optional[str] = None
    storage_terminal_id: Optional[str] = None
    storage_terminal_name: Optional[str] = None
    storage_type: Optional[str] = None
    last_updated: Optional[ISODate] = None
    crude_confidence: Optional[str] = None
