from typing import List

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.api.voyages import VoyageEnrichedItem
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_list

logger = get_logger(__name__)


class VoyagesSearchEnrichedFlattenedResult(Result):
    """
    Container class holdings search results returned from the voyages endpoint.

    This class has a `to_df()` method, allowing search results to be represented as a `pd.DataFrame`.
    """

    def to_list(self) -> List[VoyageEnrichedItem]:
        # noinspection PyTypeChecker
        raise Exception(
            f"to_list method is not supported for search results in the flattened format (i.e. when the `columns` API param is provided). Please use to_df() instead."
        )

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent voyages as a `pd.DataFrame`.

        # Returns
        `pd.DataFrame`, one row per `Voyage`.

        """

        logger.debug("Converting Voyage CSV response to a dataframe")

        # converts list to a datafrane
        return pd.DataFrame(data=super().to_list())


class VoyagesSearchEnrichedListResult(Result):
    """
    Container class holdings search results returned from the voyages endpoint.

    This class has a `to_list()` method, allowing search results to be represented as a raw JSON response.
    """

    def to_list(self) -> List[VoyageEnrichedItem]:
        """Represent voyages as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VoyageEnrichedItem)

    def to_df(self, columns=None) -> pd.DataFrame:
        # noinspection PyTypeChecker
        raise Exception(
            f"to_df method is not supported for search results in the list format (i.e. when the `columns` API param is not provided). Please use to_list() instead."
        )
