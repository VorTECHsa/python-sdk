from dataclasses import dataclass
from typing import Optional

from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class EIAForecast(FromDictMixin):
    """Represent a EIA forecast record returned by the API."""

    date: str
    forecast_fri: float
    value: Optional[int]
    stocks: Optional[int]
    cover: Optional[float]
    runs: Optional[float]
