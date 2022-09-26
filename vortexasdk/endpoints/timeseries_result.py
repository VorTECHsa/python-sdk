import functools
import os
from multiprocessing import Pool
from typing import List

import pandas as pd
from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.api.timeseries_item import TimeSeriesItem
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = ["key", "value", "count"]


class TimeSeriesResult(Result):
    """Container class that holds the result obtained from calling a time series endpoint."""

    def to_list(self) -> List[TimeSeriesItem]:
        """Represents time series as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), TimeSeriesItem)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """Represents the timeseries as a dataframe.

        Returns a `pd.DataFrame`, of time series items with columns:
         key: The time series key
         value: The value of the time series for a given key
         count: The number of records contributing to this time series record.

        # Example:

        If we're aggregating Crude exports in tonnes by day, then the `key` column holds the date,
        the `value` column holds the Crude exports on that day, and the `count` column holds
        the number of cargo movements contributing towards this day's tonnage.

        """

        logger.debug("Converting each breakdown to a flat dictionary")
        flatten = functools.partial(convert_to_flat_dict, cols=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="TimeSeries",
        )

        df["key"] = pd.to_datetime(df["key"])

        return df
