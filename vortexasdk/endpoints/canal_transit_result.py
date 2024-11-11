import functools
import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api import CanalTransitRecord
from vortexasdk.api.entity_flattening import (
    convert_to_flat_dict,
)
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = [
    "vessel_id",
    "vessel_name",
    "vessel_imo",
    "vessel_class.0.label",
    "vessel_cubic_capacity",
    "vessel_dead_weight",
    "booked",
    "canal",
    "direction",
    "lock",
    "queue_arrival_time",
    "canal_entry_time",
    "cargoes.0.product.label",
    "cargoes.0.quantity_barrels",
    "cargoes.0.quantity_tonnes",
    "cargoes.0.quantity_cubic_metres",
    "origin.0.label",
    "destination.0.label",
]


class CanalTransitResult(Result):

    """
    Container class holdings search results returns from the Canal transit endpoint.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `CanalTransitRecords`, or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[CanalTransitRecord]:
        """Represent canal transit records as a list of `CanalTransitRecord`s."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), CanalTransitRecord)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent canal transit record as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `canal_transit.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per canal transit record.

        """

        flatten = functools.partial(convert_to_flat_dict, columns=columns)
        logger.debug("Converting each CanalTransitRecord to a flat dictionary")

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            data=records,
            logger_description="CanalTransitRecords",
        )
