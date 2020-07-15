import os
from typing import List

import pandas as pd

from vortexasdk.api import Geography
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class GeographyResult(Result):
    """Container class that holds the result obtained from calling the `Geography` endpoint."""

    def to_list(self) -> List[Geography]:
        """Represent geographies as a list."""
        list_of_dicts = super().to_list()

        logger.debug(f"Converting dictionary to Geographies using {os.cpu_count()} processes")
        return list(map(Geography.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent geographies as a `pd.DataFrame`.

        # Arguments
            columns: The geography features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'layer']`.


        # Returns
        `pd.DataFrame` of geographies.

        """
        logger.debug(f"Creating DataFrame of Geographies")

        if columns is None:
            columns = DEFAULT_COLUMNS

        if columns == "all":
            return pd.DataFrame(data=super().to_list())
        else:
            return pd.DataFrame(data=super().to_list(), columns=columns)


DEFAULT_COLUMNS = ["id", "name", "layer"]
