from typing import List

import pandas as pd

from vortexasdk.api import Corporation
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = ["id", "name", "corporate_entity_type"]


class CorporationsResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""

    def to_list(self) -> List[Corporation]:
        """Represent vessels as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), Corporation)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent corporations as a `pd.DataFrame`.

        # Arguments
            columns: The corporation features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'corporate_entity_type']`.


        # Returns
        `pd.DataFrame` of corporations.

        """
        return create_dataframe(
            columns=columns,
            data=super().to_list(),
            logger_description="Corporations",
        )
