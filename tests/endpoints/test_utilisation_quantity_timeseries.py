from datetime import datetime
from vortexasdk.endpoints.utilisation_quantity_timeseries import UtilisationQuantityTimeseries

from tests.testcases import TestCaseUsingRealAPI

class TestUtilisationQuantityTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            UtilisationQuantityTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day",
                timeseries_property="quantity",
                timeseries_unit="t"
            )
            .to_df()
        )

        assert len(df) == 5
