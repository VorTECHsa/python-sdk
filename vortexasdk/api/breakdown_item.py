from dataclasses import dataclass
from typing import Dict, List, Optional

from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class BreakdownItem(FromDictMixin):
    """
    Generic container class holding a `key <> value` pair, a `count`, and optionally a `label` and a `breakdown` of records contributing to the given value.

    For example, this class could hold the average speed of vessels (`value`) on 2019-01-01 (`key`), the number of vessels contributing to the
    this average (count) and additional information about the aggregation (`breakdown`).

    If the `BreakdownItem` is enriched by reference data (e.g. in `fleet-utilisation/breakdown/origin`), `key` is the ID of the reference entity, `label` holds its name 
    and `value` and `count` correspond to numeric values of the returned record.
    """

    key: str
    count: int
    value: float = None
    label: Optional[str] = None
    breakdown: Optional[List[Dict]] = None
