import functools
import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd
from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.api.voyages import CongestionBreakdownItem
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class CongestionBreakdownResult(Result):
    """
    Container class holdings search results returns from the voyages congestion breakdown endpoint.

    Please note: you will require a subscription to our Freight module to access this endpoint.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `CongestionBreakdownResult`(ies),
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[CongestionBreakdownItem]:
        """Represent availability as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), CongestionBreakdownItem)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent availability as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `voyages_congestion_breakdown_result.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per `VesselAvailability`.


        ## Notes

        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            'avg_waiting_time',
            'vessel_dwt',
            'vessel_cubic_capacity',
            'vessel_count',
            'cargo_quantity',
            'avg_waiting_time_laden',
            'vessel_dwt_laden',
            'vessel_cubic_capacity_laden',
            'vessel_count_laden',
            'avg_waiting_time_ballast',
            'vessel_dwt_ballast',
            'vessel_cubic_capacity_ballast',
            'vessel_count_ballast',
            'location_details.0.label',
        ]
        ```
        The exact default columns used can be found at `voyages_congestion_breakdown_result.DEFAULT_COLUMNS`

        A near complete list of columns is given below
        ```
        [
            'avg_waiting_time',
            'vessel_dwt',
            'vessel_cubic_capacity',
            'vessel_count',
            'cargo_quantity',
            'avg_waiting_time_laden',
            'vessel_dwt_laden',
            'vessel_cubic_capacity_laden',
            'vessel_count_laden',
            'avg_waiting_time_ballast',
            'vessel_dwt_ballast',
            'vessel_cubic_capacity_ballast',
            'vessel_count_ballast',
            'location_details.0.label',
            'location_details.0.id',
            'location_details.0.layer.0'
            'location_details.0.layer.1'
            'location_details.0.layer.2',
            'location_details.1.label',
            'location_details.1.id',
            'location_details.1.layer.0'
            'location_details.1.layer.1'
            'location_details.1.layer.2'
        ]
        ```

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        logger.debug(
            "Converting each Voyage Congestion Breakdown to a flat dictionary"
        )
        flatten = functools.partial(convert_to_flat_dict, cols=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="VoyagesCongestionBreakdown",
        )


DEFAULT_COLUMNS = [
    "avg_waiting_time",
    "vessel_dwt",
    "vessel_cubic_capacity",
    "vessel_count",
    "cargo_quantity",
    "avg_waiting_time_laden",
    "vessel_dwt_laden",
    "vessel_cubic_capacity_laden",
    "vessel_count_laden",
    "avg_waiting_time_ballast",
    "vessel_dwt_ballast",
    "vessel_cubic_capacity_ballast",
    "vessel_count_ballast",
    "location_details.0.label",
]
