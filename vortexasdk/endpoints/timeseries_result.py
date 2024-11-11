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

DEFAULT_COLUMNS = ["key", "value", "count"]


def sort_breakdown(item: dict, full_header_column: list):
    if "breakdown" not in item:
        return item

    breakdown_labels = [x["label"] for x in item["breakdown"]]
    header_items = {b_item["label"]: b_item for b_item in full_header_column}
    labels_to_append = set(header_items.keys()) - set(breakdown_labels)
    for label in labels_to_append:
        item["breakdown"].append(
            {
                "label": label,
                "id": header_items[label]["id"],
                "value": "",
                "count": "",
            }
        )

    item["breakdown"].sort(
        key=lambda x: x["label"] if "label" in x is not None else ""
    )
    return item


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
        - The 'breakdown' column in the DataFrame provides aggregated data and can contain multiple entries. To access additional breakdown information, modify the column names in the 'columns' parameter (e.g., 'breakdown.1.label', 'breakdown.2.label').
        """
        items = super().to_list()
        full_header_column: list = []
        # there is a world where we can just get items[-1], as it seems reasonable to thing the most recent one would have the most regions
        for item in items:
            if "breakdown" not in item:
                continue
            if len(item["breakdown"]) > len(full_header_column):
                full_header_column = item["breakdown"][:]
        sorted_list = map(
            lambda item: sort_breakdown(item, full_header_column), items
        )

        flatten = functools.partial(convert_to_flat_dict, columns=columns)
        cpu_count = os.cpu_count()
        if cpu_count is None or cpu_count > 1:
            with Pool(os.cpu_count()) as pool:
                records = pool.map(flatten, sorted_list)
        else:
            records = [flatten(v) for v in sorted_list]

        df = create_dataframe(
            columns=columns,
            data=records,
            logger_description="TimeSeries",
        )

        if "key" in df.columns:
            df["key"] = pd.to_datetime(df["key"])

        return df
