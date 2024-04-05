from datetime import datetime, timedelta
from typing import Any, Dict, List, Union
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
        time_min: datetime = datetime.now() - timedelta(days=2),
        time_max: datetime = datetime.now() + timedelta(days=2),
        timeseries_activity: str = "started_waiting",
        metric: str = "count_of_vessels",
        timeseries_frequency: str = "day",
        filter_vessel_cubic_capacity_min: int = None,
        filter_vessel_cubic_capacity_max: int = None,
        filter_vessel_dead_weight_min: int = None,
        filter_vessel_dead_weight_max: int = None,
        filter_canal: str = None,
        filter_direction: str = None,
        filter_lock: str = None,
        filter_queue_arrival_time_min: datetime = None,
        filter_queue_arrival_time_max: datetime = None,
        filter_canal_entry_time_min: datetime = None,
        filter_canal_entry_time_max: datetime = None,
        filter_canal_exit_time_min: datetime = None,
        filter_canal_exit_time_max: datetime = None,
        filter_booked_time_min: datetime = None,
        filter_booked_time_max: datetime = None,
        filter_booked_status: bool = None,
        filter_voyage_status: str = None,
        updated_since: datetime = datetime.now() - timedelta(days=2),
        exclude_filter_vessels: Union[ID, List[ID]] = None,
        exclude_filter_vessel_classes: Union[ID, List[ID]] = None,
        exclude_filter_products: Union[ID, List[ID]] = None,
        exclude_filter_origin: Union[ID, List[ID]] = None,
        exclude_filter_destination: Union[ID, List[ID]] = None,
        exclude_filter_charterer: Union[ID, List[ID]] = None,
        exclude_filter_effective_controller: Union[ID, List[ID]] = None,
    ) -> TimeSeriesResult:
        """

        Aggregate Canal Transit records for various activities and frequencies.

        # Arguments

            metric: Aggregation metric. Must be one of [`'count_of_vessels'`, `'minimum_waiting_time'`, `'maximum_waiting_time'`, `'average_waiting_time'`]

            time_min: The UTC date when `timeseries_activity` starts,

            time_max: The UTC date when `timeseries_activity` ends,

            timeseries_activity: Activity of the vessel we want to aggregate on. Must be one of [`'started_waiting'`, `'waiting'`, `'started_transiting'`, `'transiting'`, `'transited'`]

            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of [`'day'`, `'week'`]

            filter_vessel_cubic_capacity_min: Minimum cubic capacity of the vessel,

            filter_vessel_cubic_capacity_max: Maximum cubic capacity of the vessel,

            filter_vessel_dead_weight_min: Minimum DWT of the vessel,

            filter_vessel_dead_weight_max: Maximum DWT of the vessel,

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

            filter_booked_status: Boolean flat to filter vessels that booked their slots. Can be `'true'` or `'false'`,

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
            "filter_canal": filter_canal,
            "filter_direction": filter_direction,
            "filter_lock": filter_lock,
            "filter_booked_status": filter_booked_status,
            "filter_voyage_status": filter_voyage_status,
            "updated_since": to_ISODate(updated_since),
            "exclude": exclude_params,
        }

        response = super().search_with_client_with_search_after(**api_params)

        return TimeSeriesResult(
            records=response["data"], reference=response["reference"]
        )
