from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ID:
    """Represent an `id`."""
    id: str


@dataclass(frozen=True)
class Name:
    """Represent a `name`."""
    name: str


@dataclass(frozen=True)
class Layer:
    """Represent a `layer`."""
    layer: str


@dataclass(frozen=True)
class IDName(ID, Name):
    """Tuple containing `id` and `name`."""
    pass


@dataclass(frozen=True)
class IDLayer(ID, Layer):
    """Tuple containing `id` and `layer`."""
    pass


@dataclass(frozen=True)
class IDNameLayer(ID, Name, Layer):
    """Triple holding `id`, `name`, and `layer`."""
    pass


@dataclass(frozen=True)
class Node(ABC, IDName):
    """Abstract Base Class holding a node of a tree."""
    ref_type: str
    leaf: bool
    parent: List[IDNameLayer]


@dataclass(frozen=True)
class BoundingBox:
    """Polygon with list of bounding lat lon coords."""
    type: str
    coordinates: List[List[float]]


@dataclass(frozen=True)
class GeographyNode(Node, IDNameLayer):
    """Represent a Polygon."""
    bounding_box: BoundingBox
    centre_point: List[float]
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[IDLayer]


@dataclass(frozen=True)
class ChartererNode(IDName):
    """
    Represent a Charterer.

    This class is almost inherets from `Node`,
     but not quite - it's parents are a list of strings rather than list of `IDName`
    """
    corporate_entity_type: List[str]
    ref_type: str
    leaf: bool
    parent: List[str]


@dataclass(frozen=True)
class ProductNode(Node):
    """
    Represent a Product.

    # Further Documentation

    https://docs.vortexa.com/reference/GET/reference/products/%7Bid%7D
    """
    layer: List[str]
    meta: dict


@dataclass(frozen=True)
class VesselNode(Node):
    """
    Represent a Vessel.

    # Further Documentation

    https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D
    """
    related_names: List[str]
    mmsi: int
    imo: int
    cubic_capacity: int
    call_sign: str
    to_bow: str
    to_stern: str
    to_port: str
    to_starboard: str
    year: int
    dead_weight: int
    gross_tonnage: int
