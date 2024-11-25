from pydantic import v1 as pydantic_v1
from typing import List, Optional, Union
from typing_extensions import Annotated, Literal

from vortexasdk.api.geography import GeographyEntity

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


class RawLocations(pydantic_v1.BaseModel):
    probability: Optional[float] = None
    location_id: Optional[str] = None


class CargoPortLoadEvent(pydantic_v1.BaseModel):
    vessel_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_port_load_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoFSOLoadEvent(pydantic_v1.BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_fso_load_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    fso_vessel_id: Optional[ID] = None
    fso_vessel_name: Optional[str] = None
    to_vessel_id: Optional[ID] = None
    to_vessel_name: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoPortUnloadEvent(pydantic_v1.BaseModel):
    vessel_id: Optional[ID] = None
    event_type: Optional[Literal["cargo_port_unload_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    end_timestamp: Optional[ISODate] = None
    raw_locations: Optional[List[RawLocations]] = None
    pos: Optional[List[float]] = None
    start_timestamp: Optional[ISODate] = None
    restricted: Optional[bool] = False


class CargoFSOUnloadEvent(pydantic_v1.BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_fso_unload_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    fso_vessel_id: Optional[str] = None
    fso_vessel_name: Optional[str] = None
    from_vessel_id: Optional[str] = None
    from_vessel_name: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoFixtureEvent(pydantic_v1.BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_fixture_event"]] = None
    end_timestamp: Optional[ISODate] = None


class CargoSTSEvent(pydantic_v1.BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_sts_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    to_vessel_id: Optional[str] = None
    to_vessel_name: Optional[str] = None
    from_vessel_id: Optional[str] = None
    from_vessel_name: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoStorageEvent(pydantic_v1.BaseModel):
    vessel_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_storage_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    vessel_class: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoWaypointEvent(pydantic_v1.BaseModel):
    vessel_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_waypoint_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoTransitingEvent(pydantic_v1.BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_transiting_event"]] = None
    end_timestamp: Optional[ISODate] = None


class CargoOilOnWaterEvent(pydantic_v1.BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_oil_on_water_event"]] = None
    end_timestamp: Optional[ISODate] = None


class ParentID(pydantic_v1.BaseModel):
    """

    `cargo_movement_id` may change under certain conditions. `ParentID` contains an `id`,
    a previous id of the cargo movement, and a `splinter_timestamp`, the time at which the id change occurred.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    id: Optional[str] = None
    splinter_timestamp: Optional[ISODate] = None


class CargoMovementProductEntry(pydantic_v1.BaseModel):
    probability: Optional[float] = None
    source: Optional[str] = None
    id: Optional[ID] = None
    layer: Optional[str] = None
    label: Optional[str] = None


class CargoMovement(pydantic_v1.BaseModel):
    """

    Cargo movements are the base data set the Vortexa API is centred around.

    Each movement represents a journey of a certain quantity of a product between places.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    cargo_movement_id: ID
    quantity: Optional[int] = None
    status: Optional[str] = None
    vessels: Optional[List[VesselEntity]] = None
    product: Optional[List[CargoMovementProductEntry]] = None
    parent_ids: Optional[List[ParentID]] = None
    events: Optional[
        List[
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
                pydantic_v1.Field(discriminator="event_type"),
            ]
        ]
    ] = None
