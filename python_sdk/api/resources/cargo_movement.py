from dataclasses import dataclass
from typing import List

from python_sdk.api.resources.cargo_event import CargoEventEntity
from python_sdk.api.resources.product import ProductEntity
from python_sdk.api.resources.vessel import VesselEntity


@dataclass
class CargoMovementEntity:
    cargo_movement_id: str
    quantity: int
    status: str
    vessels: List[VesselEntity]
    product: List[ProductEntity]
    events: List[CargoEventEntity]
