from datetime import datetime
from vortexasdk.endpoints.utilisation_avg_distance_timeseries import UtilisationAvgDistanceTimeseries

from tests.testcases import TestCaseUsingRealAPI

class TestUtilisationAvgDistanceTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            UtilisationAvgDistanceTimeseries()
            .search(
                timeseries_unit="km",
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day"
            )
            .to_df()
        )

        assert len(df) == 5
