from dataclasses import dataclass
from typing import List


@dataclass
class LayerEntity:
    """

    """
    id: str
    layer: str
    label: str
    probability: float
    source: str


@dataclass
class GeographyEntity(LayerEntity):
    """
    A GeographyEntry represents a hierarchy tree of locational data.


    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)

    """


@dataclass
class ProductEntity(LayerEntity):
    """
    A ProductEntry represents a single product layer of a hierarchical product tree.

    [Product Entity Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)

    """


@dataclass
class CorporateEntity(LayerEntity):
    """
    A CorporateEntity represents a relationship between a corporate entity and another entity like a vessel.

    [Corporate Entity Further Documentation](https://docs.vortexa.com/reference/intro-corporate-entities)

    """


@dataclass
class TagEntity:
    """
    A Tag represents a property that is associated with a period of time.
    A good example is if a vessel has acted as an FSO during a time period.

    [Tags Further Documentation](https://docs.vortexa.com/reference/intro-tags)


    """
    tag: str
    start_timestamp: str = None
    end_timestamp: str = None


@dataclass
class VesselEntity:
    """
    A VesselEntity represents a vessel record

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)

    """
    id: str
    mmsi: int
    imo: int
    name: str
    dwt: int
    cubic_capacity: int
    vessel_class: str
    corporate_entities: List[CorporateEntity]
    start_timestamp: str
    tags: List[TagEntity]
    status: str

    voyage_id: str = None
    fixture_fulfilled: bool = None
    end_timestamp: str = None
    fixture_id: str = None


@dataclass
class CargoEventEntity:
    """
    A CargoEvent represents an event that occurred to a cargo during a cargo movement


    [Cargo Event Entities Further Documentation](https://docs.vortexa.com/reference/intro-cargo-events)

    """
    event_type: str
    pos: List[float]

    probability: float = None
    vessel_id: str = None
    start_timestamp: str = None
    end_timestamp: str = None
    location: List[GeographyEntity] = None


@dataclass
class CargoMovementEntity:
    """
    Cargo movements are the base data set the Vortexa API is centred around.
    Each movement represents a journey of a certain quantity of a product between places.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    cargo_movement_id: str
    quantity: int
    status: str
    vessels: List[VesselEntity]
    product: List[ProductEntity]
    events: List[CargoEventEntity]
