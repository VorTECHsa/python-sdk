from datetime import datetime
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.products import Products
from vortexasdk.endpoints.utilisation_capacity_timeseries import UtilisationCapacityTimeseries

from tests.testcases import TestCaseUsingRealAPI

class TestUtilisationCapacityTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 1, 11)
        end = datetime(2021, 1, 18)

        rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        crude = [p.id for p in Products().search("crude").to_list() if "Crude" == p.name]

        df = (
            UtilisationCapacityTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day",
                filter_origins=rotterdam,
                filter_products=crude,
                timeseries_property="quantity"
            )
            .to_df()
        )

        assert len(df) == 8
