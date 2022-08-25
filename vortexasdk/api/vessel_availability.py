from pydantic import BaseModel
from typing import List, Optional


from vortexasdk.api.shared_types import EntityWithListLayer, ISODate


class DeclaredDestination(BaseModel):
    """

    Current destination location, as reported by the available vessel

    """

    eta: Optional[ISODate]
    name: str
    vessel_id: str


class VesselFixtures(BaseModel):
    """

    Current fixture information for the available vessel

    """

    origin: Optional[str]
    destination: Optional[str]
    charterer: Optional[str]
    fixing_timestamp: ISODate
    laycan_from: ISODate
    laycan_to: ISODate


class VesselAvailability(BaseModel):
    """

    Vessel Availability shows vessels that are available to load a given cargo at a given port within a specified time range.

    """

    available_at: ISODate
    evaluated_at: ISODate
    vessel_class: str
    vessel_declared_destination: List[DeclaredDestination]
    vessel_dwt: int
    vessel_fixtures: List[VesselFixtures]
    vessel_id: str
    vessel_last_cargo: List[EntityWithListLayer]
    vessel_location: List[EntityWithListLayer]
    vessel_name: Optional[str]
    vessel_owner_id: Optional[str]
    vessel_owner_name: Optional[str]
    vessel_predicted_destination: List[EntityWithListLayer]
    vessel_scrubber: Optional[bool]
    vessel_status: str
    vessel_year_built: Optional[int]
    last_activity_at: Optional[ISODate]
    last_activity: Optional[int]
