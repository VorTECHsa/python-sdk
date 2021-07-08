from typing import List
from vortexasdk.api.breakdown_item import BreakdownItem

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


class BreakdownResult(Result):
    """Container class that holds the result obtained from calling a breakdown endpoint."""

    def to_list(self) -> List[BreakdownItem]:
        """Represents time series as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), BreakdownItem)

    def to_df(self, columns=None) -> pd.DataFrame:
        """Represents the timeseries as a dataframe.

        Returns a `pd.DataFrame`, of time series items with columns:
         key: The breakdown key
         value: The value of the breakdown for a given key
         count: The number of records contributing to this time series record.
         breakdown: additional information about the aggregation.

        # Example:

        If we're aggregating average vessel speeds by day, then the `key` column holds the date,
        the `value` holds the average speed on the day, the `count` holds
        the number of vessel movements contributing towards this average, and breakdown
        provides further information about the aggregation.

        """
        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="Breakdown",
        )

        df["key"] = pd.to_datetime(df["key"])

        return df


DEFAULT_COLUMNS = ["key", "value", "count", "breakdown"]
