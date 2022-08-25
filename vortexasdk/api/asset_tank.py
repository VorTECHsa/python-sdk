from pydantic import BaseModel
from typing import List, Optional


from vortexasdk.api.shared_types import ISODate


class CorporateEntity(BaseModel):
    id: str
    label: str
    layer: Optional[str] = None


class LocationDetails(BaseModel):
    id: str
    label: str
    layer: str


class AssetTank(BaseModel):
    """
    Represents an Asset Tank reference record returned by the API.
    """

    id: str
    capacity_bbl: int
    capacity_cbm: int
    capacity_ton: int
    corporate_entity_details: CorporateEntity
    corporate_entity_id: str
    leaf: bool
    location_id: str
    location_details: List[LocationDetails]
    name: str
    lat: float
    lon: float
    radius: int
    ref_type: str
    storage_terminal_id: str
    storage_terminal_name: str
    storage_type: str
    last_updated: ISODate
    crude_confidence: Optional[str] = None
