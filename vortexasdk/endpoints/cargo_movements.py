"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fcargo_movements.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.cargo_movements_result import CargoMovementsResult
from vortexasdk.endpoints.endpoints import (
    CARGO_MOVEMENTS_RESOURCE,
    CARGO_MOVEMENT_RESOURCE,
)
from vortexasdk.logger import get_logger
from vortexasdk.operations import Record, Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class CargoMovements(Record, Search):
    """
    Cargo Movements Endpoint, use this to search through Vortexa's cargo movements.

    A detailed explanation of Cargo/Vessel Movements can be found [here](https://docs.vortexa.com/reference/intro-movement-difference).
    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Record.__init__(self, CARGO_MOVEMENT_RESOURCE)
        Search.__init__(self, CARGO_MOVEMENTS_RESOURCE)

    def search(
        self,
        filter_activity: str = None,
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        cm_unit: str = "b",
        filter_charterers: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_effective_controllers: Union[ID, List[ID]] = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_storage_locations: Union[ID, List[ID]] = None,
        filter_ship_to_ship_locations: Union[ID, List[ID]] = None,
        filter_waypoints: Union[ID, List[ID]] = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_vessel_flags: Union[ID, List[ID]] = None,
        filter_vessel_ice_class: Union[ID, List[ID]] = None,
        filter_vessel_propulsion: Union[ID, List[ID]] = None,
        exclude_origins: Union[ID, List[ID]] = None,
        exclude_destinations: Union[ID, List[ID]] = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[str, List[str]] = None,
        exclude_charterers: Union[ID, List[ID]] = None,
        exclude_owners: Union[ID, List[ID]] = None,
        exclude_effective_controllers: Union[ID, List[ID]] = None,
        exclude_vessel_flags: Union[ID, List[ID]] = None,
        exclude_vessel_ice_class: Union[ID, List[ID]] = None,
        exclude_vessel_propulsion: Union[ID, List[ID]] = None,
        disable_geographic_exclusion_rules: bool = None,
    ) -> CargoMovementsResult:
        """

        Find CargoMovements matching the given search parameters.

        # Arguments
            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'unloaded_state', 'storing_state', 'storing_start', 'storing_end', 'transiting_state',
               'any_activity', 'oil_on_water_state'].

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            cm_unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_charterers: A charterer ID, or list of charterer IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_storage_locations: A geography ID, or list of geography IDs to filter on.

            filter_ship_to_ship_locations: A geography ID, or list of geography IDs to filter on.

            filter_waypoints: A geography ID, or list of geography IDs to filter on.

            filter_vessel_age_min: A number between 1 and 100 (representing years).

            filter_vessel_age_max: A number between 1 and 100 (representing years).

            filter_vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

            filter_vessel_flags: A vessel flag, or list of vessel flags to filter on.

            filter_vessel_ice_class: An attribute ID, or list of attribute IDs to filter on.

            filter_vessel_propulsion: An attribute ID, or list of attribute IDs to filter on.

            exclude_origins: A geography ID, or list of geography IDs to exclude.

            exclude_destinations: A geography ID, or list of geography IDs to exclude.

            exclude_products: A product ID, or list of product IDs to exclude.

            exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

            exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

            exclude_charterers: A charterer ID, or list of charterer IDs to exclude.

            exclude_filter_effective_controllers: An effective controller ID, or list of effective controller IDs to exclude.

            exclude_vessel_flags: A geography ID, or list of geography IDs to exclude.

            exclude_vessel_ice_class: An attribute ID, or list of attribute IDs to exclude.

            exclude_vessel_propulsion: An attribute ID, or list of attribute IDs to exclude.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
        `CargoMovementsResult`, containing all the cargo movements matching the given search terms.


        # Example

        * _Which cargoes were loaded from Rotterdam on the morning of 1st December 2018?_


        ```python
        >>> from vortexasdk import CargoMovements, Geographies
        >>> rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        >>> search_result = CargoMovements().search(
        ...    filter_origins=rotterdam,
        ...    filter_activity='loading_state',
        ...    filter_time_min=datetime(2018, 12, 1),
        ...    filter_time_max=datetime(2018, 12, 1, 12))
        >>> df = search_result.to_df(columns=['product.grade.label', 'product.group.label', 'vessels.0.vessel_class'])

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

        * _Which VLCC cargoes passed through the Suez canal en route to China?_

        Note here we include vessels.0..., vessels.1..., vessels.2... columns.
        This lets us view all vessels present in any STS operations.

        ```python
        >>> from vortexasdk import CargoMovements, Geographies, Vessels
        >>> suez = [g.id for g in Geographies().search("suez").to_list()]
        >>> china = [g.id for g in Geographies().search("china").to_list() if "country" in g.layer]
        >>> vlccs = [v.id for v in Vessels().search(vessel_classes="vlcc_plus").to_list()]
        >>> cargo_movement_search_result = CargoMovements().search(
        ...    filter_destinations=china,
        ...    filter_activity="loading_state",
        ...    filter_waypoints=suez,
        ...    filter_vessels=vlccs,
        ...    filter_time_min=datetime(2018, 12, 1),
        ...    filter_time_max=datetime(2018, 12, 1))
        >>> cols = ['vessels.0.name', 'vessels.0.vessel_class', 'vessels.1.name', 'vessels.1.vessel_class',  'vessels.2.name', 'vessels.2.vessel_class', 'product.group.label', 'quantity']
        >>> cargo_movements_df = cargo_movement_search_result.to_df(columns=cols)

        ```

        |    | vessels.0.name   | vessels.0.vessel_class   | vessels.1.name   | vessels.1.vessel_class   | vessels.2.name   | vessels.2.vessel_class   | product.group.label   |   quantity |
        |---:|:-----------------|:-------------------------|:-----------------|:-------------------------|:-----------------|:-------------------------|:----------------------|-----------:|
        |  0 | MINERVA MARINA   | suezmax                  | COSGLORY LAKE    | vlcc_plus                | nan              | nan                      | Crude                 |     700614 |
        |  1 | BUKHA            | vlcc_plus                | nan              | nan                      | nan              | nan                      | Crude                 |    1896374 |
        |  2 | ATHENIAN FREEDOM | vlcc_plus                | nan              | nan                      | nan              | nan                      | Crude                 |     183537 |
        |  3 | ATINA            | suezmax                  | DONAT            | suezmax                  | DS VISION        | vlcc_plus                | Crude                 |     896773 |
        |  4 | MINERVA MARINA   | suezmax                  | COSGLORY LAKE    | vlcc_plus                | nan              | nan                      | Crude                 |     405724 |
        |  5 | MASAL            | suezmax                  | EKTA             | vlcc_plus                | nan              | nan                      | Crude                 |     997896 |
        |  6 | ATHENIAN FREEDOM | vlcc_plus                | nan              | nan                      | nan              | nan                      | Crude                 |     120812 |

        [Cargo Movements Endpoint Further Documentation](https://docs.vortexa.com/reference/POST/cargo-movements/search)

        """
        exclude_params: Dict[str, Any] = {
            "filter_origins": convert_to_list(exclude_origins),
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_owners": convert_to_list(exclude_owners),
            "filter_effective_controllers": convert_to_list(
                exclude_effective_controllers
            ),
            "filter_vessel_flags": convert_to_list(exclude_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                exclude_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                exclude_vessel_propulsion
            ),
        }

        api_params: Dict[str, Any] = {
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "cm_unit": cm_unit,
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_effective_controllers": convert_to_list(
                filter_effective_controllers
            ),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_storage_locations": convert_to_list(
                filter_storage_locations
            ),
            "filter_ship_to_ship_locations": convert_to_list(
                filter_ship_to_ship_locations
            ),
            "filter_waypoints": convert_to_list(filter_waypoints),
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "filter_vessel_flags": convert_to_list(filter_vessel_flags),
            "filter_vessel_ice_class": convert_to_list(
                filter_vessel_ice_class
            ),
            "filter_vessel_propulsion": convert_to_list(
                filter_vessel_propulsion
            ),
            "exclude": exclude_params,
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules,
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        response = super().search_with_client(**api_params)

        return CargoMovementsResult(
            records=response["data"], reference=response["reference"]
        )

    def record(self, id: ID, params: Dict = {}) -> Dict:
        """
        Perform a cargo movement lookup.

        # Arguments
            id: Cargo movement ID to lookup (long_id or short_id)

            params: Supported search params:
                'unit': enter 'b' for barrels, 't' for tonnes and 'cbm' for cubic meters

        # Returns
        Cargo movement record matching the ID

        # Further Documentation:
        [VortexaAPI Cargo Movement](https://docs.vortexa.com/reference/GET/cargo-movements/%7Bid%7D)

        """
        return super().record_with_params(id, params)
