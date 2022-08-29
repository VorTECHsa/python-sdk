from datetime import datetime
from vortexasdk import OriginBreakdown

from tests.testcases import TestCaseUsingRealAPI


class TestOriginBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = OriginBreakdown().search(
            filter_activity="loading_state",
            breakdown_geography="country",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 5

    def test_search_returns_multiple_breakdowns(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = OriginBreakdown().search(
            filter_activity="loading_state",
            breakdown_geography="country",
            breakdown_unit="b",
            filter_time_min=start,
            filter_time_max=end,
            breakdown_size=100,
        )

        assert len(result) == 100

    def test_search_returns_any_activity(self):
        date = datetime(2019, 11, 10)

        result = OriginBreakdown().search(
            filter_activity="any_activity",
            breakdown_geography="country",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 5

    def test_search_returns_excluded_params(self):
        date = datetime(2019, 11, 10)
        rotterdam = (
            "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        )

        result = OriginBreakdown().search(
            filter_activity="any_activity",
            breakdown_geography="country",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
            exclude_origins=rotterdam,
        )

        assert len(result) == 5

    def test_to_df(self):
        date = datetime(2019, 11, 10)

        df = (
            OriginBreakdown()
            .search(
                filter_activity="any_activity",
                breakdown_geography="country",
                breakdown_unit="b",
                filter_time_min=date,
                filter_time_max=date,
            )
            .to_df()
        )

        assert len(df) == 5
        assert list(df.columns) == ["key", "label", "value", "count"]

    def test_to_df_without_label(self):
        date = datetime(2019, 11, 10)

        df = (
            OriginBreakdown()
            .search(
                filter_activity="any_activity",
                breakdown_geography="country",
                breakdown_unit="b",
                filter_time_min=date,
                filter_time_max=date,
            )
            .to_df(columns=["key", "value", "count"])
        )

        assert len(df) == 5
        assert list(df.columns) == ["key", "value", "count"]

    def test_to_list(self):
        date = datetime(2019, 11, 10)

        time_series_list = (
            OriginBreakdown()
            .search(
                filter_activity="any_activity",
                breakdown_geography="country",
                breakdown_unit="b",
                filter_time_min=date,
                filter_time_max=date,
            )
            .to_list()
        )

        assert len(time_series_list) == 5

    def test_with_params(self):
        start = datetime(2019, 11, 10)
        end = datetime(2019, 11, 15)

        df = (
            OriginBreakdown()
            .search(
                filter_activity="loading_end",
                breakdown_geography="terminal",
                breakdown_unit="t",
                breakdown_size=5,
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        assert len(df) == 5
        assert list(df.columns) == ["key", "label", "value", "count"]
