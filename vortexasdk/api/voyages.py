from pydantic import BaseModel, Field
from typing import List, Optional, Union
from typing_extensions import Literal
from vortexasdk.api.id import ID


from vortexasdk.api.shared_types import (
    EntityWithListLayer,
    EntityWithSingleLayer,
    EntityWithSingleLayerAndTimespan,
    Flag,
    ISODate,
    Scrubber,
    Tag,
)


class CongestionBreakdownItem(BaseModel):
    """

    Congestion breakdown shows various stats of vessels in congestion.

    """

    avg_waiting_time: Optional[int] = None
    vessel_dwt: Optional[int] = None
    vessel_cubic_capacity: Optional[int] = None
    vessel_count: Optional[int] = None
    cargo_quantity: Optional[int] = None
    avg_waiting_time_laden: Optional[int] = None
    vessel_dwt_laden: Optional[int] = None
    vessel_cubic_capacity_laden: Optional[int] = None
    vessel_count_laden: Optional[int] = None
    avg_waiting_time_ballast: Optional[int] = None
    vessel_dwt_ballast: Optional[int] = None
    vessel_cubic_capacity_ballast: Optional[int] = None
    vessel_count_ballast: Optional[int] = None
    location_details: List[EntityWithListLayer] = Field(default_factory=list)


class VoyagesVesselEntity(BaseModel):
    """
    A VoyagesVesselEntity represents a vessel record used in Voyages.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)
    """

    id: Optional[ID] = None
    name: Optional[str] = None
    dead_weight: Optional[int] = None
    vessel_class: Optional[str] = None
    imo: Optional[int] = None
    mmsi: Optional[int] = None
    call_sign: Optional[str] = None
    cubic_capacity: Optional[int] = None
    year: Optional[int] = None
    flag: List[Flag] = Field(default_factory=list)
    scrubber: List[Scrubber] = Field(default_factory=list)
    ice_class: Optional[str] = None
    propulsion: Optional[str] = None
    tags: List[Tag] = Field(default_factory=list)
    vessel_risk_level: Optional[str] = None


class VoyageVesselEvent(BaseModel):
    """
    A vessel event represents an activity that a vessel has performed during a voyage

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """

    event_id: Optional[str] = None
    event_group: Optional[str] = None
    event_type: Optional[str] = None
    location_id: Optional[str] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
    activity: Optional[str] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    location_layer: Optional[List[str]] = Field(default_factory=list)
    cargo_movement_id: Optional[List[str]] = None
    sts_event_counterparty_vessel_id: Optional[str] = None
    waiting_event_target_geography_id: Optional[str] = None
    fixture_event_fixing_timestamp: Optional[ISODate] = None
    tags: Optional[List[Tag]] = Field(default_factory=list)
    probability: Optional[int] = None
    location_details: Optional[List[EntityWithSingleLayer]] = Field(default_factory=list)
    is_open_event: Optional[bool] = None
    waiting_event_target_geography_details: Optional[
        List[EntityWithSingleLayer]
    ] = None


class VoyageCargoEvent(BaseModel):
    """
    Cargo events relate to the movement of cargo during the voyage.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """

    event_id: Optional[str] = None
    event_group: Literal["derived"]
    event_type: Optional[str] = None
    cargo_movement_id: Optional[str] = None
    cargo_origin_id: Optional[str] = None
    product_id: Optional[str] = None
    quantity_tonnes: Optional[int] = None
    quantity_barrels: Optional[int] = None
    quantity_cubic_metres: Optional[int] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
    activity: Optional[str] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    cargo_destination_id: Optional[str] = None
    tonne_miles: Optional[int] = None
    product_details: Optional[List[EntityWithSingleLayer]] = Field(default_factory=list)
    cargo_origin_details: Optional[List[EntityWithSingleLayer]] = Field(
        default_factory=list
    )
    cargo_destination_details: Optional[List[EntityWithSingleLayer]] = Field(
        default_factory=list
    )
    is_open_event: Optional[bool] = None


class VoyageStatusEvent(BaseModel):
    """
    Status events describe the status of the voyage at a given period.

    [Voyage Events Further Documentation](https://docs.vortexa.com/reference/intro-voyage-events)


    """

    event_id: Optional[str] = None
    event_group: Literal["derived"]
    event_type: Optional[str] = None
    activity: Optional[str] = None
    value: Optional[str] = None
    source_event_id: Optional[str] = None
    end_timestamp: Optional[ISODate] = None
    start_timestamp: Optional[ISODate] = None
    is_open_event: Optional[bool] = None


class VoyageEnrichedItem(BaseModel):
    """

    A voyage is defined as a continuous period of time when the vessel is either laden or ballast.

    Each voyage is made up of multiple voyage events which describe the activity of the vessel while it is laden or ballast.

    [Voyages Further Documentation](https://docs.vortexa.com/reference/intro-voyages)

    """

    schema_version: Optional[str] = None
    voyage_id: Optional[ID] = None
    start_event_id: Optional[ID] = None
    vessel_id: Optional[ID] = None
    vessel: Optional[VoyagesVesselEntity] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None
    end_event_id: Optional[ID] = None
    previous_voyage_id: Optional[ID] = None
    next_voyage_id: Optional[ID] = None
    latest_product_ids: Optional[List[ID]] = Field(default_factory=list)
    tags: Optional[List[Tag]] = Field(default_factory=list)
    tonne_miles: Optional[int] = None
    corporate_entities:Optional[List[EntityWithSingleLayerAndTimespan]] = Field(
        default_factory=list
    )
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    events: Optional[List[
        Optional[Union[VoyageVesselEvent, VoyageCargoEvent, VoyageStatusEvent]]
    ]] = Field(default_factory=list)
    latest_product_details: Optional[List[EntityWithSingleLayer]] = Field(
        default_factory=list
    )
