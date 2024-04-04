from datetime import datetime, timedelta
from typing import Any, Dict

from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import CANAL_TRANSIT_TIME_SERIES
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search

logger = get_logger(__name__)


class CanalTransitTimeseries(Search):
    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CANAL_TRANSIT_TIME_SERIES)

    def search(
        self,
        time_min: datetime = datetime.now() - timedelta(days=2),
        time_max: datetime = datetime.now() + timedelta(days=2),
        timeseries_activity: str = "started_waiting",
        metric: str = "count_of_vessels",
        timeseries_frequency: str = "day",
    ) -> TimeSeriesResult:
        """

        Aggregate Canal Transit records for various activities and frequencies.

        # Arguments

            metric: Aggregation metric. Must be one of [`'count_of_vessels'`, `'minimum_waiting_time'`, `'maximum_waiting_time'`, `'average_waiting_time'`]

            time_min: The UTC date when `timeseries_activity` starts,

            time_max: The UTC date when `timeseries_activity` ends,

            timeseries_activity: Activity of the vessel we want to aggregate on. Must be one of [`'started_waiting'`, `'waiting'`, `'started_transiting'`, `'transiting'`, `'transited'`]

            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of [`'day'`, `'week'`]



        # Returns
        `CanalTransitTimeseries`

        """

        api_params: Dict[str, Any] = {
            "time_min": to_ISODate(time_min),
            "time_max": to_ISODate(time_max),
            "timeseries_activity": timeseries_activity,
            "metric": metric,
            "timeseries_frequency": timeseries_frequency,
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        response = super().search_with_client_with_search_after(**api_params)

        return TimeSeriesResult(
            records=response["data"], reference=response["reference"]
        )
