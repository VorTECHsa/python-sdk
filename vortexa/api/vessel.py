from dataclasses import dataclass
from typing import List, Optional

from vortexa.api.corporate import CorporateEntity

from vortexa.api.shared_types import Node, IDName, ID, ISODate, Tag


@dataclass(frozen=True)
class Vessel(Node):
    """
    Represent a Vessel reference record returned by the API.

    # Further Documentation

    https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D
    """

    # identifiers
    related_names: List[str]
    mmsi: int
    imo: int
    call_sign: str
    year: int

    # physical attributes
    to_bow: str
    to_stern: str
    to_port: str
    to_starboard: str
    cubic_capacity: int
    dead_weight: int
    gross_tonnage: int

    tags: List[Tag]
    current_product_type: List


@dataclass(frozen=True)
class VesselEntity(IDName):
    """

    A VesselEntity represents a vessel record used in CargoMovements and VesselMovements.

    [Vessel Entities Further Documentation](https://docs.vortexa.com/reference/intro-vessel-entities)

    """

    id: ID
    name: str
    mmsi: int
    imo: Optional[int]

    dwt: int
    cubic_capacity: Optional[int]

    vessel_class: str
    corporate_entities: List[CorporateEntity]
    tags: List[Tag]
    status: str

    voyage_id: Optional[str]
    fixture_fulfilled: Optional[bool]
    start_timestamp: ISODate
    end_timestamp: Optional[ISODate]
    fixture_id: Optional[str]
