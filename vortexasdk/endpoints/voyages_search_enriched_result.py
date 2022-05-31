from typing import List

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.api.voyages import VoyageEnrichedItem
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class VoyagesSearchEnrichedResult(Result):
    """
    Container class holdings search results returned from the voyages endpoint.

    Please note: you will require a subscription to our Freight module to access Voyages.

    This class has a `to_df()` method, allowing search results to be represented as a `pd.DataFrame`.
    """

    def to_list(self) -> List[VoyageEnrichedItem]:
        """Represent voyages as a list."""
        # noinspection PyTypeChecker
        raise Exception(f"to_list method is not supported")

    def to_df(self) -> pd.DataFrame:
        """
        Represent voyages as a `pd.DataFrame`.

        # Returns
        `pd.DataFrame`, one row per `Voyage`.

        """

        logger.debug("Converting Voyage CSV response to a dataframe")

        # converts list to a datafrane
        return pd.DataFrame(data=super().to_list())
