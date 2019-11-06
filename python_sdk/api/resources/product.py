from dataclasses import dataclass
from enum import Enum


class ProductLayer(Enum):
    """ProductLayer describes layers in the hierarchical product tree

    Layer 1 (Group) is the widest layer, each subsequent layer becomes more specific with layer 4 (Grade) being the
    most specific.
    """
    grade = 'grade'
    category = 'category'
    group_product = 'group_product'
    group = 'group'


@dataclass
class ProductEntity:
    """A ProductEntry represents a single product layer of a hierarchical product tree. """
    id: str
    layer: ProductLayer
    label: str
    source: str
    probability: float
