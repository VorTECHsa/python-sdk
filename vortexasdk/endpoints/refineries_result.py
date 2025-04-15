from typing import List, Optional, Union
from typing_extensions import Literal

import pandas as pd

from vortexasdk.logger import get_logger
from vortexasdk.api import Refinery
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = ["id", "name", "status", "country_name"]


class RefineriesResult(Result):
    """Container class that holds the result obtained from calling the `Results` endpoint."""

    def to_list(self) -> List[Refinery]:
        """Represent refineries as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), Refinery)

    def to_df(
        self,
        columns: Optional[Union[List[str], Literal["all"]]] = DEFAULT_COLUMNS,
    ) -> pd.DataFrame:
        """
        Represent refineries as a `pd.DataFrame`.

        # Arguments
            columns: The refinery features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'status', 'country_name']`.


        # Returns
        `pd.DataFrame` of refineries.

        """
        return create_dataframe(
            data=super().to_list(),
            logger_description="Refineries",
            columns=columns,
        )
