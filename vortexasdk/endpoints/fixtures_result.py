from typing import List

import pandas as pd

from vortexasdk.api import Fixture
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


class FixtureResult(Result):
    """Container class that holds the result obtained from calling the `Fixtures` endpoint."""

    def to_list(self) -> List[Fixture]:
        """Represent Fixtures data as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), Fixture)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent Fixtures as a `pd.DataFrame`.

        # Arguments
            columns: The Fixtures columns we want in the dataframe. Enter `columns='all'` to include all columns.
            Defaults to `columns = ["id", "vessel", "laycan_from", "laycan_to", "tones", "fixing_timestamp", 'fulfilled', 'vtx_fulfilled', 'destination','origin', 'product', 'charterer']`.


        # Returns
        `pd.DataFrame` of Fixtures.
        """
        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="Fixtures",
        )


DEFAULT_COLUMNS = ["id", "vessel", "laycan_from", "laycan_to", "tones", "fixing_timestamp", 'fulfilled', 'vtx_fulfilled', 'destination', 'origin', 'product', 'charterer']
