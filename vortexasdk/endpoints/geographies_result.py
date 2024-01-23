from typing import List
import pandas as pd

from vortexasdk.api import Geography
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


DEFAULT_COLUMNS = ["id", "name", "layer"]


class GeographyResult(Result):
    """Container class that holds the result obtained from calling the `Geography` endpoint."""

    def to_list(self) -> List[Geography]:
        """Represent geographies as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), Geography)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent geographies as a `pd.DataFrame`.

        # Arguments
            columns: The geography features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'layer']`.


        # Returns
        `pd.DataFrame` of geographies.

        """
        return create_dataframe(
            data=super().to_list(),
            columns=columns,
            logger_description="Geographies",
        )
