from dataclasses import dataclass

from vortexasdk.api.serdes import FromDictMixin

@dataclass(frozen=True)
class GeographyBreakdownItem(FromDictMixin):
    """
    A container class holding a _key_, _value_ pair, and a _count_ of records contributing to the given value.

    For example, this class could hold the total number of unique vessels (value) on for a given geography (key), 
    and the count of vessel movements contributing to this value in the specified period (count).
    """

    key: str
    count: int
    value: float = None
