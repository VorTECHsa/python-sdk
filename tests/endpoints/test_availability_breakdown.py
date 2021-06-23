
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.availability_breakdown import AvailabilityBreakdown
from tests.testcases import TestCaseUsingRealAPI


class TestAvailabilityBreakdown(TestCaseUsingRealAPI):
    def test_search(self):

        rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]

        df = AvailabilityBreakdown().search(
            filter_days_to_arrival=[{"min": 0, "max": 5}],
            filter_port=rotterdam[0]
        ).to_df()

        assert len(df) == 5