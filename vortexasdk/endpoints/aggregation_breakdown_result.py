from typing import List
import pandas as pd

from vortexasdk.api.aggregation_breakdown_item import AggregationBreakdownItem
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = ["id", "value", "count", "label"]


class AggregationBreakdownResult(Result):
    """Container class that holds the result obtained from calling a top hits endpoint."""

    def to_list(self) -> List[AggregationBreakdownItem]:
        """Represents time series as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), AggregationBreakdownItem)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """Represents the aggregation breakdown as a dataframe.

        Returns a `pd.DataFrame`, of time series items with columns:
         id: ID of the reference record
         value: Value of the time series for a given ID
         count: Number of records contributing to this time series record.
         label: Label of the reference record.

        # Example:

        If we're aggregating top vessel origins, then the `id` column holds the ID of a location, the `label` holds the name of the location,
        the `value` column holds the number of voyages contributing to this aggregation record, and the `count` column holds
        the number of vessels.

        """
        df = create_dataframe(
            columns=columns,
            data=super().to_list(),
            logger_description="AggregationBreakdown",
        )

        return df
