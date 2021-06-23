from datetime import datetime
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.availability_timeseries import AvailabilityTimeseries

from tests.testcases import TestCaseUsingRealAPI

singapore = "1b79e18416d358d7e07b978abcab3f17e2ca75085a6d70ce1811cf4eaeaea886"

class TestAvailabilityTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]

        df = (
            AvailabilityTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                filter_port=rotterdam[0],
                filter_days_to_arrival={"min": 0, "max": 5}
            )
            .to_df()
        )
        assert len(df) == 4
