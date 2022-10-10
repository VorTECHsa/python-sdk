from datetime import datetime
from vortexasdk import FleetUtilisationSpeedBreakdown

from tests.testcases import TestCaseUsingRealAPI


class TestFleetUtilisationSpeedBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = FleetUtilisationSpeedBreakdown().search(
            filter_activity="loading_state",
            breakdown_unit="kmh",
            filter_time_min=date,
            filter_time_max=date,
            breakdown_frequency="day",
        )

        assert len(result) == 1

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = FleetUtilisationSpeedBreakdown().search(
            filter_activity="loading_state",
            breakdown_unit="kmh",
            filter_time_min=start,
            filter_time_max=end,
            breakdown_frequency="day",
        )

        n_days = (end - start).days + 1

        assert n_days == len(result)

    def test_search_returns_for_mps(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = FleetUtilisationSpeedBreakdown().search(
            filter_activity="loading_state",
            breakdown_unit="mps",
            filter_time_min=start,
            filter_time_max=end,
            breakdown_frequency="day",
        )

        n_days = (end - start).days + 1

        assert n_days == len(result)

    def test_search_returns_default_freq(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 11, 10)

        result = FleetUtilisationSpeedBreakdown().search(
            filter_activity="loading_state",
            breakdown_unit="kmh",
            filter_time_min=start,
            filter_time_max=end,
        )

        n_months = (end.year - start.year) * 12 + end.month - start.month + 1

        assert n_months == len(result)

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            FleetUtilisationSpeedBreakdown()
            .search(
                filter_activity="loading_state",
                breakdown_unit="kmh",
                filter_time_min=start,
                filter_time_max=end,
                breakdown_frequency="day",
            )
            .to_df()
        )

        n_days = (end - start).days + 1

        assert len(df) == n_days
        assert list(df.columns) == [
            "key",
            "value",
            "count",
            "breakdown.0.label",
            "breakdown.0.count",
            "breakdown.0.value",
        ]

    def test_with_params(self):

        df = (
            FleetUtilisationSpeedBreakdown()
            .search(
                filter_vessel_status="vessel_status_laden_known",
                filter_origins="80aa9e4f3014c3d96559c8e642157edbb2b684ea0144ed76cd20b3af75110877",
                filter_destinations="934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2",
                filter_time_min=datetime(2020, 12, 19),
                filter_time_max=datetime(2021, 1, 18),
                breakdown_unit="kn",
                breakdown_frequency="week",
                breakdown_property="vessel_class",
            )
            .to_df()
            .head()
        )

        assert list(df.columns) == [
            "key",
            "value",
            "count",
            "breakdown.0.label",
            "breakdown.0.count",
            "breakdown.0.value",
        ]

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            FleetUtilisationSpeedBreakdown()
            .search(
                filter_activity="loading_state",
                breakdown_unit="kmh",
                filter_time_min=start,
                filter_time_max=end,
                breakdown_frequency="day",
            )
            .to_list()
        )

        n_days = (end - start).days + 1

        assert len(time_series_list) == n_days
