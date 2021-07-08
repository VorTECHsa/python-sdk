from dataclasses import dataclass
from typing import Dict, List

from vortexasdk.api import ISODate
from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class BreakdownItem(FromDictMixin):
    """
    Generic container class holding a _key_, _value_ pair, and a _count_ and breakdown of records contributing to the given value.

    For example, this class could hold the average speed of vessels (value) on 2019-01-01 (key), the number of vessels contributing to the
    this average (count) and additional information about the aggregation (breakdown).
    """

    key: ISODate
    count: int
    breakdown: List[Dict]
    value: float = None
