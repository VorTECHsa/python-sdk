from dataclasses import dataclass
from typing import List

from python_sdk.api.resources.geography import GeographyEntity


@dataclass
class CargoEventEntity:
    # always present
    event_type: str
    pos: List[float]

    # optional
    probability: float = None
    vessel_id: str = None
    start_timestamp: str = None
    end_timestamp: str = None
    location: List[GeographyEntity] = None
