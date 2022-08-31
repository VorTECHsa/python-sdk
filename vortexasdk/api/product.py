from typing import List, Optional


from vortexasdk.api.shared_types import (
    EntityWithListLayerAndProbability,
    EntityWithSingleLayer,
    EntityWithSingleLayerAndProbability,
    Node,
)


class Product(Node):
    """
    Represent a Product reference record returned by the API.

    [Product Further Documentation](https://docs.vortexa.com/reference/GET/reference/products/%7Bid%7D)
    """

    layer: Optional[List[str]] = None
    meta: Optional[dict] = None
    hierarchy: Optional[List[EntityWithSingleLayer]] = None


class ProductEntityWithSingleLayer(EntityWithSingleLayerAndProbability):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """


class ProductEntityWithListLayer(EntityWithListLayerAndProbability):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """
