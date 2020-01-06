import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.api.timeseries_item import TimeSeriesItem


class TimeSeriesResult(Result):
    """Container class that holds the result obtained from calling a time series endpoint."""

    def to_list(self) -> List[TimeSeriesItem]:
        """Represents time series as a list."""
        list_of_dicts = super().to_list()
        with Pool(os.cpu_count()) as pool:
            return list(pool.map(TimeSeriesItem.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
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
        return pd.DataFrame(data=super().to_list())
