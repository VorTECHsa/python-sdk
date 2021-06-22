from datetime import datetime
from vortexasdk.endpoints.utilisation_timeseries_utilisation import UtilisationTimeseriesUtilisation

from tests.testcases import TestCaseUsingRealAPI

class TestUtilisationUtilisationTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            UtilisationTimeseriesUtilisation()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day",
                timeseries_property="quantity"
            )
            .to_list()
        )

        assert len(df) == 5
