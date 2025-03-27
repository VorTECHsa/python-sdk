from vortexasdk import OnshoreInventoriesSearch

from tests.testcases import TestCaseUsingRealAPI


class TestOnshoreInventoriesSearch(TestCaseUsingRealAPI):
    # Commented out because the API is not returning data for this query, will bring them back once fixed
    # def test_timeseries_returns_data_frame(self):
    #     df = (
    #         OnshoreInventoriesSearch()
    #         .search(crude_confidence=["unlikely"], storage_types=["refinery"])
    #         .to_df()
    #     )

    #     assert len(df) > 100

    # def test_timeseries_returns_list(self):
    #     lst = (
    #         OnshoreInventoriesSearch()
    #         .search(crude_confidence=["probable"], storage_types=["refinery"])
    #         .to_list()
    #     )

    #     assert len(lst) > 0
    #
    def test_should_throw_an_error_when_invalid_params_are_passed(self):
        self.assertRaises(
            ValueError,
            lambda: OnshoreInventoriesSearch().search(
                crude_confidence=["hello"]
            ),
        )
