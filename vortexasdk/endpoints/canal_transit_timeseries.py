from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union
from vortexasdk.api import ID


from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import CANAL_TRANSIT_TIME_SERIES
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.logger import get_logger
from vortexasdk.utils import convert_to_list
from vortexasdk.operations import Search

logger = get_logger(__name__)


class CanalTransitTimeseries(Search):
    def __init__(self):
        Search.__init__(self, CANAL_TRANSIT_TIME_SERIES)

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
        updated_since: Optional[datetime] = None,
        filter_canal: Optional[str] = None,
        filter_direction: Optional[str] = None,
        filter_lock: Optional[str] = None,
        time_min: datetime = datetime.now() - timedelta(days=2),
        time_max: datetime = datetime.now() + timedelta(days=2),
        timeseries_activity: str = "started_waiting",
        metric: str = "count_of_vessels",
        timeseries_frequency: str = "day",
        exclude_filter_vessels: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_vessel_classes: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_products: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_origin: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_destination: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_charterer: Optional[Union[ID, List[ID]]] = None,
        exclude_filter_effective_controller: Optional[
            Union[ID, List[ID]]
        ] = None,
    ) -> TimeSeriesResult:
        """

        Aggregate Canal Transit records for various activities and frequencies.

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

            filter_queue_arrival_time_min: The UTC date of when vessel arrived to the queue,

            filter_queue_arrival_time_max: The UTC date of when vessel arrived to the queue,

            filter_canal_entry_time_min: The UTC date of when vessel entered the canal,

            filter_canal_entry_time_max: The UTC date of when vessel entered the canal,

            filter_canal_exit_time_min: The UTC date of when vessel left the canal,

            filter_canal_exit_time_max: The UTC date of when vessel left the canal,

            filter_booked_time_min: The UTC date of planned time to enter the canal,

            filter_booked_time_max: The UTC date of planned time to enter the canal,

            filter_booked_status: Boolean to filter vessels that booked their slots before arrival. Can be `'true'` or `'false'`,

            filter_voyage_status: A voyage status, or list of voyage statuses to filter on. Can be one of: `'ballast'`, `'laden'`,

            updated_since: The UTC date of last update time of the record,

            filter_canal: Canal the vessel is queuing for. Must be one of [`'suez_canal'`, `'panama_canal'`],

            filter_direction: Direction that vessel is heading. Must be one of  [`'northbound'`, `'southbound'`],

            filter_lock: Route taken through the canal. For the Panama canal, it must be one of [`'panamax'`, `'neopanamax'`],

            time_min: The UTC date when `timeseries_activity` starts,

            time_max: The UTC date when `timeseries_activity` ends,

            timeseries_activity: Activity of the vessel we want to aggregate on. Must be one of [`'started_waiting'`, `'waiting'`, `'started_transiting'`, `'transiting'`, `'transited'`]

            metric: Aggregation metric. Must be one of [`'count_of_vessels'`, `'minimum_waiting_time'`, `'maximum_waiting_time'`, `'average_waiting_time'`]

            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of [`'day'`, `'week'`]

            exclude_filter_vessels: A vessel ID, or list of vessel IDs to exclude,

            exclude_filter_vessel_classes: A vessel class, or list of vessel classes to exclude,

            exclude_filter_products: A product ID, or list of product IDs to exclude,

            exclude_filter_origin: A geography ID, or list of geography IDs to exclude,

            exclude_filter_destination: A geography ID, or list of geography IDs to exclude,

            exclude_filter_charterer: A charterer ID, or list of charterer IDs to exclude,

            exclude_filter_effective_controller: A effective controller ID, or list of IDs to exclude,

        # Returns
        `CanalTransitTimeseries`

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
            "time_min": to_ISODate(time_min),
            "time_max": to_ISODate(time_max),
            "timeseries_activity": timeseries_activity,
            "metric": metric,
            "timeseries_frequency": timeseries_frequency,
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
            "updated_since": to_ISODate(updated_since)
            if updated_since
            else None,
            "exclude": exclude_params,
        }

        response = super().search_with_client_with_search_after(**api_params)

        return TimeSeriesResult(
            records=response["data"], reference=response["reference"]
        )
