import functools
import os
from multiprocessing import Pool
from typing import List, Optional, Union
from typing_extensions import Literal

import pandas as pd

from vortexasdk.api.fixture import Fixture
from vortexasdk.api.entity_flattening import convert_fixture_to_flat_dict
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
    "tonnes",
    "fixing_timestamp",
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

    def to_df(
        self,
        columns: Optional[Union[List[str], Literal["all"]]] = DEFAULT_COLUMNS,
    ) -> pd.DataFrame:
        """
        Represent Fixtures as a `pd.DataFrame`.

        # Arguments
            columns: The Fixtures columns we want in the dataframe.
            Defaults to `columns = [
                "id",
                'vessel.corporate_entities.charterer.id',
                'vessel.corporate_entities.charterer.label',
                'vessel.corporate_entities.charterer.layer',
                'vessel.corporate_entities.charterer.probability',
                'vessel.corporate_entities.charterer.source',
                'vessel.corporate_entities.effective_controller.id',
                'vessel.corporate_entities.effective_controller.label',
                'vessel.corporate_entities.effective_controller.layer',
                'vessel.corporate_entities.effective_controller.probability',
                'vessel.corporate_entities.effective_controller.source',
                'vessel.corporate_entities.time_charterer.end_timestamp',
                'vessel.corporate_entities.time_charterer.id',
                'vessel.corporate_entities.time_charterer.label',
                'vessel.corporate_entities.time_charterer.layer',
                'vessel.corporate_entities.time_charterer.probability',
                'vessel.corporate_entities.time_charterer.source',
                'vessel.corporate_entities.time_charterer.start_timestamp',
                'vessel.cubic_capacity',
                'vessel.dwt',
                'vessel.end_timestamp',
                'vessel.id',
                'vessel.imo',
                'vessel.mmsi',
                'vessel.name',
                'vessel.start_timestamp',
                'vessel.status',
                'vessel.tags.end_timestamp',
                'vessel.tags.start_timestamp',
                'vessel.tags.tag',
                'vessel.vessel_class',
                'vessel.voyage_id',
                "laycan_from",
                "laycan_to",
                "tonnes",
                "fixing_timestamp",
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
            "tonnes",
            "fixing_timestamp",
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

        flatten = functools.partial(convert_fixture_to_flat_dict, columns=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            data=records,
            logger_description="Fixtures",
            columns=columns,
        )
