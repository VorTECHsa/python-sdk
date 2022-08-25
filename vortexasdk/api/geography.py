from pydantic import BaseModel
from typing import List, Tuple


from vortexasdk.api.shared_types import (
    ID,
    EntityWithSingleLayerAndProbability,
    IDLayer,
    IDNameLayer,
    Node,
)

Position = Tuple[float, float]



class BoundingBox(BaseModel):
    """Polygon with list of bounding lon lat coords."""

    type: str
    coordinates: List[Position]



class Geography(Node, BaseModel):
    """Represent a Geography reference record returned by the API."""

    id: ID
    name: str
    layer: List[str]
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[IDLayer]
    pos: List[str]



class GeographyEntity(EntityWithSingleLayerAndProbability, BaseModel):
    """
    Represents a hierarchy tree of locational data.

    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)

    """
