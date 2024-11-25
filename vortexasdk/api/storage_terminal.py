from pydantic import v1 as pydantic_v1

from typing import List, Optional


from vortexasdk.api.shared_types import IDNameLayer


class TerminalHierarchy(pydantic_v1.BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    layer: Optional[str] = None


class TerminalParent(pydantic_v1.BaseModel):
    id: Optional[str] = None
    layer: Optional[List[str]] = None
    name: Optional[str] = None


class StorageTerminal(pydantic_v1.BaseModel):
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
