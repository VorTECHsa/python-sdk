import functools
import os
from multiprocessing.pool import Pool
import pandas as pd
from typing import List, Optional
from pydantic import BaseModel
from vortexasdk.api.id import ID

from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = ["id", "value", "label"]


def sort_breakdown(item: dict, full_header_column: list):
    if "breakdown" not in item:
        return item
    for b_item in full_header_column:
        label = b_item["label"]
        if next((x for x in item["breakdown"] if x["label"] == label), None):
            continue

        item["breakdown"].append(
            {"label": label, "id": b_item["id"], "value": ""}
        )

    item["breakdown"].sort(
        key=lambda x: x["label"] if "label" in x is not None else ""
    )
    return item


class VoyagesBreakdownItem(BaseModel):
    """
    Generic container class holding a `id <> value` pair, a `label`.

    For example, this class could hold a number of vessels (`value`) in East Asia ('label') with id of "212fb4cfc862391f" (`id`) and the number of voyages in this location (count).

    If the `VoyagesBreakdownItem` is enriched by reference data (e.g. in `/voyages/cargo-origin`), `id` is the short ID of the reference entity, `label` holds its name
    and `value` correspond to numeric values of the returned record.
    """

    id: ID
    value: Optional[float] = None
    label: Optional[str] = None


class VoyagesBreakdown(VoyagesBreakdownItem):
    breakdown: Optional[List[VoyagesBreakdownItem]] = None


class VoyagesBreakdownResult(Result):
    """Container class that holds the result obtained from calling a top hits endpoint."""

    def to_list(self) -> List[VoyagesBreakdown]:
        """Represents breakdown as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VoyagesBreakdown)

    def to_df(self, columns="all") -> pd.DataFrame:
        """
        Converts the breakdown data into a pandas DataFrame.

        This method transforms breakdown data into a structured DataFrame, making it easier to analyze and manipulate. The DataFrame includes various columns representing different aspects of the breakdown, such as ids, values, and breakdowns.

        Parameters:
        - columns (str or list, optional): Specifies the columns to include in the output DataFrame.
            - If set to 'all' (default), all available columns are included.
            - If a list is provided, it should contain the column names to be included. For example:
            ['id', 'value', 'breakdown.0.label', 'breakdown.0.count', 'breakdown.0.value']
            This list can be customized to include specific breakdown indices (e.g., 'breakdown.1.label').

        Returns:
        - pd.DataFrame: A DataFrame containing the breakdown data. The DataFrame includes the following columns by default:
            - id (datetime): The breakdown key.
            - value (varies): The value associated with each key in the time series.
            - breakdown (dict): Additional aggregated information for each time interval.

        Notes:
        - The 'breakdown' column in the DataFrame provides aggregated data and can contain multiple entries. To access additional breakdown information, modify the column names in the 'columns' parameter (e.g., 'breakdown.1.label', 'breakdown.2.label').
        """
        flatten = functools.partial(convert_to_flat_dict, columns=columns)
        with Pool(os.cpu_count()) as pool:
            items = super().to_list()

            full_header_column: list = []
            # there is a world where we can just get items[-1], as it seems reasonable to thing the most recent one would have the most regions
            for item in items:
                if "breakdown" not in item:
                    continue
                if len(item["breakdown"]) > len(full_header_column):
                    full_header_column = item["breakdown"][:]
            sorted_list = map(
                lambda item: sort_breakdown(item, full_header_column), items
            )
            records = pool.map(flatten, sorted_list)

        df = create_dataframe(
            columns=columns,
            data=records,
            logger_description="VoyagesBreakdown",
        )

        return df
