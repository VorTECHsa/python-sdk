from pydantic import v1 as pydantic_v1
from typing import Optional


class EIAForecast(pydantic_v1.BaseModel):
    """Represent a EIA forecast record returned by the API."""

    date: Optional[str] = None
    forecast_fri: Optional[float] = None
    value: Optional[int] = None
    stocks: Optional[int] = None
    cover: Optional[float] = None
    runs: Optional[float] = None
