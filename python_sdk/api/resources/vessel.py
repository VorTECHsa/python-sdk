from dataclasses import dataclass
from enum import Enum
from typing import List

from python_sdk.api.resources.corporate import CorporateEntity


class VesselClass(Enum):
    tiny_tanker = 'tiny_tanker'
    general_purpose = 'general_purpose'
    handysize = 'handysize'
    handymax = 'handymax'
    panamax = 'panamax'
    aframax = 'aframax'
    suezmax = 'suezmax'
    vlcc_plus = 'vlcc_plus'
    sgc = 'sgc'
    mgc = 'mgc'
    lgc = 'lgc'
    vlgc = 'vlgc'


@dataclass
class VesselEntity:
    id: str
    mmsi: int
    imo: int
    name: str
    dwt: int
    cubic_capacity: int
    vessel_class: VesselClass
    corporate_entities: List[CorporateEntity]
    start_timestamp: str  # TODO(this shouldn't be a string)
    fixture_id: str
    fixture_fulfilled: bool
    voyage_id: str
    tags: List[str]
    status: str
