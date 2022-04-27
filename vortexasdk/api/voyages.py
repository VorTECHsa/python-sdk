from dataclasses import dataclass
from typing import List

from vortexasdk.api.serdes import FromDictMixin


@dataclass(frozen=True)
class LocationDetails:
    id: str
    label: str
    layer: List[str]


@dataclass(frozen=True)
class CongestionBreakdownItem(FromDictMixin):
    """

    Congestion breakdown shows various stats of vessels in congestion.

    """
    avg_waiting_time: int
    vessel_dwt: int
    vessel_cubic_capacity: int
    vessel_count: int
    cargo_quantity: int
    avg_waiting_time_laden: int
    vessel_dwt_laden: int
    vessel_cubic_capacity_laden: int
    vessel_count_laden: int
    avg_waiting_time_ballast: int
    vessel_dwt_ballast: int
    vessel_cubic_capacity_ballast: int
    vessel_count_ballast: int
    location_details: List[LocationDetails]
