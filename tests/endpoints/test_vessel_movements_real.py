from tests.testcases import TestCaseUsingRealAPI
from tests.utils import to_markdown
from vortexasdk import VesselMovements


class TestVesselMovementsReal(TestCaseUsingRealAPI):
    def test_search(self):
        v = VesselMovements().search(
            filter_time_min="2019-10-01T00:00:00.000Z",
            filter_time_max="2019-10-01T00:10:00.000Z",
            filter_origins="rotterdam",
        )

        assert len(v) > 10

    def test_search_to_dataframe(self):
        df = (
            VesselMovements()
            .search(
                filter_time_min="2017-10-01T00:00:00.000Z",
                filter_time_max="2017-10-01T00:10:00.000Z",
                filter_origins="rotterdam",
            )
            .to_df()
            .head(2)
        )

        for c in sorted(df.columns):
            print(f"{c},")

        print(df)

        print(to_markdown(df))
