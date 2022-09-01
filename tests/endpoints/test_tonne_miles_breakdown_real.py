from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import TonneMilesBreakdown


class TestTonneMilesBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = TonneMilesBreakdown().search(
            filter_activity="loading_state",
            filter_time_min=date,
            filter_time_max=date,
            breakdown_frequency="day",
        )

        assert len(result) == 1

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = TonneMilesBreakdown().search(
            filter_activity="loading_state",
            filter_time_min=start,
            filter_time_max=end,
            breakdown_frequency="day",
        )

        n_days = (end - start).days + 1

        assert n_days == len(result)

    def test_search_returns_default_freq(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 11, 10)

        result = TonneMilesBreakdown().search(
            filter_activity="loading_state",
            filter_time_min=start,
            filter_time_max=end,
        )

        n_months = (end.year - start.year) * 12 + end.month - start.month + 1

        assert n_months == len(result)

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            TonneMilesBreakdown()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
                breakdown_frequency="day",
            )
            .to_df()
        )

        n_days = (end - start).days + 1

        assert len(df) == n_days
        assert list(df.columns) == ["key", "value", "count"]

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            TonneMilesBreakdown()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
                breakdown_frequency="day",
            )
            .to_list()
        )

        n_days = (end - start).days + 1

        assert len(time_series_list) == n_days
