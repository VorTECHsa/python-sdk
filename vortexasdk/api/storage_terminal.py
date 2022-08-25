from pydantic import BaseModel
from typing import List


from vortexasdk.api.shared_types import IDNameLayer, ISODate


class TerminalHierarchy(BaseModel):
    id: str
    label: str
    layer: str


class TerminalParent(BaseModel):
    id: str
    layer: List[str]
    name: str


class StorageTerminal(BaseModel):
    """
    Represents a Storage Terminal reference record returned by the API.
    """

    id: str
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[TerminalHierarchy]
    layer: List[str]
    lat: float
    lon: float
    leaf: bool
    name: str
    parent: List[TerminalParent]
    ref_type: str
