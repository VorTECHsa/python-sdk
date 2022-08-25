from pydantic import BaseModel
from typing import List


from vortexasdk.api.shared_types import (
    EntityWithListLayerAndProbability,
    EntityWithSingleLayer,
    EntityWithSingleLayerAndProbability,
    Node,
)



class Product(Node, BaseModel):
    """
    Represent a Product reference record returned by the API.

    [Product Further Documentation](https://docs.vortexa.com/reference/GET/reference/products/%7Bid%7D)
    """

    layer: List[str]
    meta: dict
    hierarchy: List[EntityWithSingleLayer]



class ProductEntityWithSingleLayer(EntityWithSingleLayerAndProbability, BaseModel):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """



class ProductEntityWithListLayer(EntityWithListLayerAndProbability, BaseModel):
    """

    Represents a single product layer of a hierarchical product tree.

    [Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)
    """
