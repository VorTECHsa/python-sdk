from datetime import datetime
from vortexasdk import VesselAvailabilityTimeseries

from tests.testcases import TestCaseUsingRealAPI

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"


class TestVesselAvailabilityTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VesselAvailabilityTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                filter_port=rotterdam,
                filter_days_to_arrival={"min": 0, "max": 5},
            )
            .to_df()
        )
        assert len(df) == 4
