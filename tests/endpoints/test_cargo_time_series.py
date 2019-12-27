from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.cargo_timeseries import CargoTimeSeries


class TestCargoTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2018, 10, 1)
        end = datetime(2019, 11, 1)

        df = (
            CargoTimeSeries()
                .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
            )
                .to_df()
        )

        n_days = (end - start).days + 1

        assert n_days == len(df)
