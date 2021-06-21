
from vortexasdk.endpoints.availability_breakdown import AvailabilityBreakdown
from tests.testcases import TestCaseUsingMockAPI


class TestAvailabilityBreakdown(TestCaseUsingMockAPI):
    def test_search(self):

        result = AvailabilityBreakdown().search(
            filter_days_to_arrival= [{"min": 0, "max": 5}],
            filter_port = "1b79e18416d358d7e07b978abcab3f17e2ca75085a6d70ce1811cf4eaeaea886"
        )

        assert len(result) == 3