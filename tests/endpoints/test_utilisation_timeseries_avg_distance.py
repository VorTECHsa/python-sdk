from datetime import datetime
from vortexasdk.endpoints.utilisation_timeseries_avg_distance import UtilisationTimeseriesAvgDistance

from tests.testcases import TestCaseUsingMockAPI

class TestUtilisationCapacityTimeSeries(TestCaseUsingMockAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            UtilisationTimeseriesAvgDistance()
            .search(
                timeseries_unit="km",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        assert len(df) == 3
