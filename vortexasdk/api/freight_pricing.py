from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from vortexasdk.api.id import ID


class FreightPricingPrediction(BaseModel):
    prediction: Optional[str] = None
    prediction_type: Optional[str] = None
    rating: Optional[str] = None


class FreightPricing(BaseModel):
    """
    Freight pricing shows pricing information applicable to a selected route on a given day.
    """

    id: Optional[ID] = None
    short_code: Optional[str] = None
    rate: Optional[float] = None
    record_date: Optional[datetime] = None
    rate_precision: Optional[int] = None
    rate_unit: Optional[str] = None
    cost: Optional[float] = None
    cost_precision: Optional[int] = None
    cost_unit: Optional[str] = None
    tce: Optional[float] = None
    tce_precision: Optional[int] = None
    tce_unit: Optional[str] = None
    predictions: Optional[List[FreightPricingPrediction]] = None
