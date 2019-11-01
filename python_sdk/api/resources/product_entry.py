from dataclasses import dataclass


@dataclass
class ProductEntity:
    """A ProductEntry represents a single product layer of a hierarchical product tree. """
    id: str
    layer: str
    probability: float
    label: str
