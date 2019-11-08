from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class ID:
    id: str


@dataclass
class Name:
    name: str


@dataclass
class Layer:
    layer: str


@dataclass
class IDName(ID, Name):
    pass


@dataclass
class IDLayer(ID, Layer):
    pass


@dataclass
class IDNameLayer(ID, Name, Layer):
    """Triple holding ID, name, and layer."""
    pass


@dataclass
class Node(ABC, IDName):
    """Abstract Base Class holding a node of a tree."""
    ref_type: str
    leaf: bool
    parent: List[IDNameLayer]


@dataclass
class BoundingBox:
    """Polygon with list of bounding lat lon coords."""
    type: str
    coordinates: List[List[float]]


@dataclass
class GeographyNode(Node, IDNameLayer):
    """Represent a Polygon."""
    bounding_box: BoundingBox
    centre_point: List[float]
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[IDLayer]


@dataclass
class ChartererNode(IDName):
    """
    Represent a Charterer.

    This class is almost a `Node`,
     but not quite - it's parents are a list of strings rather than list of `IDName`
    """
    corporate_entity_type: List[str]
    ref_type: str
    leaf: bool
    parent: List[str]


@dataclass
class ProductNode(Node):
    layer: List[str]
    meta: dict
