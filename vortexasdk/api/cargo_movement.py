from pydantic import Field
from pydantic.dataclasses import dataclass
from typing import List, Literal, Optional, Union
from typing_extensions import Annotated

from vortexasdk.api.geography import GeographyEntity
from vortexasdk.api.product import ProductEntityWithSingleLayer

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


@dataclass(frozen=True)
class RawLocations:
    probability: float
    location_id: str


@dataclass(frozen=True)
class CargoPortLoadEvent:
    vessel_id: ID
    start_timestamp: ISODate
    event_type: Literal["cargo_port_load_event"]
    location: List[GeographyEntity]
    probability: float
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


@dataclass(frozen=True)
class CargoFSOLoadEvent:
    start_timestamp: ISODate
    event_type: Literal["cargo_fso_load_event"]
    location: List[GeographyEntity]
    probability: float
    fso_vessel_id: ID
    fso_vessel_name: str
    to_vessel_id: ID
    to_vessel_name: str
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


@dataclass(frozen=True)
class CargoPortUnloadEvent:
    vessel_id: ID
    event_type: Literal["cargo_port_unload_event"]
    location: List[GeographyEntity]
    probability: float
    end_timestamp: Optional[ISODate] = None
    raw_locations: Optional[List[RawLocations]] = None
    pos: Optional[List[float]] = None
    start_timestamp: Optional[ISODate] = None
    restricted: Optional[bool] = False


@dataclass(frozen=True)
class CargoFSOUnloadEvent:
    start_timestamp: ISODate
    event_type: Literal["cargo_fso_unload_event"]
    location: List[GeographyEntity]
    probability: float
    fso_vessel_id: str
    fso_vessel_name: str
    from_vessel_id: str
    from_vessel_name: str
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


@dataclass(frozen=True)
class CargoFixtureEvent:
    start_timestamp: ISODate
    event_type: Literal["cargo_fixture_event"]
    end_timestamp: Optional[ISODate] = None


@dataclass(frozen=True)
class CargoSTSEvent:
    start_timestamp: ISODate
    event_type: Literal["cargo_sts_event"]
    location: List[GeographyEntity]
    to_vessel_id: str
    to_vessel_name: str
    from_vessel_id: str
    from_vessel_name: str
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


@dataclass(frozen=True)
class CargoStorageEvent:
    vessel_id: ID
    start_timestamp: ISODate
    event_type: Literal["cargo_storage_event"]
    location: List[GeographyEntity]
    vessel_class: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


@dataclass(frozen=True)
class CargoWaypointEvent:
    vessel_id: ID
    start_timestamp: ISODate
    event_type: Literal["cargo_waypoint_event"]
    location: List[GeographyEntity]
    probability: float
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


@dataclass(frozen=True)
class CargoTransitingEvent:
    start_timestamp: ISODate
    event_type: Literal["cargo_transiting_event"]
    end_timestamp: Optional[ISODate] = None


@dataclass(frozen=True)
class CargoOilOnWaterEvent:
    start_timestamp: ISODate
    event_type: Literal["cargo_oil_on_water_event"]
    end_timestamp: Optional[ISODate] = None


@dataclass(frozen=True)
class ParentID:
    """

    `cargo_movement_id` may change under certain conditions. `ParentID` contains an `id`,
    a previous id of the cargo movement, and a `splinter_timestamp`, the time at which the id change occurred.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    id: str
    splinter_timestamp: ISODate


@dataclass(frozen=True)
class CargoMovementProductEntry:
    probability: float
    source: str
    id: ID
    layer: Optional[str] = None
    label: Optional[str] = None


@dataclass(frozen=True)
class CargoMovement:
    """

    Cargo movements are the base data set the Vortexa API is centred around.

    Each movement represents a journey of a certain quantity of a product between places.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    cargo_movement_id: ID
    quantity: int
    status: str
    vessels: List[VesselEntity]
    product: List[CargoMovementProductEntry]
    parent_ids: List[ParentID]
    events: List[
        Annotated[
            Union[
                CargoPortLoadEvent,
                CargoFSOLoadEvent,
                CargoPortUnloadEvent,
                CargoFSOUnloadEvent,
                CargoFixtureEvent,
                CargoSTSEvent,
                CargoStorageEvent,
                CargoWaypointEvent,
                CargoTransitingEvent,
                CargoOilOnWaterEvent,
            ],
            Field(discriminator="event_type"),
        ]
    ]
