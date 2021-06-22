from typing import List
from vortexasdk.api.breakdown_item import BreakdownItem

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

def key_from_ref(datum, refs):
    key = datum["key"]
    name = refs[key]["label"]
    return {**datum, "key": name}


class BreakdownResult(Result):
    """Container class that holds the result obtained from calling a time series endpoint."""

    def to_list(self) -> List[BreakdownItem]:
        """Represents time series as a list."""
        # noinspection PyTypeChecker
        refs = self["reference"]
        data = self["data"]

        new_list = list(map(lambda x: key_from_ref(x, refs), data))

        return create_list(new_list, BreakdownItem)

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
        
        refs = self["reference"]
        data = self["data"]

        new_list = list(map(lambda x: key_from_ref(x, refs), data))

        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=new_list,
            logger_description="Breakdown",
        )

        return df


DEFAULT_COLUMNS = ["key", "value", "count"]
