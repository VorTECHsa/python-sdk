from dataclasses import dataclass
from typing import List, Tuple

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import ISODate


@dataclass(frozen=True)
class TerminalHierarchy:
    id: str
    label: str
    layer: str


@dataclass(frozen=True)
class TerminalParent:
    id: str
    layer: List[str]
    name: str


@dataclass(frozen=True)
class StorageTerminal(FromDictMixin):
    """
    Represents a Storage Terminal reference record returned by the API.
    """
    id: str
    exclusion_rule: List[str]
    hierarchy: List[TerminalHierarchy]
    layer: List[str]
    lat: float
    lon: float
    leaf: bool
    name: str
    parent: List[TerminalParent]
