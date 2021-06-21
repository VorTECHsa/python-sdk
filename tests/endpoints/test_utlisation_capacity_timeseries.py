from datetime import datetime
from vortexasdk.endpoints.utilisation_timeseries_capacity import UtilisationTimeseriesCapacity

from tests.testcases import TestCaseUsingMockAPI

class TestUtilisationCapacityTimeSeries(TestCaseUsingMockAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            UtilisationTimeseriesCapacity()
            .search(
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        assert len(df) == 3
