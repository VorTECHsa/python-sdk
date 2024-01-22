import functools
import os
from multiprocessing.pool import Pool
from typing import List
from vortexasdk.api.vessel_availability import VesselAvailability
import pandas as pd

from vortexasdk.api.entity_flattening import convert_to_flat_dict
from vortexasdk.api.search_result import Result
from vortexasdk.result_conversions import create_dataframe, create_list
from vortexasdk.logger import get_logger

logger = get_logger(__name__)

DEFAULT_COLUMNS = [
    "available_at",
    "vessel_name",
    "vessel_class",
    "vessel_declared_destination.0.eta",
    "vessel_declared_destination.0.name",
    "vessel_owner_name",
    "vessel_status",
    "vessel_last_cargo.0.label",
    "vessel_last_cargo.0.layer",
    "vessel_predicted_destination.0.label",
    "vessel_predicted_destination.0.layer",
]


class VesselAvailabilityResult(Result):
    """
    Container class holdings search results returns from the availability endpoint.

    Please note: you will require a subscription to our Freight module to access Vessel Availability.

    This class has two methods, `to_list()`, and `to_df()`, allowing search results to be represented as a list of `Availability`(ies),
     or as a `pd.DataFrame` , respectively.
    """

    def to_list(self) -> List[VesselAvailability]:
        """Represent availability as a list."""
        # noinspection PyTypeChecker
        return create_list(super().to_list(), VesselAvailability)

    def to_df(self, columns=DEFAULT_COLUMNS) -> pd.DataFrame:
        """
        Represent availability as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `vessel_availability_result.DEFAULT_COLUMNS`.

        # Returns
        `pd.DataFrame`, one row per `VesselAvailability`.


        ## Notes

        By default, the columns returned are something along the lines of.
        ```python
        DEFAULT_COLUMNS = [
            'available_at',
            'vessel_name',
            'vessel_class',
            'vessel_declared_destination.0.name'
            'vessel_declared_destination.0.eta',
            'vessel_owner_name',
            'vessel_status',
            'vessel_last_cargo.0.label',
            'vessel_last_cargo.0.layer',
            'vessel_predicted_destination.0.label',
            'vessel_predicted_destination.0.layer',

        ]
        ```
        The exact default columns used can be found at `vessel_availability_result.DEFAULT_COLUMNS`

        A near complete list of columns is given below
        ```
        [
            'available_at',
            'evaluated_at',
            'last_activity',
            'last_activity_at',
            'vessel_class',
            'vessel_declared_destination.0.name'
            'vessel_declared_destination.0.eta',
            'vessel_declared_destination.0.vessel_id',
            'vessel_dwt',
            'vessel_cubic_capacity',
            'vessel_fixtures.0.origin',
            'vessel_fixtures.0.destination',
            'vessel_fixtures.0.charterer',
            'vessel_fixtures.0.fixing_timestamp',
            'vessel_fixtures.0.laycan_to',
            'vessel_fixtures.0.laycan_from',
            'vessel_id',
            'vessel_imo',
            'vessel_last_cargo.0.id',
            'vessel_last_cargo.0.label',
            'vessel_last_cargo.0.layer',
            'vessel_last_cargo.1.id',
            'vessel_last_cargo.1.label',
            'vessel_last_cargo.1.layer',
            'vessel_last_cargo.2.id',
            'vessel_last_cargo.2.label',
            'vessel_last_cargo.2.layer',
            'vessel_last_cargo.3.id',
            'vessel_last_cargo.3.label',
            'vessel_last_cargo.3.layer',
            'vessel_location.0.id',
            'vessel_location.0.label',
            'vessel_location.0.layer',
            'vessel_location.1.id',
            'vessel_location.1.label',
            'vessel_location.1.layer',
            'vessel_location.2.id',
            'vessel_location.2.label',
            'vessel_location.2.layer',
            'vessel_location.3.id',
            'vessel_location.3.label',
            'vessel_location.3.layer',
            'vessel_location.4.id',
            'vessel_location.4.label',
            'vessel_location.4.layer',
            'vessel_location.5.id',
            'vessel_location.5.label',
            'vessel_location.5.layer',
            'vessel_location.6.id',
            'vessel_location.6.label',
            'vessel_location.6.layer',
            'vessel_location.7.id',
            'vessel_location.7.label',
            'vessel_location.7.layer',
            'vessel_location.8.id',
            'vessel_location.8.label',
            'vessel_location.8.layer',
            'vessel_location.9.id',
            'vessel_location.9.label',
            'vessel_location.9.layer',
            'vessel_location.10.id',
            'vessel_location.10.label',
            'vessel_location.10.layer',
            'vessel_location.11.id',
            'vessel_location.11.label',
            'vessel_location.11.layer',
            'vessel_location.12.id',
            'vessel_location.12.label',
            'vessel_location.12.layer',
            'vessel_location.13.id',
            'vessel_location.13.label',
            'vessel_location.13.layer',
            'vessel_name',
            'vessel_owner_id',
            'vessel_owner_name',
            'vessel_risk_level',
            'vessel_predicted_destination.0.id',
            'vessel_predicted_destination.0.label',
            'vessel_predicted_destination.0.layer',
            'vessel_predicted_destination.1.id',
            'vessel_predicted_destination.1.label',
            'vessel_predicted_destination.1.layer',
            'vessel_predicted_destination.2.id',
            'vessel_predicted_destination.2.label',
            'vessel_predicted_destination.2.layer',
            'vessel_predicted_destination.3.id',
            'vessel_predicted_destination.3.label',
            'vessel_predicted_destination.3.layer',
            'vessel_predicted_destination.4.id',
            'vessel_predicted_destination.4.label',
            'vessel_predicted_destination.4.layer',
            'vessel_predicted_destination.5.id',
            'vessel_predicted_destination.5.label',
            'vessel_predicted_destination.5.layer',
            'vessel_predicted_destination.6.id',
            'vessel_predicted_destination.6.label',
            'vessel_predicted_destination.6.layer',
            'vessel_predicted_destination.7.id',
            'vessel_predicted_destination.7.label',
            'vessel_predicted_destination.7.layer',
            'vessel_predicted_destination.8.id',
            'vessel_predicted_destination.8.label',
            'vessel_predicted_destination.8.layer',
            'vessel_predicted_destination.9.id',
            'vessel_predicted_destination.9.label',
            'vessel_predicted_destination.9.layer',
            'vessel_predicted_destination.10.id',
            'vessel_predicted_destination.10.label',
            'vessel_predicted_destination.10.layer',
            'vessel_predicted_destination.11.id',
            'vessel_predicted_destination.11.label',
            'vessel_predicted_destination.11.layer',
            'vessel_predicted_destination.12.id',
            'vessel_predicted_destination.12.label',
            'vessel_predicted_destination.12.layer',
            'vessel_predicted_destination.13.id',
            'vessel_predicted_destination.13.label',
            'vessel_predicted_destination.13.layer',
            'vessel_status',
            'vessel_year_built'
        ]
        ```

        """

        logger.debug(
            "Converting each Vessel Availability to a flat dictionary"
        )

        flatten = functools.partial(convert_to_flat_dict, columns=columns)

        with Pool(os.cpu_count()) as pool:
            records = pool.map(flatten, super().to_list())

        return create_dataframe(
            columns=columns,
            data=records,
            logger_description="VesselAvailability",
        )
