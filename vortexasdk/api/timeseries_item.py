from typing import List, Optional
from pydantic import BaseModel

from vortexasdk.api import ISODate


class TimeSeriesBreakdownItem(BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    value: Optional[float] = None
    count: Optional[int] = None


class TimeSeriesItem(BaseModel):
    """
    Generic container class holding a `key <> value` pair, a `count` of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """

    key: Optional[ISODate] = None
    count: Optional[int] = None
    breakdown: Optional[List[TimeSeriesBreakdownItem]] = None
    value: Optional[float] = None
