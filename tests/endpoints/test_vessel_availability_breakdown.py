
from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.vessel_availability_breakdown import VesselAvailabilityBreakdown


class TestVesselAvailabilityBreakdown(TestCaseUsingMockAPI):
    def test_search(self):

        result = VesselAvailabilityBreakdown().search(
            filter_days_to_arrival= [{"min": 0, "max": 5}],
            filter_port = "1b79e18416d358d7e07b978abcab3f17e2ca75085a6d70ce1811cf4eaeaea886"
        )

        assert len(result) == 3