from typing import List
from vortexasdk.api.geo_breakdown_item import GeoBreakdownItem
from vortexasdk.api.breakdown_item import BreakdownItem

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

def replace_keys(result):
    """Creates a list of data entries with keys enriched by references"""
    refs = result["reference"]
    data = result["data"]
        
    return list(map(lambda x: key_from_ref(x, refs), data))

def key_from_ref(datum, refs):
    """Reads the label from references and replaces the key in the data with that label"""
    key = datum["key"]
    name = refs[key]["label"]
    return {**datum, "key": name}


class GeoBreakdownResult(Result):
    """Container class that holds the result obtained from calling a breakdown endpoint."""

    def to_list(self) -> List[GeoBreakdownItem]:
        """Represents time series as a list."""
        # noinspection PyTypeChecker

        # data enrichment step - labels from `reference` replace keys from `data`
        new_list = replace_keys(self)

        return create_list(new_list, GeoBreakdownItem)

    def to_df(self, columns=None) -> pd.DataFrame:
        """Represents the breakdown as a dataframe.

        Returns a `pd.DataFrame`, of breakdown items with columns:
         key: label of the breakdown item
         value: The value of the breakdown for a given key
         count: The number of records contributing to this breakdown record.

        # Example:

        If we're aggregating origin breakdown by vessel count, then the `key` column holds the name of the country,
        the `value` column holds the number of movements on that day, and the `count` column holds
        the number of vessels contributing towards this day's movements.

        """

        # data enrichment step - labels from `reference` replace keys from `data`
        new_list = replace_keys(self)

        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=new_list,
            logger_description="GeoBreakdown",
        )

        return df


DEFAULT_COLUMNS = ["key", "value", "count"]
