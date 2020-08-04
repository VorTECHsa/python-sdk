import functools
import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from api.vessel_diversion import VesselDiversion
from vortexasdk.api import CargoMovement
from vortexasdk.api.entity_flattening import (
    convert_cargo_movement_to_flat_dict,
)
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class VesselDiversionsResult(Result):
    """
    Container class holdings search results returns from the cargo movements endpoint.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `CargoMovements`,
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[VesselDiversion]:
        """Represent cargo movements as a list of `CargoMovementEntity`s."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VesselDiversion)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent cargo movements as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `cargo_movements.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per cargo movement.


        ## Notes


        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        flatten = functools.partial(
            convert_cargo_movement_to_flat_dict, cols=columns
        )

        logger.debug("Converting each CargoMovement to a flat dictionary")
        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="CargoMovements",
        )


DEFAULT_COLUMNS = [
    "events.cargo_port_load_event.0.location.port.label",
    "events.cargo_port_unload_event.0.location.port.label",
    "product.group.label",
    "product.grade.label",
    "quantity",
    "vessels.0.name",
    "events.cargo_port_load_event.0.end_timestamp",
    "events.cargo_port_unload_event.0.start_timestamp",
]
