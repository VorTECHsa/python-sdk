from pydantic.dataclasses import dataclass
from typing import List, Optional, Tuple


from vortexasdk.api.shared_types import (
    EntityWithListLayerAndProbability,
    ID,
    EntityWithSingleLayerAndProbability,
    IDLayer,
    IDNameLayer,
    Node,
)

Position = Tuple[float, float]


@dataclass(frozen=True)
class BoundingBox:
    """Polygon with list of bounding lon lat coords."""

    type: str
    coordinates: List[Position]


@dataclass(frozen=True)
class Geography(Node):
    """Represent a Geography reference record returned by the API."""

    id: ID
    name: str
    layer: List[str]
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[IDLayer]
    pos: List[str]


@dataclass(frozen=True)
class GeographyEntity(EntityWithSingleLayerAndProbability):
    """
    Represents a hierarchy tree of locational data.

    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)

    """
