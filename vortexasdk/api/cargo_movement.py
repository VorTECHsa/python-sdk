from pydantic import Field
from pydantic import BaseModel
from typing import List, Optional, Union
from typing_extensions import Annotated, Literal

from vortexasdk.api.geography import GeographyEntity
from vortexasdk.api.product import ProductEntityWithSingleLayer

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID
from vortexasdk.api.vessel import VesselEntity


class RawLocations(BaseModel):
    probability: float
    location_id: str


class CargoPortLoadEvent(BaseModel):
    vessel_id: ID
    start_timestamp: ISODate
    event_type: Literal["cargo_port_load_event"]
    location: List[GeographyEntity]
    probability: float
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoFSOLoadEvent(BaseModel):
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


class CargoPortUnloadEvent(BaseModel):
    vessel_id: ID
    event_type: Literal["cargo_port_unload_event"]
    location: List[GeographyEntity]
    probability: float
    end_timestamp: Optional[ISODate] = None
    raw_locations: Optional[List[RawLocations]] = None
    pos: Optional[List[float]] = None
    start_timestamp: Optional[ISODate] = None
    restricted: Optional[bool] = False


class CargoFSOUnloadEvent(BaseModel):
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


class CargoFixtureEvent(BaseModel):
    start_timestamp: ISODate
    event_type: Literal["cargo_fixture_event"]
    end_timestamp: Optional[ISODate] = None


class CargoSTSEvent(BaseModel):
    start_timestamp: ISODate
    event_type: Literal["cargo_sts_event"]
    location: List[GeographyEntity]
    to_vessel_id: str
    to_vessel_name: str
    from_vessel_id: str
    from_vessel_name: str
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoStorageEvent(BaseModel):
    vessel_id: ID
    start_timestamp: ISODate
    event_type: Literal["cargo_storage_event"]
    location: List[GeographyEntity]
    vessel_class: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoWaypointEvent(BaseModel):
    vessel_id: ID
    start_timestamp: ISODate
    event_type: Literal["cargo_waypoint_event"]
    location: List[GeographyEntity]
    probability: float
    end_timestamp: Optional[ISODate] = None
    pos: Optional[List[float]] = None


class CargoTransitingEvent(BaseModel):
    start_timestamp: ISODate
    event_type: Literal["cargo_transiting_event"]
    end_timestamp: Optional[ISODate] = None


class CargoOilOnWaterEvent(BaseModel):
    start_timestamp: ISODate
    event_type: Literal["cargo_oil_on_water_event"]
    end_timestamp: Optional[ISODate] = None


class ParentID(BaseModel):
    """

    `cargo_movement_id` may change under certain conditions. `ParentID` contains an `id`,
    a previous id of the cargo movement, and a `splinter_timestamp`, the time at which the id change occurred.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    id: str
    splinter_timestamp: ISODate


class CargoMovementProductEntry(BaseModel):
    probability: float
    source: str
    id: ID
    layer: Optional[str] = None
    label: Optional[str] = None


class CargoMovement(BaseModel):
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
