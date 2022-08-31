from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VoyagesTopHits
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.products import Products


class TestVoyagesTopHits(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)
        end_date = datetime(2019, 11, 11)

        result = VoyagesTopHits().search(
            time_min=date,
            time_max=end_date,
        )

        assert len(result) > 0

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = VoyagesTopHits().search(
            time_min=start,
            time_max=end,
        )

        assert len(result) > 0

    def test_search_split_vessel_status(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = VoyagesTopHits().search(
            breakdown_split_property="vessel_status",
            time_min=start,
            time_max=end,
        )

        assert len(result) > 0

    def test_search_returns_larger_size(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 11, 10)

        result = VoyagesTopHits().search(
            time_min=start, time_max=end, breakdown_size=5
        )

        assert len(result) == 5

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            VoyagesTopHits()
            .search(
                time_min=start,
                time_max=end,
            )
            .to_df()
        )

        assert len(df) > 0
        assert list(df.columns) == ["id", "value", "count", "label"]

    def test_with_params(self):

        df = (
            VoyagesTopHits()
            .search(
                origins="80aa9e4f3014c3d96559c8e642157edbb2b684ea0144ed76cd20b3af75110877",
                destinations="934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2",
                time_min=datetime(2020, 12, 19),
                time_max=datetime(2021, 1, 18),
            )
            .to_df()
            .head()
        )

        assert list(df.columns) == ["id", "value", "count", "label"]

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            VoyagesTopHits()
            .search(
                time_min=start,
                time_max=end,
            )
            .to_list()
        )

        assert len(time_series_list) > 0

    def test_from_description(self):
        start = datetime(2021, 8, 1)
        end = datetime(2021, 8, 1, 23, 59)

        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        crude = [
            p.id
            for p in Products().search("crude").to_list()
            if "Crude" == p.name
        ]

        time_series_list = (
            VoyagesTopHits()
            .search(
                destinations=rotterdam,
                products=crude,
                time_min=start,
                time_max=end,
                breakdown_split_property="origin_country",
                breakdown_size=5,
            )
            .to_list()
        )

        assert len(time_series_list) > 0
