"""Cargo Movements Endpoint."""
from typing import List, Union

from vortexasdk.conversions import convert_to_charterer_ids, convert_to_geography_ids, convert_to_product_ids
from vortexasdk.conversions.vessels import convert_to_vessel_ids
from vortexasdk.endpoints.cargo_movements_result import CargoMovementsResult
from vortexasdk.endpoints.endpoints import CARGO_MOVEMENTS_RESOURCE
from vortexasdk.operations import Search
from vortexasdk.utils import to_list


class CargoMovements(Search):
    """Cargo Movements Endpoint, use this to search through Vortexa's cargo movements."""

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_MOVEMENTS_RESOURCE)

    def search(self,
               filter_activity: str,
               filter_time_min: str = "2019-10-01T00:00:00.000Z",
               filter_time_max: str = "2019-10-01T01:00:00.000Z",
               cm_unit: str = 'b',

               filter_charterers: Union[str, List[str]] = None,
               filter_destinations: Union[str, List[str]] = None,
               filter_origins: Union[str, List[str]] = None,
               filter_owners: Union[str, List[str]] = None,
               filter_products: Union[str, List[str]] = None,
               filter_vessels: Union[str, List[str]] = None,
               filter_storage_locations: Union[str, List[str]] = None,
               filter_ship_to_ship_locations: Union[str, List[str]] = None,
               filter_waypoints: Union[str, List[str]] = None,
               disable_geographic_exclusion_rules: bool = None,
               ) -> CargoMovementsResult:
        """

        Find CargoMovements matching the given search parameters.

        # Arguments
            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'unloaded_state', 'storing_state', 'storing_start', 'storing_end', 'transiting_state',
               'any_state'].

            filter_time_min: The start date of the time filter.

            filter_time_max: The end date of the time filter.

            cm_unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_charterers: A charterer, or list of charterers to filter on.

            filter_destinations: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_origins: A geography, or list of geographies to filter on. Both geography names or IDs can be entered here.

            filter_owners: An owner, or list of owners to filter on. Both charterer/owner names or IDs can be entered here.

            filter_products: A product, or list of products to filter on. Both product names or IDs can be entered here.

            filter_vessels: A vessel, or list of vessels to filter on. Both vessel names or IDs can be entered here,

            filter_storage_locations: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            filter_ship_to_ship_locations: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            filter_waypoints: A geography, or list of geography to filter on. Both geography names or IDs can be entered here.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
        `CargoMovementsResult`, containing all the cargo movements matching the given search terms.


        # Example
        Let's search for all vessels that loaded from `Rotterdam [NL]` on the morning of 1st December 2018.

        ```python
        >>> from vortexasdk import CargoMovements
        >>> df = CargoMovements().search(
            filter_origins="Rotterdam",
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

        [Cargo Movements Endpoint Further Documentation](https://docs.vortexa.com/reference/POST/cargo-movements/search)


        """
        geog = lambda x: convert_to_geography_ids(to_list(x))
        charterer = lambda x: convert_to_charterer_ids(to_list(x))
        ves = lambda x: convert_to_vessel_ids(to_list(x))
        product = lambda x: convert_to_product_ids(to_list(x))

        params = {
            # Compulsory search parameters
            'filter_activity': filter_activity,
            'filter_time_min': filter_time_min,
            'filter_time_max': filter_time_max,
            'cm_unit': cm_unit,
            'size': self._MAX_PAGE_RESULT_SIZE,

            "filter_charterers": charterer(filter_charterers),
            "filter_destinations": geog(filter_destinations),
            "filter_origins": geog(filter_origins),
            "filter_owners": charterer(filter_owners),
            "filter_products": product(filter_products),
            "filter_vessels": ves(filter_vessels),
            "filter_storage_locations": geog(filter_storage_locations),
            "filter_ship_to_ship_locations": geog(filter_ship_to_ship_locations),
            "filter_waypoints": geog(filter_waypoints),
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules
        }

        return CargoMovementsResult(super().search(**params))
