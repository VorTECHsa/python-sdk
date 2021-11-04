from typing import List

import pandas as pd

from vortexasdk.api import StorageTerminal
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class StorageTerminalResult(Result):
    """Container class that holds the result obtained from calling the `Storage Terminals` endpoint."""

    def to_list(self) -> List[StorageTerminal]:
        """Represent storage terminals as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), StorageTerminal)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent storage terminals as a `pd.DataFrame`.

        # Arguments
            columns: The storage terminals features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'lat', 'lon']`.


        # Returns
        `pd.DataFrame` of storage terminals.

        """
        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="StorageTerminals",
        )


DEFAULT_COLUMNS = ["id", "name", "lat", "lon"]
