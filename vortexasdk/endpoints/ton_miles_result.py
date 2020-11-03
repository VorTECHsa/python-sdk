from typing import List

import pandas as pd

from vortexasdk.api.timeseries_item import TimeSeriesItem
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list


class TonMilesBreakdownResult(Result):
    """
    comment
    """

    def to_list(self) -> List[TimeSeriesItem]:
        """Represent (...) comment"""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), TimeSeriesItem)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        comment
        """

        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="TonMilesBreakdown",
        )

        df["key"] = pd.to_datetime(df["key"])

        return df


DEFAULT_COLUMNS = ["key", "value", "count"]
