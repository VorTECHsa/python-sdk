from dataclasses import dataclass
from enum import Enum


class CorporateLayer(Enum):
    commercial_owner = 'commercial_owner'
    time_charterer = 'time_charterer'
    charterer = 'charterer'


@dataclass
class CorporateEntity:
    """
    A CorporateEntity represents a relationship between a corporate entity and another entity like a vessel.
    Vortexa currently exposes three layers of corporate entities:
    """
    id: str
    layer: CorporateLayer
    probability: float
    label: str
    source: str
