import functools
from multiprocessing.pool import Pool
import os
from typing import List

import pandas as pd

from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.api.timeseries_item import TimeSeriesItem
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


class TimeSeriesResult(Result):
    """Container class that holds the result obtained from calling a time series endpoint."""

    def to_list(self) -> List[TimeSeriesItem]:
        """Represents time series as a list."""
        return create_list(super().to_list(), TimeSeriesItem)

    def to_df(self, columns="all") -> pd.DataFrame:
        """
        Converts the time series data into a pandas DataFrame.

        This method transforms time series data into a structured DataFrame, making it easier to analyze and manipulate. The DataFrame includes various columns representing different aspects of the time series, such as keys, values, counts, and breakdowns.

        Parameters:
        - columns (str or list, optional): Specifies the columns to include in the output DataFrame.
            - If set to 'all' (default), all available columns are included.
            - If a list is provided, it should contain the column names to be included. For example:
            ['key', 'count', 'value', 'breakdown.0.label', 'breakdown.0.count', 'breakdown.0.value']
            This list can be customized to include specific breakdown indices (e.g., 'breakdown.1.label').

        Returns:
        - pd.DataFrame: A DataFrame containing the time series data. The DataFrame includes the following columns by default:
            - key (datetime): The breakdown key, converted to a datetime object.
            - value (varies): The value associated with each key in the time series.
            - count (int): The number of records contributing to each time series entry.
            - breakdown (dict): Additional aggregated information for each time interval.

        Notes:
        - The method utilizes multiprocessing to efficiently flatten the time series data into a DataFrame.
        - The 'breakdown' column in the DataFrame provides aggregated data and can contain multiple entries. To access additional breakdown information, modify the column names in the 'columns' parameter (e.g., 'breakdown.1.label', 'breakdown.2.label').

        Example:
        >>> time_series_data.to_df(columns=['key', 'value', 'count', 'breakdown.0.label', 'breakdown.0.count', 'breakdown.0.value'])
        # Returns a time series DataFrame with the top breakdown for each interval.
        """
        flatten = functools.partial(convert_to_flat_dict, columns=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        df = create_dataframe(
            columns=columns,
            data=records,
            logger_description="TimeSeries",
        )

        df["key"] = pd.to_datetime(df["key"])

        return df
