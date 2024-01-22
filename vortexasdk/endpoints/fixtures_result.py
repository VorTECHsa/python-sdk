import functools
import os
from multiprocessing import Pool
from typing import List

import pandas as pd

from vortexasdk.api import Fixture
from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger
from vortexasdk.result_conversions import create_dataframe, create_list

logger = get_logger(__name__)

DEFAULT_COLUMNS = [
    "id",
    "vessel.id",
    "vessel.name",
    "laycan_from",
    "laycan_to",
    "tones",
    "fixing_timestamp",
    "fulfilled",
    "vtx_fulfilled",
    "destination.label",
    "origin.label",
    "product.label",
    "charterer.label",
]


class FixtureResult(Result):
    """Container class that holds the result obtained from calling the `Fixtures` endpoint."""

    def to_list(self) -> List[Fixture]:
        """Represent Fixtures data as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), Fixture)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent Fixtures as a `pd.DataFrame`.

        # Arguments
            columns: The Fixtures columns we want in the dataframe.
            Defaults to `columns = [
                "id",
                'vessels.corporate_entities.charterer.id',
                'vessels.corporate_entities.charterer.label',
                'vessels.corporate_entities.charterer.layer',
                'vessels.corporate_entities.charterer.probability',
                'vessels.corporate_entities.charterer.source',
                'vessels.corporate_entities.effective_controller.id',
                'vessels.corporate_entities.effective_controller.label',
                'vessels.corporate_entities.effective_controller.layer',
                'vessels.corporate_entities.effective_controller.probability',
                'vessels.corporate_entities.effective_controller.source',
                'vessels.corporate_entities.time_charterer.end_timestamp',
                'vessels.corporate_entities.time_charterer.id',
                'vessels.corporate_entities.time_charterer.label',
                'vessels.corporate_entities.time_charterer.layer',
                'vessels.corporate_entities.time_charterer.probability',
                'vessels.corporate_entities.time_charterer.source',
                'vessels.corporate_entities.time_charterer.start_timestamp',
                'vessels.cubic_capacity',
                'vessels.dwt',
                'vessels.end_timestamp',
                'vessels.fixture_fulfilled',
                'vessels.fixture_id',
                'vessels.id',
                'vessels.imo',
                'vessels.mmsi',
                'vessels.name',
                'vessels.start_timestamp',
                'vessels.status',
                'vessels.tags.end_timestamp',
                'vessels.tags.start_timestamp',
                'vessels.tags.tag',
                'vessels.vessel_class',
                'vessels.voyage_id',
                "laycan_from",
                "laycan_to",
                "tones",
                "fixing_timestamp",
                "fulfilled",
                "vtx_fulfilled",
                "destination.label",
                "destination.id",
                "origin.label",
                "origin.id",
                "product.label",
                "product.id",
                "charterer.label",
                "charterer.id",
            ]`.

        A near complete list of columns is given below
        ```python
        [
            "id",
            "vessel.id",
            "vessel.name",
            "laycan_from",
            "laycan_to",
            "tones",
            "fixing_timestamp",
            "fulfilled",
            "vtx_fulfilled",
            "destination.label",
            "origin.label",
            "product.label",
            "charterer.label",
        ]
        ```

        # Returns
        `pd.DataFrame` of Fixtures.
        """

        flatten = functools.partial(convert_to_flat_dict, columns=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            data=records,
            logger_description="Fixtures",
        )
