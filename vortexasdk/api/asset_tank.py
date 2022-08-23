from pydantic.dataclasses import dataclass
from typing import List, Optional


from vortexasdk.api.shared_types import ISODate


@dataclass(frozen=True)
class CorporateEntity:
    id: str
    label: str
    layer: Optional[str] = None


@dataclass(frozen=True)
class LocationDetails:
    id: str
    label: str
    layer: str


@dataclass(frozen=True)
class AssetTank:
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
