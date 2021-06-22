from dataclasses import dataclass
from typing import Dict, List

from vortexasdk.api import ISODate
from vortexasdk.api.serdes import FromDictMixin




@dataclass(frozen=True)
class Breakdown(FromDictMixin):
    """
    Generic container class holding a _key_, _value_ pair, and a _count_ of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """

    key: str
    value: float
    count: float

@dataclass(frozen=True)
class GeographyBreakdownItem(FromDictMixin):
    """
    Generic container class holding a _key_, _value_ pair, and a _count_ of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """

    key: ISODate
    count: int
    breakdown: List[Breakdown]
    value: float = None

@dataclass(frozen=True)
class GeographyReferenceEntry(FromDictMixin):
    """
    Generic container class holding a _key_, _value_ pair, and a _count_ of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """
    label: str
    record: int
    type: str

@dataclass(frozen=True)
class GeographyBreakdown(FromDictMixin):
    """
    Generic container class holding a _key_, _value_ pair, and a _count_ of records contributing to the given value.

    For example, this class could hold the total tonnage exported (value) on 2019-01-01 (key), and the count of cargo
    movements contributing to this tonnage aggregate, ie the number of cargo movements on this day (count).
    """

    data: List[GeographyBreakdownItem]
    reference: Dict[str, GeographyReferenceEntry]


