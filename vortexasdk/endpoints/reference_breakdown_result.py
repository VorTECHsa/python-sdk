from typing import List

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.api.breakdown_item import BreakdownItem
from vortexasdk.api.entity_flattening import convert_to_flat_dict
import functools
import os
from multiprocessing.pool import Pool

logger = get_logger(__name__)


def replace_keys(result: Result):
    # Creates a list of data entries with keys enriched by references
    if len(result) == 0:
        return list([])
    else:
        refs = result.reference
        data = result.records
        return list(map(lambda x: key_from_ref(x, refs), data))


def key_from_ref(datum, refs):
    # Reads the label from references and adds the label to the output
    key = datum["key"]
    if key in refs:
        name = refs[key]["label"]
        return {**datum, "label": name}
    else:
        name = datum["key"]
        return {**datum, "label": name}


class ReferenceBreakdownResult(Result):
    """Container class that holds the result obtained from calling a breakdown endpoint enriched with reference data."""

    def to_list(self) -> List[BreakdownItem]:
        """Represents time series as a list."""
        # data enrichment step - labels from `reference` enrich entries from `data`
        new_list = replace_keys(self)

        return create_list(new_list, BreakdownItem)

    def to_df(self, columns=None) -> pd.DataFrame:
        """Represents the breakdown as a dataframe.

        Returns a `pd.DataFrame`, of breakdown items with columns:
         key: id of the breakdown item
         label: name of the breakdown item
         value: The value of the breakdown for a given key
         count: The number of records contributing to this breakdown record.

        # Example:

        If we're aggregating origin breakdown by vessel count, then the `key` column holds the id of the country,
        the `label` holds the name of the country, the `value` column holds the number of unique vessels on that day,
        and the `count` column holds the number of vessels movements contributing towards this day's movements.

        """

        # data enrichment step - labels from `reference` replace keys from `data`
        new_list = replace_keys(self)

        if columns is None:
            columns = DEFAULT_COLUMNS

        logger.debug("Converting each breakdown to a flat dictionary")
        flatten = functools.partial(convert_to_flat_dict, cols=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, new_list)

        df = create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="ReferenceBreakdown",
        )

        return df


DEFAULT_COLUMNS = ["key", "label", "value", "count"]
