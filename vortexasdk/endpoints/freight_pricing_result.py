import functools
import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.freight_pricing import FreightPricing
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = [
    "short_code",
    "record_date",
    "rate",
    "rate_unit",
    "cost",
    "cost_unit",
    "tce",
    "tce_unit",
    "predictions.outlook_1d.prediction",
    "predictions.outlook_1d.rating",
]


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

    @staticmethod
    def format_prediction_outlooks(records: List):
        """
        This method formats the freight_pricing records to replace a list of predictions
        with a dictionary where each key is the prediction outlook.

        We do this so that when the freight pricing object is flattened to be consumed in a dataframe,
        the column names are predictable, without having list indices in the column name.
        `predictions.0.prediction` will become `predictions.outlook_1d.prediction`
        This also means specific outlooks can be passed in the `columns` argument to the `to_df()` method.

        E.G.
        Input:
        {
            predictions: [
                {
                    prediction_type: "outlook_1d",
                    prediction: "firm",
                    rating: "medium"
                },
                {
                    prediction_type: "outlook_4d",
                    prediction: "firm",
                    rating: "low"
                }
            ]
        }

        Output:
        {
            predictions: {
                outlook_1d: {
                    prediction: "firm",
                    rating: "medium",
                    prediction_type: "outlook_1d"
                },
                outlook_4d: {
                    prediction: "firm",
                    rating: "low",
                    prediction_type: "outlook_4d"
                }
            }
        }

        """
        formatted_records = []

        for record in records:
            formatted_predictions = None
            new_record = {}

            if record["predictions"]:
                formatted_predictions = {}

                for fp_prediction in record["predictions"]:
                    formatted_predictions[fp_prediction["prediction_type"]] = {
                        **fp_prediction
                    }

            new_record = {
                **record,
                "predictions": formatted_predictions,
            }

            formatted_records.append(new_record)

        return formatted_records

    def to_df(self, columns="all") -> pd.DataFrame:
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
            'record_date',
            'rate',
            'rate_unit',
            'cost',
            'cost_unit',
            'tce',
            'tce_unit',
            'predictions.outlook_1d.prediction',
            'predictions.outlook_1d.rating',
        ]
        ```
        The exact default columns used can be found at `freight_pricing.DEFAULT_COLUMNS`

        A near complete list of columns is given below
        ```
        [
            'id',
            'short_code',
            'rate',
            'rate_precision',
            'rate_unit',
            'cost',
            'cost_precision,
            'cost_unit',
            'tce',
            'tce_precision',
            'tce_unit',
            'record_date',
            'predictions.outlook_1d.prediction',
            'predictions.outlook_1d.rating',
            'predictions.outlook_2d.prediction',
            'predictions.outlook_2d.rating',
            'predictions.outlook_3d.prediction',
            'predictions.outlook_3d.rating',
            'predictions.outlook_4d.prediction',
            'predictions.outlook_4d.rating',
        ]
        ```

        """

        logger.debug(
            "Converting each Freight Pricing object to a flat dictionary"
        )
        flatten = functools.partial(convert_to_flat_dict, columns=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(
                flatten, self.format_prediction_outlooks(super().to_list())
            )

        return create_dataframe(
            columns=columns,
            data=records,
            logger_description="FreightPricing",
        )
