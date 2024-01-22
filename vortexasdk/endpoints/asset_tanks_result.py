from typing import List

from vortexasdk.api import AssetTank
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

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


class AssetTankResult(Result):
    """Container class that holds the result obtained from calling the `Asset Tanks` endpoint."""

    def to_list(self) -> List[AssetTank]:
        """Represent asset tanks as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), AssetTank)

    def to_df(self, columns=DEFAULT_COLUMNS):
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
            data=super().to_list(),
            logger_description="AssetTanks",
        )
