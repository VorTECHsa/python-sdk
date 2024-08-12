from pydantic import BaseModel
from typing import List, Optional

from vortexasdk.api.asset_tank import AssetTank

from vortexasdk.api.shared_types import ISODate
from vortexasdk.api.id import ID


class OnshoreInventory(BaseModel):
    """

    Land Storage measurements are the base data set the Vortexa API is centred around.

    Each measurement represents the total capacity and current amount being stored at each location.

    [Land Storage Further Documentation](https://docs.vortexa.com/reference/intro-land-storage)

    """

    measurement_id: Optional[ID] = None
    tank_id: Optional[ID] = None
    tank_details: Optional[AssetTank] = None
    measurement_timestamp: Optional[ISODate] = None
    publish_timestamp: Optional[ISODate] = None
    fill_bbl: Optional[int] = None
    fill_tons: Optional[float] = None
    fill_cbm: Optional[float] = None
    reference_data_version: Optional[str] = None
    latest_in_day: Optional[List[str]] = None
    latest_in_doe_week: Optional[List[str]] = None
    latest_in_month: Optional[List[str]] = None
    latest_in_quarter: Optional[List[str]] = None
    latest_in_week: Optional[List[str]] = None
    latest_in_year: Optional[List[str]] = None
