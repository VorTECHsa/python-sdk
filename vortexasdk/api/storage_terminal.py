from pydantic import BaseModel
from typing import List, Optional


from vortexasdk.api.shared_types import IDNameLayer


class TerminalHierarchy(BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    layer: Optional[str] = None


class TerminalParent(BaseModel):
    id: Optional[str] = None
    layer: Optional[List[str]] = None
    name: Optional[str] = None


class StorageTerminal(BaseModel):
    """
    Represents a Storage Terminal reference record returned by the API.
    """

    id: Optional[str] = None
    exclusion_rule: Optional[List[IDNameLayer]] = None
    hierarchy: Optional[List[TerminalHierarchy]] = None
    layer: Optional[List[str]] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    leaf: Optional[bool] = None
    name: Optional[str] = None
    parent: Optional[List[TerminalParent]] = None
    ref_type: Optional[str] = None
