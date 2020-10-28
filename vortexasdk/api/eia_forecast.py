from dataclasses import dataclass
from typing import List

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import IDName


@dataclass(frozen=True)
class EIAForecast(IDName, FromDictMixin):
    """Represent a EIA forecast record returned by the API."""

    date: List[str]
    forecast_fri: float
    value: int
    stocks: int
    cover: float
    runs: float
