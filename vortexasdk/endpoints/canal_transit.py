"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fcanal_transit.ipynb)
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.canal_transit_result import CanalTransitResult
from vortexasdk.endpoints.endpoints import CANAL_TRANSIT_SEARCH
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class CanalTransit(Search):
    """
    Canal Transit Endpoint, use this to search through Vortexa's canal transit records.

    A detailed explanation of what Canal Transit is can be found [here](https://docs.vortexa.com/reference/intro-canal-transit).
    """

    def __init__(self):
        Search.__init__(self, CANAL_TRANSIT_SEARCH)

    def search(
        self,
        filter_vessel_cubic_capacity_min: Optional[int] = None,
        filter_vessel_cubic_capacity_max: Optional[int] = None,
        filter_vessel_dead_weight_min: Optional[int] = None,
        filter_vessel_dead_weight_max: Optional[int] = None,
        filter_vessel_classes: Optional[Union[ID, List[ID]]] = None,
        filter_vessels: Optional[Union[ID, List[ID]]] = None,
        filter_products: Optional[Union[ID, List[ID]]] = None,
        filter_origin: Optional[Union[ID, List[ID]]] = None,
        filter_destination: Optional[Union[ID, List[ID]]] = None,
        filter_charterer: Optional[Union[ID, List[ID]]] = None,
        filter_effective_controller: Optional[Union[ID, List[ID]]] = None,
        filter_queue_arrival_time_min: Optional[datetime] = None,
        filter_queue_arrival_time_max: Optional[datetime] = None,
        filter_canal_entry_time_min: Optional[datetime] = None,
        filter_canal_entry_time_max: Optional[datetime] = None,
        filter_canal_exit_time_min: Optional[datetime] = None,
        filter_canal_exit_time_max: Optional[datetime] = None,
        filter_booked_time_min: Optional[datetime] = None,
        filter_booked_time_max: Optional[datetime] = None,
        filter_booked_status: Optional[bool] = None,
        filter_voyage_status: Optional[str] = None,
        updated_since: datetime = datetime.now() - timedelta(days=2),
        filter_canal: Optional[str] = None,
        filter_direction: Optional[str] = None,
        filter_lock: Optional[str] = None,
        exclude_filter_vessels: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_vessel_classes: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_products: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_origin: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_destination: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_charterer: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_effective_controller: Optional[
            Union[ID, List[ID]]
        ] = None,
    ) -> CanalTransitResult:
        """

        Find CanalTransitRecords matching the given search parameters.

        # Arguments

            filter_vessel_cubic_capacity_min: Minimum cubic capacity of the vessel,

            filter_vessel_cubic_capacity_max: Maximum cubic capacity of the vessel,

            filter_vessel_dead_weight_min: Minimum DWT of the vessel,

            filter_vessel_dead_weight_max: Maximum DWT of the vessel,

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_origin: A geography ID, or list of geography IDs to filter on.

            filter_destination: A geography ID, or list of geography IDs to filter on.

            filter_charterer: An charterer ID, or list of charterer IDs to filter on.

            filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

            filter_canal: Canal the vessel is queuing for. Must be one of [`'suez_canal'`, `'panama_canal'`],

            filter_direction: Direction that vessel is heading. Must be one of  [`'northbound'`, `'southbound'`],

            filter_lock: Route taken through the canal. For the Panama canal, it must be one of [`'panamax'`, `'neopanamax'`],

            filter_queue_arrival_time_min: The UTC date of when vessel arrived to the queue,

            filter_queue_arrival_time_max: The UTC date of when vessel arrived to the queue,

            filter_canal_entry_time_min: The UTC date of when vessel entered the canal,

            filter_canal_entry_time_max: The UTC date of when vessel entered the canal,

            filter_canal_exit_time_min: The UTC date of when vessel left the canal,

            filter_canal_exit_time_max: The UTC date of when vessel left the canal,

            filter_booked_time_min: The UTC date of planned time to enter the canal,

            filter_booked_time_max: The UTC date of planned time to enter the canal,

            filter_booked_status: Boolean to filter vessels that booked their slots. Can be `'true'` or `'false'`,

            filter_voyage_status: A voyage status, or list of voyage statuses to filter on. Can be one of: `'ballast'`, `'laden'`,

            updated_since: The UTC date of last record update time,

            exclude_filter_vessels: A vessel ID, or list of vessel IDs to exclude,

            exclude_filter_vessel_classes: A vessel class, or list of vessel classes to exclude,

            exclude_filter_products: A product ID, or list of product IDs to exclude,

            exclude_filter_origin: A geography ID, or list of geography IDs to exclude,

            exclude_filter_destination: A geography ID, or list of geography IDs to exclude,

            exclude_filter_charterer: A charterer ID, or list of charterer IDs to exclude,

            exclude_filter_effective_controller: A effective controller ID, or list of IDs to exclude,

        # Returns
        `CanalTransitResults`, containing all the canal transit records matching the given search terms.

        """

        exclude_params: Dict[str, Any] = {
            "filter_origin": convert_to_list(exclude_filter_origin),
            "filter_destination": convert_to_list(exclude_filter_destination),
            "filter_products": convert_to_list(exclude_filter_products),
            "filter_vessels": convert_to_list(exclude_filter_vessels),
            "filter_vessel_classes": convert_to_list(
                exclude_filter_vessel_classes
            ),
            "filter_charterers": convert_to_list(exclude_filter_charterer),
            "filter_effective_controllers": convert_to_list(
                exclude_filter_effective_controller
            ),
        }

        api_params: Dict[str, Any] = {
            "filter_booked_time_max": to_ISODate(filter_booked_time_max)
            if filter_booked_time_max
            else None,
            "filter_booked_time_min": to_ISODate(filter_booked_time_min)
            if filter_booked_time_min
            else None,
            "filter_canal_entry_time_max": to_ISODate(
                filter_canal_entry_time_max
            )
            if filter_canal_entry_time_max
            else None,
            "filter_canal_entry_time_min": to_ISODate(
                filter_canal_entry_time_min
            )
            if filter_canal_entry_time_min
            else None,
            "filter_canal_exit_time_max": to_ISODate(
                filter_canal_exit_time_max
            )
            if filter_canal_exit_time_max
            else None,
            "filter_canal_exit_time_min": to_ISODate(
                filter_canal_exit_time_min
            )
            if filter_canal_exit_time_min
            else None,
            "filter_queue_arrival_time_max": to_ISODate(
                filter_queue_arrival_time_max
            )
            if filter_queue_arrival_time_max
            else None,
            "filter_queue_arrival_time_min": to_ISODate(
                filter_queue_arrival_time_min
            )
            if filter_queue_arrival_time_min
            else None,
            "filter_vessel_cubic_capacity_max": filter_vessel_cubic_capacity_max,
            "filter_vessel_cubic_capacity_min": filter_vessel_cubic_capacity_min,
            "filter_vessel_dead_weight_max": filter_vessel_dead_weight_max,
            "filter_vessel_dead_weight_min": filter_vessel_dead_weight_min,
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_products": convert_to_list(filter_products),
            "filter_origin": convert_to_list(filter_origin),
            "filter_destination": convert_to_list(filter_destination),
            "filter_charterer": convert_to_list(filter_charterer),
            "filter_effective_controller": convert_to_list(
                filter_effective_controller
            ),
            "filter_canal": filter_canal,
            "filter_direction": filter_direction,
            "filter_lock": filter_lock,
            "filter_booked_status": filter_booked_status,
            "filter_voyage_status": filter_voyage_status,
            "updated_since": to_ISODate(updated_since),
            "exclude": exclude_params,
        }

        response = super().search_with_client(**api_params)

        return CanalTransitResult(
            records=response["data"], reference=response["reference"]
        )
