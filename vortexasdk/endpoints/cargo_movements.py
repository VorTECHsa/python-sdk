"""Cargo Movements Endpoint."""
from typing import List

import jsons
import pandas as pd

from vortexasdk.api.cargo_movement import CargoMovement
from vortexasdk.api.entity_serializing import convert_cme_to_flat_dict
from vortexasdk.endpoints.endpoints import CARGO_MOVEMENTS_RESOURCE
from vortexasdk.operations import Search
from vortexasdk.api.search_result import Result

DEFAULT_COLUMNS = [
    'events.cargo_port_load_event.0.label',
    'events.cargo_port_unload_event.0.label',
    'product.group.label',
    'product.grade.label',
    'quantity',
    'vessels.0.name',
    'events.cargo_port_load_event.0.start_timestamp',
    'events.cargo_port_unload_event.0.start_timestamp',
]


class CargoMovementsResult(Result):
    """Container class holdings search results returns from the cargo movements endpoint."""

    def __init__(self, movements: List[dict]):
        deserialized = jsons.loads(jsons.dumps(movements), List[CargoMovement])
        super().__init__(deserialized)

    def to_list(self) -> List[CargoMovement]:
        """Represent cargo movements as a list of `CargoMovementEntity`s."""
        return super().to_list()

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent cargo movements as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter `columns=None` to use `cargo_movements.DEFAULT_COLUMNS`.


        # Returns
        `pd.DataFrame`, one row per cargo movement.

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        records = [convert_cme_to_flat_dict(cm, columns) for cm in self.to_list()]

        return pd.DataFrame(records)


class CargoMovements(Search):
    """Cargo Movements Endpoint."""

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_MOVEMENTS_RESOURCE)

    def search(self,
               filter_activity: str = "loading_state",
               filter_time_min: str = "2019-10-01T00:00:00.000Z",
               filter_time_max: str = "2019-10-01T01:00:00.000Z",
               include_definition: bool = True,
               cm_unit: str = 'b',

               filter_charterers: List[str] = None,
               filter_destinations: List[str] = None,
               filter_origins: List[str] = None,
               filter_owners: List[str] = None,
               filter_products: List[str] = None,
               filter_vessels: List[str] = None,
               filter_storage_locations: List[str] = None,
               filter_ship_to_ship_locations: List[str] = None,
               filter_waypoints: List[str] = None,
               disable_geographic_exclusion_rules: bool = None,
               ) -> CargoMovementsResult:
        """

        Find CargoMovements matching the given search parameters.

        # Arguments
            filter_activity: Movement activity on which to base the time filter. It can be a filter for a
             specific timestamp, which looks for it within the specified time-frame.

            filter_time_min: The start date of the time filter.

            filter_time_max: The end date of the time filter.

            include_definition: A list of grade or grade group identifiers to filter by.

            cm_unit:

            filter_charterers:

            filter_destinations: A list of geographical identifiers to apply to the destination filter.

            filter_origins: A list of geographical identifiers to apply to the origin filter.

            filter_owners:

            filter_products:

            filter_vessels: A list of vessel identifiers to filter by.

            filter_storage_locations:

            filter_ship_to_ship_locations:

            filter_waypoints: A list of geographical identifiers to apply to the waypoint filter.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
        List of cargo movements matching all the search parameters.


        # Example
        Let's search for all vessels that loaded from `Rotterdam [NL]` on the morning of 1st December 2018.

        ```python

        >>> df = CargoMovements().search(
            filter_origins=[g['id'] for g in Geographies().search("rotterdam") if 'port' in g['layer']],
            filter_activity='loading_state',
            filter_time_min="2018-12-01T00:00:00.000Z",
            filter_time_max="2018-12-01T12:00:00.000Z",
        ).to_df(columns=['product.grade.label', 'product.group.label', 'vessels.0.vessel_class', 'vessels'])
        ```

        |    | product.group.label   | product.grade.label             | vessels.0.vessel_class   |
        |---:|:----------------------|:--------------------------------|:-------------------------|
        |  0 | Clean products        | Pygas                           | general_purpose          |
        |  1 | Clean products        | Chemicals                       | tiny_tanker              |
        |  2 | Clean products        | Chemicals                       | tiny_tanker              |
        |  3 | Dirty products        | Low Sulphur VGO (LSVGO)         | general_purpose          |
        |  4 | Clean products        | ULSD (Ultra Low Sulphur Diesel) | general_purpose          |
        |  5 | Clean products        | Chemicals                       | tiny_tanker              |
        |  6 | Clean products        | Finished Gasoline               | handymax                 |

        """
        params = {
            # Compulsory search parameters
            'filter_activity': filter_activity,
            'filter_time_min': filter_time_min,
            'filter_time_max': filter_time_max,
            'include_definition': include_definition,
            'cm_unit': cm_unit,
            'size': self._MAX_PAGE_RESULT_SIZE,
            'cm_size': self._MAX_PAGE_RESULT_SIZE,
            # cm_size is used by the api https://docs.vortexa.com/reference/POST/cargo-movements/search

            "filter_charterers": filter_charterers,
            "filter_destinations": filter_destinations,
            "filter_origins": filter_origins,
            "filter_owners": filter_owners,
            "filter_products": filter_products,
            "filter_vessels": filter_vessels,
            "filter_storage_locations": filter_storage_locations,
            "filter_ship_to_ship_locations": filter_ship_to_ship_locations,
            "filter_waypoints": filter_waypoints,
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules
        }

        return CargoMovementsResult(super().search(**params))
