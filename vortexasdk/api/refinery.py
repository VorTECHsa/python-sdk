from pydantic import BaseModel
from typing import List, Optional
from vortexasdk.api import ID
from vortexasdk.api.shared_types import Node


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
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    name: Optional[str] = None
    ports: Optional[List[RefineryPort]] = None
    refinery_operator_id: Optional[str] = None
    refinery_operator_name: Optional[str] = None
    refinery_owner_id: Optional[str] = None
    refinery_owner_name: Optional[str] = None
    refinery_type: Optional[str] = None
    shipping_region_name: Optional[str] = None
    status: Optional[str] = None
    ref_type: Optional[str] = None
