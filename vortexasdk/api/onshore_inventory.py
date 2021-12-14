from dataclasses import dataclass
from typing import Optional

from vortexasdk.api.asset_tank import AssetTank
from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID


@dataclass(frozen=True)
class OnshoreInventory(FromDictMixin):
    """

    Land Storage measurements are the base data set the Vortexa API is centred around.

    Each measurement represents the total capacity and current amount being stored at each location.

    [Land Storage Further Documentation](https://docs.vortexa.com/reference/intro-land-storage)

    """

    measurement_id: ID
    tank_id: ID
    tank_details: AssetTank
    measurement_timestamp: Optional[ISODate]
    publish_timestamp: Optional[ISODate]
    report_timestamp: ISODate
    carry_forward: bool
    fill_bbl: int
    fill_tons: float
    fill_cbm: float
    reference_data_version: str
