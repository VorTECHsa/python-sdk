from pydantic.dataclasses import dataclass
from typing import List


from vortexasdk.api.shared_types import (
    EntityWithListLayerAndProbability,
    EntityWithSingleLayer,
    EntityWithSingleLayerAndProbability,
    Node,
)


@dataclass(frozen=True)
class Product(Node):
    """
    Represent a Product reference record returned by the API.

    [Product Further Documentation](https://docs.vortexa.com/reference/GET/reference/products/%7Bid%7D)
    """

    layer: List[str]
    meta: dict
    hierarchy: List[EntityWithSingleLayer]


@dataclass(frozen=True)
class ProductEntityWithSingleLayer(EntityWithSingleLayerAndProbability):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """


@dataclass(frozen=True)
class ProductEntityWithListLayer(EntityWithListLayerAndProbability):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """
