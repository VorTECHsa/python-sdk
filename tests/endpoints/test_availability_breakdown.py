
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.availability_breakdown import AvailabilityBreakdown
from tests.testcases import TestCaseUsingRealAPI


class TestAvailabilityBreakdown(TestCaseUsingRealAPI):
    def test_search(self):

        rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"

        df = AvailabilityBreakdown().search(
            filter_days_to_arrival=[{"min": 0, "max": 5}],
            filter_port=rotterdam
        ).to_df()

        assert len(df) == 5