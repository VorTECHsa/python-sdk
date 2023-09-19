from pydantic import BaseModel
from typing import List, Optional


from vortexasdk.api.shared_types import (
    EntityWithListLayer,
    ISODate,
    VesselClassEntry,
    Tag,
    Flag,
)


class DeclaredDestination(BaseModel):
    """

    Current destination location, as reported by the available vessel

    """

    eta: Optional[ISODate] = None
    name: Optional[str] = None
    vessel_id: Optional[str] = None


class VesselFixtures(BaseModel):
    """

    Current fixture information for the available vessel

    """

    origin: Optional[str] = None
    destination: Optional[str] = None
    charterer: Optional[str] = None
    fixing_timestamp: Optional[ISODate] = None
    laycan_from: Optional[ISODate] = None
    laycan_to: Optional[ISODate] = None


class VesselAvailability(BaseModel):
    """

    Vessel Availability shows vessels that are available to load a given cargo at a given port within a specified time range.

    """

    available_at: Optional[ISODate] = None
    evaluated_at: Optional[ISODate] = None
    vessel_class: Optional[str] = None
    vessel_class_hierarchy: Optional[List[VesselClassEntry]] = None
    vessel_declared_destination: Optional[List[DeclaredDestination]] = None
    vessel_dwt: Optional[int] = None
    vessel_cubic_capacity: Optional[int] = None
    vessel_fixtures: Optional[List[VesselFixtures]] = None
    vessel_id: Optional[str] = None
    vessel_imo: Optional[str] = None
    vessel_last_cargo: Optional[List[EntityWithListLayer]] = None
    vessel_location: Optional[List[EntityWithListLayer]] = None
    vessel_name: Optional[str] = None
    vessel_owner_id: Optional[str] = None
    vessel_owner_name: Optional[str] = None
    vessel_risk_level: Optional[str] = None
    vessel_predicted_destination: Optional[List[EntityWithListLayer]] = None
    vessel_scrubber: Optional[bool] = None
    vessel_status: Optional[str] = None
    vessel_year_built: Optional[int] = None
    last_activity_at: Optional[ISODate] = None
    last_activity: Optional[int] = None
    vessel_flags: Optional[List[Flag]] = None
    vessel_tags: Optional[List[Tag]] = None
    vessel_ice_class: Optional[str] = None
