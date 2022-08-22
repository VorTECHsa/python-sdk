from typing import List, Optional
from pydantic.dataclasses import dataclass

from vortexasdk.api import ISODate


@dataclass(frozen=True)
class TimeSeriesBreakdownItem:
    id: str
    label: str
    value: float
    count: int


@dataclass(frozen=True)
class TimeSeriesItem:
    """
    Generic container class holding a `key <> value` pair, a `count` of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """

    key: ISODate
    count: int
    breakdown: Optional[List[TimeSeriesBreakdownItem]] = None
    value: Optional[float] = None
