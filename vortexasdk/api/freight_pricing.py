from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from vortexasdk.api.id import ID



class FreightPricingPrediction(BaseModel):
    prediction: str
    prediction_type: str
    rating: str



class FreightPricing(BaseModel):
    """
    Freight pricing shows pricing information applicable to a selected route on a given day.
    """

    id: ID
    short_code: str
    rate: float
    record_date: datetime
    rate_precision: int
    rate_unit: str
    cost: float
    cost_precision: int
    cost_unit: str
    tce: Optional[float]
    tce_precision: Optional[int]
    tce_unit: Optional[str]
    predictions: Optional[List[FreightPricingPrediction]]
