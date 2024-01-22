from typing import List

import pandas as pd

from vortexasdk.api import Attribute
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


DEFAULT_COLUMNS = ["id", "name", "type"]


class AttributeResult(Result):
    """Container class that holds the result obtained from calling the `Attributes` endpoint."""

    def to_list(self) -> List[Attribute]:
        """Represent attributes as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), Attribute)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent attributes as a `pd.DataFrame`.

        # Arguments
            columns: The attributes features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'type']`.


        # Returns
        `pd.DataFrame` of attributes.

        """
        return create_dataframe(
            columns=columns,
            data=super().to_list(),
            logger_description="Attributes",
        )
