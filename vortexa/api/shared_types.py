from abc import ABC
from dataclasses import dataclass
from typing import List, Tuple, Optional

ID = str
Position = Tuple[float, float]
ISODate = str


@dataclass(frozen=True)
class Entity:
    id: ID
    label: str
    layer: str


@dataclass(frozen=True)
class EntityWithProbability(Entity):
    probability: float
    source: str


@dataclass(frozen=True)
class IDName:
    """Tuple containing `id` and `name`."""
    id: ID
    name: str


@dataclass(frozen=True)
class IDLayer:
    """Tuple containing `id` and `layer`."""
    id: ID
    name: str


@dataclass(frozen=True)
class IDNameLayer:
    """Triple holding `id`, `name`, and `layer`."""
    id: ID
    layer: str
    name: str


@dataclass(frozen=True)
class Node(ABC, IDName):
    """
    Abstract Base Class holding a node of a tree.

    # Attributes:
        ref_type: Identifies the reference type data
        leaf: Is this node a leaf of the hierarchal tree?
        parent: List of parents

    """
    ref_type: str
    leaf: bool
    parent: List[IDNameLayer]


@dataclass(frozen=True)
class Tag:
    """

    Represents a property that is associated with a period of time.

    A good example is if a vessel has acted as an FSO during a time period.

    [Tags Further Documentation](https://docs.vortexa.com/reference/intro-tags)

    """

    tag: str
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
