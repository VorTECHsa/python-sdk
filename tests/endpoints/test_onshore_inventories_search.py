from vortexasdk import OnshoreInventoriesSearch
from datetime import datetime
from tests.testcases import TestCaseUsingRealAPI


class TestOnshoreInventoriesSearch(TestCaseUsingRealAPI):
    def test_timeseries_returns_data_frame(self):
        df = (
            OnshoreInventoriesSearch()
            .search(crude_confidence=["unlikely"], storage_types=["refinery"], time_max=datetime(2025, 1, 2), time_min=datetime(2025, 1, 1))
            .to_df()
        )

        assert len(df) > 100

    def test_timeseries_returns_list(self):
        lst = (
            OnshoreInventoriesSearch()
            .search(crude_confidence=["probable"], storage_types=["refinery"], time_max=datetime(2025, 1, 2), time_min=datetime(2025, 1, 1))
            .to_list()
        )

        assert len(lst) > 0

    def test_should_throw_an_error_when_invalid_params_are_passed(self):
        self.assertRaises(
            ValueError,
            lambda: OnshoreInventoriesSearch().search(
                crude_confidence=["hello"]
            ),
        )
