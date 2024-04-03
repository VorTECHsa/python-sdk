from datetime import datetime
from vortexasdk import VesselClassBreakdown

from tests.testcases import TestCaseUsingRealAPI

totalVesselClassBreakdown = 27


class TestVesselClassBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 1, 1)

        result = VesselClassBreakdown().search(
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == totalVesselClassBreakdown

    def test_search_returns_any_activity(self):
        date = datetime(2019, 11, 10)

        result = VesselClassBreakdown().search(
            filter_activity="any_activity",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == totalVesselClassBreakdown

    def test_search_returns_excluded_params(self):
        date = datetime(2019, 11, 10)
        rotterdam = (
            "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        )

        result = VesselClassBreakdown().search(
            filter_activity="any_activity",
            breakdown_unit="b",
            filter_time_min=date,
            filter_time_max=date,
            exclude_origins=rotterdam,
        )

        assert len(result) == totalVesselClassBreakdown
