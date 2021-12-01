import functools
import os
from multiprocessing.pool import Pool
from typing import List
from vortexasdk.api.freight_pricing import FreightPricing
from vortexasdk.api.vessel_availability import VesselAvailability

import pandas as pd

from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class FreightPricingResult(Result):
    """
    Container class holdings search results returns from the freight pricing endpoint.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[FreightPricing]:
        """Represent availability as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), FreightPricing)

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent freight pricing as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `freight_pricing_result.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per `FreightPricing`.


        ## Notes

        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            'short_code',
            'rate'
            'rate_unit',
            'cost',
            'cost_unit',
            'tce',
            'tce_unit'
        ]
        ```
        The exact default columns used can be found at `vessel_availability_result.DEFAULT_COLUMNS`

        A near complete list of columns is given below
        ```
        [
            'id',
            'short_code',
            'rate'
            'rate_precision',
            'rate_unit',
            'cost',
            'cost_precision,
            'cost_unit',
            'tce',
            'tce_precision',
            'tce_unit',
            'source',
            'route_prediction'
        ]
        ```

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        logger.debug("Converting each Freight Pricing object to a flat dictionary")
        flatten = functools.partial(
            convert_to_flat_dict, cols=columns
        )

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=records,
            logger_description="FreightPricing",
        )


DEFAULT_COLUMNS = [
    'short_code',
    'rate'
    'rate_unit',
    'cost',
    'cost_unit',
    'tce',
    'tce_unit'
]
