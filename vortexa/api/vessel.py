from dataclasses import dataclass
from typing import List, Optional

from vortexa.api.corporate import CorporateEntity

from vortexa.api.shared_types import Node, IDName, ID, ISODate, Tag


@dataclass(frozen=True, )
class Vessel(Node):
    """
    Represent a Vessel reference record returned by the API.

    # Further Documentation

    https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D
    """

    # identifiers
    related_names: List[str]
    mmsi: int
    call_sign: str

    # physical attributes
    to_bow: str
    to_stern: str
    to_port: str
    to_starboard: str
    cubic_capacity: int
    dead_weight: int

    tags: List[Tag]
    current_product_type: List

    vessel_class: str
    year: Optional[int]
    imo: Optional[int]
    gross_tonnage: Optional[int] = None


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

    vessel_class: str
    corporate_entities: List[CorporateEntity]
    tags: List[Tag]
    status: str

    start_timestamp: ISODate

    cubic_capacity: Optional[int] = None
    voyage_id: Optional[str] = None
    fixture_fulfilled: Optional[bool] = None
    end_timestamp: Optional[ISODate] = None
    fixture_id: Optional[str] = None
