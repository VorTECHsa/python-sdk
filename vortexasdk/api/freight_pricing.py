from dataclasses import dataclass
from typing import Optional
from vortexasdk.api.id import ID
from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class FreightPricing(FromDictMixin):
    """
    Freight pricing shows pricing information applicable to a selected route on a given day.
    """
    id: ID
    short_code: str
    rate: float
    rate_precision: int
    rate_unit: str
    cost: float
    cost_precision: int
    cost_unit: str
    tce: Optional[float]
    tce_precision: Optional[int]
    tce_unit: Optional[str]
    source: Optional[str]
    route_prediction: Optional[str]
