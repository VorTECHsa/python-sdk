from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VoyagesSearch

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"

class TestVoyagesSearch(TestCaseUsingRealAPI):
    def test_search_returns_dataframe(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesSearch()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_search_returns_some_cols(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesSearch()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                csv_columns=['vessel_name', 'imo', 'dwt', 'capacity']
            )
            .to_df()
        )

        assert len(df.columns) == 4