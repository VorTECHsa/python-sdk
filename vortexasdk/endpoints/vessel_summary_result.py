from typing import List, Optional, Union
from typing_extensions import Literal

import pandas as pd

from vortexasdk.logger import get_logger
from vortexasdk.api import VesselSummary
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


DEFAULT_COLUMNS = [
    "vessel_id",
    "timestamp",
    "lat",
    "lon",
    "speed",
    "draught",
    "declared_destination",
    "declared_eta",
]


class VesselSummaryResult(Result):
    """Container class that holds the result obtained from calling the `Vessel-Summary` endpoint."""

    def to_list(self) -> List[VesselSummary]:
        """Represent vessel summaries as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VesselSummary)

    def to_df(
        self,
        columns: Optional[Union[List[str], Literal["all"]]] = DEFAULT_COLUMNS,
    ) -> pd.DataFrame:
        """
        Represent vessel summaries as a `pd.DataFrame`.

        # Arguments
            columns: The vessel summaries we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['vessel_id', 'timestamp', 'lat', 'lon', 'speed', 'draught', 'declared_destination', 'declared_eta']`.

        # Returns
        `pd.DataFrame` of vessel summaries.

        """
        return create_dataframe(
            data=super().to_list(),
            logger_description="Vessel Summary",
            columns=columns,
        )
