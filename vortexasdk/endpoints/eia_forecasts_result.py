from typing import List

import pandas as pd

from vortexasdk.api import EIAForecast
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)


class EIAForecastResult(Result):
    """Container class that holds the result obtained from calling the `EIAForecasts` endpoint."""

    def to_list(self) -> List[EIAForecast]:
        """Represent EIAForecast data as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), EIAForecast)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent EIA forecasts as a `pd.DataFrame`.

        # Arguments
            columns: The EIA forecasts columns we want in the dataframe. Enter `columns='all'` to include all columns.
            Defaults to `columns = ['date', 'forecast_fri', 'value', 'stocks', 'cover', 'runs']`.


        # Returns
        `pd.DataFrame` of EIA forecasts.
        """
        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="EIAForecasts",
        )


DEFAULT_COLUMNS = ["date", "forecast_fri", "value", "stocks", "cover", "runs"]
