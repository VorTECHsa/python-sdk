from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class EIAForecast:
    """Represent a EIA forecast record returned by the API."""

    date: str
    forecast_fri: float
    value: Optional[int] = None
    stocks: Optional[int] = None
    cover: Optional[float] = None
    runs: Optional[float] = None
