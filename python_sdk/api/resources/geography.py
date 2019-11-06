from dataclasses import dataclass


@dataclass
class GeographyEntity:
    """
    A GeographyEntry represents a hierarchy tree of locational data.


    # Further Documentation
    https://docs.vortexa.com/reference/intro-geography-entries
    """
    id: str
    layer: str
    label: str
    probability: float
    source: str
