from typing import List
from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.breakdown_item import BreakdownItem
import pandas as pd
import functools
import os
from multiprocessing.pool import Pool

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

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `breakdown_result.DEFAULT_COLUMNS`.

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


        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            'key',
            'value',
            'count',
            'breakdown.0.label',
            'breakdown.0.count',
            'breakdown.0.value'
        ]
        ```

        Note that there can be more than one breakdown entry in the response. To access further
        breakdown objects, replace the index 0 with another number (1,2,3 etc.), such as
        ['breakdown.1.label', 'breakdown.2.label',  'breakdown.3.label] etc.'

        """

        if columns is None:
            columns = DEFAULT_COLUMNS

        logger.debug("Converting each breakdown to a flat dictionary")
        flatten = functools.partial(convert_to_flat_dict, cols=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="Breakdown",
        )

        df["key"] = pd.to_datetime(df["key"])

        return df


DEFAULT_COLUMNS = [
    "key",
    "value",
    "count",
    "breakdown.0.label",
    "breakdown.0.count",
    "breakdown.0.value",
]
