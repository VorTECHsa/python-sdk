from pydantic import Field
from pydantic import BaseModel
from typing import List, Optional, Union
from typing_extensions import Annotated, Literal

from vortexasdk.api.geography import GeographyEntity

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


class RawLocations(BaseModel):
    probability: Optional[float] = None
    location_id: Optional[str] = None


class CargoPortLoadEvent(BaseModel):
    vessel_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_port_load_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoFSOLoadEvent(BaseModel):
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


class CargoPortUnloadEvent(BaseModel):
    vessel_id: Optional[ID] = None
    event_type: Optional[Literal["cargo_port_unload_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    end_timestamp: Optional[ISODate] = None
    raw_locations: Optional[List[RawLocations]] = None
    pos: Optional[List[float]] = None
    start_timestamp: Optional[ISODate] = None
    restricted: Optional[bool] = False


class CargoFSOUnloadEvent(BaseModel):
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


class CargoFixtureEvent(BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_fixture_event"]] = None
    end_timestamp: Optional[ISODate] = None


class CargoSTSEvent(BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_sts_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    to_vessel_id: Optional[str] = None
    to_vessel_name: Optional[str] = None
    from_vessel_id: Optional[str] = None
    from_vessel_name: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoStorageEvent(BaseModel):
    vessel_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_storage_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    vessel_class: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoWaypointEvent(BaseModel):
    vessel_id: Optional[ID] = None
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_waypoint_event"]] = None
    location: Optional[List[GeographyEntity]] = None
    probability: Optional[float] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoTransitingEvent(BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_transiting_event"]] = None
    end_timestamp: Optional[ISODate] = None


class CargoOilOnWaterEvent(BaseModel):
    start_timestamp: Optional[ISODate] = None
    event_type: Optional[Literal["cargo_oil_on_water_event"]] = None
    end_timestamp: Optional[ISODate] = None


class ParentID(BaseModel):
    """

    `cargo_movement_id` may change under certain conditions. `ParentID` contains an `id`,
    a previous id of the cargo movement, and a `splinter_timestamp`, the time at which the id change occurred.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    id: Optional[str] = None
    splinter_timestamp: Optional[ISODate] = None


class CargoMovementProductEntry(BaseModel):
    probability: Optional[float] = None
    source: Optional[str] = None
    id: Optional[ID] = None
    layer: Optional[str] = None
    label: Optional[str] = None


class CargoMovement(BaseModel):
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
                Field(discriminator="event_type"),
            ]
        ]
    ] = None
