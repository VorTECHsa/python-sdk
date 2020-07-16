import os
from multiprocessing import Pool
from typing import List

import pandas as pd

from vortexasdk.logger import get_logger
from vortexasdk.api import Vessel
from vortexasdk.api.search_result import Result
from vortexasdk.create_dataframe import create_dataframe

logger = get_logger(__name__)


class VesselsResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""

    def to_list(self) -> List[Vessel]:
        """Represent vessels as a list."""
        list_of_dicts = super().to_list()

        with Pool(os.cpu_count()) as pool:
            logger.debug(
                f"Converting dictionary to Vessels using {os.cpu_count()} processes"
            )
            return list(pool.map(Vessel.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent vessels as a `pd.DataFrame`.

        # Arguments
            columns: The vessel features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'imo', 'vessel_class']`.


        # Returns
        `pd.DataFrame` of vessels.

        """
        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=super().to_list(),
            logger_description="Vessels",
        )


DEFAULT_COLUMNS = ["id", "name", "imo", "vessel_class"]
