from pydantic import BaseModel
from typing import List, Optional
from vortexasdk.api import ID
from vortexasdk.api.shared_types import ISODate, Node


class RefineryPort(BaseModel):
    id: int
    import_export: Optional[str] = None
    port_id: Optional[str] = None
    port_name: Optional[str] = None
    refinery_id: Optional[str] = None
    terminal_id: Optional[str] = None
    terminal_name: Optional[str] = None


class Refinery(Node):
    """
    Represent a Refinery reference record returned by the API.

    [Refineries Further Documentation](https://docs.vortexa.com/reference/GET/reference/refineries)
    """

    id: ID
    country_name: Optional[str] = None
    current_capacity_kbd: Optional[int] = None
    end_date: Optional[ISODate] = None
    historical_peak_capacity_kbd: Optional[int] = None
    is_coastal: Optional[bool] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    ports: Optional[List[RefineryPort]] = None
    refinery_operator_id: Optional[str] = None
    refinery_operator_name: Optional[str] = None
    refinery_owner_id: Optional[str] = None
    refinery_owner_name: Optional[str] = None
    refinery_type: Optional[str] = None
    shipping_region_name: Optional[str] = None
    start_date: Optional[ISODate] = None
    status: Optional[str] = None
    storage_location_id: Optional[str] = None
    storage_location_name: Optional[str] = None
    ref_type: Optional[str] = None
