from datetime import datetime
from vortexasdk import VoyagesTimeseries

from tests.testcases import TestCaseUsingRealAPI

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"

class TestVoyagesTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesTimeseries()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam
            )
            .to_df()
        )
        assert len(df) == 5
