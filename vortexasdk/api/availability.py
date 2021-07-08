from dataclasses import dataclass
from typing import List, Optional

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import Entity, ISODate


@dataclass(frozen=True)
class DeclaredDestination:
    """

    A CargoEvent represents an event that occurred to a cargo during a cargo movement.

    [Cargo Event Entities Further Documentation](https://docs.vortexa.com/reference/intro-cargo-events)

    """
    eta: Optional[ISODate]
    name: str
    vessel_id: str

@dataclass(frozen=True)
class VesselFixtures:
    """

    A CargoEvent represents an event that occurred to a cargo during a cargo movement.

    [Cargo Event Entities Further Documentation](https://docs.vortexa.com/reference/intro-cargo-events)

    """
    origin: Optional[str]
    destination: Optional[str]
    charterer: Optional[str]
    fixing_timestamp: ISODate
    laycan_from: ISODate
    laycan_to: ISODate



@dataclass(frozen=True)
class VesselAvailability(FromDictMixin):
    """

    Cargo movements are the base data set the Vortexa API is centred around.

    Each movement represents a journey of a certain quantity of a product between places.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """
    available_at: ISODate
    evaluated_at: ISODate
    vessel_class: str
    vessel_declared_destination: List[DeclaredDestination]
    vessel_dwt: int
    vessel_fixtures: List[VesselFixtures]
    vessel_id: str
    vessel_last_cargo: List[Entity]
    vessel_location: List[Entity]
    vessel_name: Optional[str]
    vessel_owner_id: Optional[str]
    vessel_owner_name: Optional[str]
    vessel_predicted_destination: List[Entity]
    vessel_scrubber: Optional[bool]
    vessel_status: str
    vessel_year_built: Optional[int]
    last_activity_at: Optional[ISODate]
    last_activity: Optional[int]
