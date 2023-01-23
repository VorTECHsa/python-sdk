from datetime import datetime
from vortexasdk import MovementStatusBreakdown

from tests.testcases import TestCaseUsingRealAPI


class TestMovementStatusBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 1, 1)

        result = MovementStatusBreakdown().search(
            timestamp=date,
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 5

    def test_search_returns_multiple_breakdowns(self):
        filter_time_min = datetime(2022, 11, 10)
        filter_time_max = datetime(2022, 11, 10)
        timestamp = datetime(2022, 11, 10)

        result = MovementStatusBreakdown().search(
            filter_activity="loading_state",
            timestamp=timestamp,
            breakdown_unit="b",
            filter_time_min=filter_time_min,
            filter_time_max=filter_time_max,
            breakdown_size=100,
        )

        assert len(result) == 6

    def test_search_returns_any_activity(self):
        date = datetime(2019, 11, 10)

        result = MovementStatusBreakdown().search(
            filter_activity="any_activity",
            timestamp=date,
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

        result = MovementStatusBreakdown().search(
            filter_activity="any_activity",
            timestamp=date,
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
            exclude_origins=rotterdam,
        )

        assert len(result) == 5
