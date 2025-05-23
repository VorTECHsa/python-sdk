from typing import List, Optional, Union
from typing_extensions import Literal

import pandas as pd

from vortexasdk.logger import get_logger
from vortexasdk.api import VesselPositions
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


DEFAULT_COLUMNS = ["vessel_id", "timestamp", "lat", "lon", "speed", "heading"]


class VesselPositionsResult(Result):
    """Container class that holds the result obtained from calling the `Vessel-Positions` endpoint."""

    def to_list(self) -> List[VesselPositions]:
        """Represent vessel positions as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VesselPositions)

    def to_df(
        self,
        columns: Optional[Union[List[str], Literal["all"]]] = DEFAULT_COLUMNS,
    ) -> pd.DataFrame:
        """
        Represent vessel positions as a `pd.DataFrame`.

        # Arguments
            columns: The vessel positions we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['vessel_id', 'timestamp', 'lat', 'lon', 'speed', 'heading']`.

        # Returns
        `pd.DataFrame` of vessel positions.

        """
        return create_dataframe(
            data=super().to_list(),
            logger_description="Vessel Positions",
            columns=columns,
        )
