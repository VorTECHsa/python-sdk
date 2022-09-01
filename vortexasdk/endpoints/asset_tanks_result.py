from typing import List

import pandas as pd
from vortexasdk.api import AssetTank
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class AssetTankResult(Result):
    """Container class that holds the result obtained from calling the `Asset Tanks` endpoint."""

    def to_list(self) -> List[AssetTank]:
        """Represent asset tanks as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), AssetTank)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent asset tanks as a `pd.DataFrame`.

        # Arguments
            columns: The asset tanks features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'capacity_bbl', 'crude_confidence', 'location_id', 'name', 'storage_type', 'lat', 'lon']`.


        # Returns
        `pd.DataFrame` of asset tanks.

        """
        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="AssetTanks",
        )


DEFAULT_COLUMNS = [
    "id",
    "capacity_bbl",
    "crude_confidence",
    "location_id",
    "name",
    "storage_type",
    "lat",
    "lon",
]
