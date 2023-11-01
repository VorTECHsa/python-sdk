			# "vessel_id": "000dc8b4d0ff3209",
			# "timestamp": "2023-10-27T14:06:39.000Z",
			# "lat": 25.44333333333333,
			# "lon": 129.67833333333334,
			# "speed": 11,
			# "draught": 9,
			# "declared_destination": "JPKZU > SGSIN",
			# "declared_eta": "2023-11-03T12:00:00.000Z"

from typing import List

import pandas as pd

from vortexasdk.logger import get_logger
from vortexasdk.api import VesselSummary
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


class VesselSummaryResult(Result):
    """Container class that holds the result obtained from calling the `Vessel-Summary` endpoint."""

    def to_list(self) -> List[VesselSummary]:
        """Represent vessels as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VesselSummary)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent vessels as a `pd.DataFrame`.

        # Arguments
            columns: The vessel features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['vessel_id', 'timestamp', 'lat', 'lon', 'speed', 'draught', 'declared_destination', 'decared_eta']`.


        # Returns
        `pd.DataFrame` of vessels.

        """
        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="Vessel Summary",
        )


DEFAULT_COLUMNS = ['vessel_id', 'timestamp', 'lat', 'lon', 'speed', 'draught', 'declared_destination', 'decared_eta']