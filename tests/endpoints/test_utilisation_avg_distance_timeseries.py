from datetime import datetime
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.products import Products
from vortexasdk.endpoints.utilisation_avg_distance_timeseries import UtilisationAvgDistanceTimeseries

from tests.testcases import TestCaseUsingRealAPI

class TestUtilisationAvgDistanceTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 1, 11)
        end = datetime(2021, 1, 18)

        rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        crude = [p.id for p in Products().search("crude").to_list() if "Crude" == p.name]

        df = (
            UtilisationAvgDistanceTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day",
                filter_origins=rotterdam,
                filter_products=crude,
                timeseries_property="quantity",
                timeseries_unit="km"
            )
            .to_df()
        )

        assert len(df) == 8
