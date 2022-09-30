from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VoyagesSearchEnriched

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"


class TestVoyagesSearchEnrichedEnriched(TestCaseUsingRealAPI):
    def test_search_returns_dataframe(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesSearchEnriched()
            .search(
                time_min=start, time_max=end, origins=rotterdam, columns="all"
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_search_returns_some_cols(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                columns=["vessel_name", "imo", "voyage_status", "destination"],
            )
            .to_df()
        )

        assert len(df.columns) == 4
        assert list(df.columns) == [
            "VESSEL NAME",
            "IMO",
            "VOYAGE STATUS",
            "DESTINATION",
        ]

    def test_search_from_description_df(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start, time_max=end, origins=rotterdam, columns="all"
            )
            .to_df()
            .head()
        )

        assert len(res) > 0

    def test_search_from_description_raw(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(time_min=start, time_max=end, origins=rotterdam)
            .to_list()
        )

        assert len(res) > 0
        assert res[0].schema_version == "1.0.0"
        assert res[0].vessel is not None
        assert len(res[0].events) > 0
        assert res[0].events[0].event_group is not None

    def test_has_charterer_param(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        try:
            VoyagesSearchEnriched().search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                has_charterer=False,
            ).to_list()

        except ValueError as error:
            print(error)

    def test_has_ship_to_ship_param(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        try:
            VoyagesSearchEnriched().search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                has_ship_to_ship=False,
            ).to_list()

        except ValueError as error:
            print(error)
