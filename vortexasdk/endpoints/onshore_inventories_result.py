import functools
import os
from multiprocessing.pool import Pool
from typing import List
from vortexasdk.api.onshore_inventory import OnshoreInventory

import pandas as pd

from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


DEFAULT_COLUMNS = [
    "measurement_id",
    "tank_id",
    "tank_details.capacity_bbl",
    "tank_details.capacity_cbm",
    "tank_details.capacity_ton",
    "tank_details.corporate_entity_details.id",
    "tank_details.corporate_entity_details.label",
    "tank_details.crude_confidence",
    "tank_details.location_id",
    "tank_details.name",
    "tank_details.pos",
    "tank_details.storage_terminal_id",
    "tank_details.storage_terminal_name",
    "tank_details.last_updated",
    "measurement_timestamp",
    "fill_bbl",
    "fill_tons",
    "fill_cbm",
]


class OnshoreInventoriesResult(Result):
    """
    Container class holdings search results returns from the crude onshore inventories endpoint.

    Please note: you will require a subscription to the Onshore Inventories API to access Crude Onshore Inventories.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `OnshoreInventories`,
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[OnshoreInventory]:
        """Represent availability as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), OnshoreInventory)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent onshore inventories as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `vessel_availability_result.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per `OnshoreInventory`.


        ## Notes

        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            measurement_id,
            tank_id,
            'tank_details.capacity_bbl',
            'tank_details.capacity_cbm',
            'tank_details.capacity_ton',
            'tank_details.corporate_entity_details.id',
            'tank_details.corporate_entity_details.label',
            'tank_details.crude_confidence',
            'tank_details.location_id',
            'tank_details.name',
            'tank_details.pos',
            'tank_details.storage_terminal_id',
            'tank_details.storage_terminal_name',
            'tank_details.last_updated',
            fill_bbl,
            fill_tons,
            fill_cbm,
        ]
        ```
        The exact default columns used can be found at `onshore_inventories_result.DEFAULT_COLUMNS`


        """

        logger.debug(
            "Converting Crude Onshore Inventories to a flat dictionary"
        )
        flatten = functools.partial(convert_to_flat_dict, columns=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            data=records,
            logger_description="OnshoreInventory",
        )
