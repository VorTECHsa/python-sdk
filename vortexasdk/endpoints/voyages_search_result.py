import functools
import os
from multiprocessing.pool import Pool
from typing import List
from io import StringIO

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class VoyagesSearchResult(Result):
    """
    Container class holdings search results returned from the voyages endpoint.

    Please note: you will require a subscription to our Freight module to access Voyages.

    This class returns results 
    """

    def to_df(self) -> pd.DataFrame:
        """
        Represent voyages as a `pd.DataFrame`.

        # Returns
        `pd.DataFrame`, one row per `Voyage`.

        """

        logger.debug("Converting each Voyage to a dataframe")

        # https://stackoverflow.com/questions/22604564/create-pandas-dataframe-from-a-string
        # convertu utf-8 decoded CSV response to a text buffer
        buffer = StringIO(super().to_list()[0])

        # converts buffer to a datafrane
        df = pd.read_csv(buffer, sep=",")

        return df 