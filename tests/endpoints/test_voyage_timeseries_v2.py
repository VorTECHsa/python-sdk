from datetime import datetime
from vortexasdk import VoyagesTimeseriesV2

from tests.testcases import TestCaseUsingRealAPI

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"


class TestVoyagesTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        numbers_of_days_between_start_and_end = 4

        df = (
            VoyagesTimeseriesV2("voyage-count")
            .search(time_min=start, time_max=end, origins=rotterdam)
            .to_df()
        )
        assert len(df) == numbers_of_days_between_start_and_end

    def test_search_with_breakdown_property_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        numbers_of_days_between_start_and_end = 4

        df = (
            VoyagesTimeseriesV2("voyage-count", "status")
            .search(time_min=start, time_max=end, origins=rotterdam)
            .to_df()
        )
        assert len(df) == numbers_of_days_between_start_and_end
