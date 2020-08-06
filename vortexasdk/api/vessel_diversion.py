from dataclasses import dataclass
from typing import List, Optional

from api import ProductEntity, GeographyEntity, CorporateEntity
from vortexasdk.api import ID, Entity, ISODate
from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class DiversionCargo(FromDictMixin):
    product_hierarchy: List[ProductEntity]
    quantity: float


@dataclass(frozen=True)
class VesselDiversion(FromDictMixin):
    id: ID
    timestamp: ISODate
    cargoes: List[DiversionCargo]
    origin: List[GeographyEntity]
    is_considered_waypoint: bool

    prev_destination: List[Entity]
    prev_eta: ISODate
    prev_declared_destination: str

    next_destination: List[Entity]
    next_eta: ISODate
    next_declared_destination: str
    next_destination_timestamp: ISODate

    vessel_id: ID
    vessel_name: str
    vessel_class: str
    vessel_corporate_entities: List[CorporateEntity]
    vessel_imo: Optional[int] = None
