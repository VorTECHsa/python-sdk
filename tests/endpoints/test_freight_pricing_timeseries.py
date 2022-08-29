from datetime import datetime
from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.freight_pricing_timeseries import (
    FreightPricingTimeseries,
)


class TestFreightPricingTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 11, 1)
        end = datetime(2021, 11, 5)

        df = (
            FreightPricingTimeseries()
            .search(
                time_min=start,
                time_max=end,
                routes=["TD3C"],
                breakdown_frequency="day",
                breakdown_property="rate",
            )
            .to_df()
        )
        assert len(df) == 5

    def test_search_returns_all_days_as_list(self):
        start = datetime(2021, 11, 1)
        end = datetime(2021, 11, 5)

        result_list = (
            FreightPricingTimeseries()
            .search(
                time_min=start,
                time_max=end,
                routes=["TD3C"],
                breakdown_frequency="day",
                breakdown_property="rate",
            )
            .to_list()
        )
        assert len(result_list) == 5
