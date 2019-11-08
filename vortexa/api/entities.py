"""DataClasses returned by VortexaAPI."""
from dataclasses import dataclass
from typing import List, Optional

from vortexa.api.references import IDLayer, IDName


@dataclass(frozen=True)
class Entity(IDLayer):
    """

    Contains a set of attributes commonly used by various entities.

    [Entities Further Documentation](https://docs.vortexa.com/reference/intro-entities)

    """
    label: str
    probability: float
    source: str


@dataclass(frozen=True)
class GeographyEntity(Entity):
    """

    Represents a hierarchy tree of locational data.

    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)


    """


@dataclass(frozen=True)
class ProductEntity(Entity):
    """

    Represents a single product layer of a hierarchical product tree.

    [Product Entity Further Documentation](https://docs.vortexa.com/reference/intro-product-entities)


    """


@dataclass(frozen=True)
class CorporateEntity(Entity):
    """

    Represents a relationship between a corporation and another entity like a vessel.

    [Corporate Entity Further Documentation](https://docs.vortexa.com/reference/intro-corporate-entities)


    """


@dataclass(frozen=True)
class TagEntity:
    """

    Represents a property that is associated with a period of time.

    A good example is if a vessel has acted as an FSO during a time period.

    [Tags Further Documentation](https://docs.vortexa.com/reference/intro-tags)

    """

    tag: str
    start_timestamp: Optional[str] = None
    end_timestamp: Optional[str] = None


@dataclass(frozen=True)
class VesselEntity(IDName):
    """

    A VesselEntity represents a vessel record used in CargoMovements and VesselMovements.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)

    """

    mmsi: int
    dwt: int
    cubic_capacity: int
    vessel_class: str
    corporate_entities: List[CorporateEntity]
    start_timestamp: str
    tags: List[TagEntity]
    status: str

    imo: Optional[int] = None
    voyage_id: Optional[str] = None
    fixture_fulfilled: Optional[bool] = None
    end_timestamp: Optional[str] = None
    fixture_id: Optional[str] = None


@dataclass(frozen=True)
class CargoEventEntity:
    """

    A CargoEvent represents an event that occurred to a cargo during a cargo movement.

    [Cargo Event Entities Further Documentation](https://docs.vortexa.com/reference/intro-cargo-events)

    """

    event_type: str
    location: List[GeographyEntity]

    probability: Optional[float] = None
    pos: Optional[List[float]] = None
    vessel_id: Optional[str] = None
    start_timestamp: Optional[str] = None
    end_timestamp: Optional[str] = None


@dataclass(frozen=True)
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
