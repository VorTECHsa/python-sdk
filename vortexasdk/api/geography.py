from pydantic import BaseModel
from typing import List, Optional, Tuple


from vortexasdk.api import ID
from vortexasdk.api.shared_types import (
    EntityWithSingleLayerAndProbability,
    IDLayer,
    IDNameLayer,
    Node,
)

Position = Tuple[float, float]


class BoundingBox(BaseModel):
    """Polygon with list of bounding lon lat coords."""

    type: Optional[str] = None
    coordinates: Optional[List[Position]] = None


class Geography(Node):
    """Represent a Geography reference record returned by the API."""

    id: ID
    name: Optional[str] = None
    layer: List[str] = []
    exclusion_rule: Optional[List[IDNameLayer]] = None
    hierarchy: Optional[List[IDLayer]] = None
    pos: Optional[List[float]] = None


class GeographyEntity(EntityWithSingleLayerAndProbability):
    """
    Represents a hierarchy tree of locational data.

    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)

    """
