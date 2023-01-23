from datetime import datetime
from vortexasdk import ParentProductBreakdown

from tests.testcases import TestCaseUsingRealAPI


class TestParentProductBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 1, 1)

        result = ParentProductBreakdown().search(
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 4

    def test_search_returns_multiple_breakdowns(self):
        filter_time_min = datetime(2022, 11, 10)
        filter_time_max = datetime(2022, 11, 10)

        result = ParentProductBreakdown().search(
            filter_activity="loading_state",
            breakdown_unit="b",
            filter_time_min=filter_time_min,
            filter_time_max=filter_time_max,
            breakdown_size=100,
        )

        assert len(result) == 4

    def test_search_returns_any_activity(self):
        date = datetime(2019, 11, 10)

        result = ParentProductBreakdown().search(
            filter_activity="any_activity",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 4

    def test_search_returns_excluded_params(self):
        date = datetime(2019, 11, 10)
        rotterdam = (
            "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        )

        result = ParentProductBreakdown().search(
            filter_activity="any_activity",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
            exclude_origins=rotterdam,
        )

        assert len(result) == 4
