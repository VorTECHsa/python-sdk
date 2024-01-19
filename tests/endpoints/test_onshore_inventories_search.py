from vortexasdk import OnshoreInventoriesSearch

from tests.testcases import TestCaseUsingRealAPI


class TestOnshoreInventoriesSearch(TestCaseUsingRealAPI):
    def test_timeseries_returns_data_frame(self):
        df = (
            OnshoreInventoriesSearch()
            .search(crude_confidence=["unlikely"], storage_types=["refinery"])
            .to_df()
        )

        assert len(df) > 100

    def test_filter_by_measurement_ids(self):
        """
        This test can be a little flaky!
        Sometimes the `measurement_id` might get recycled and disappear.
        If this happens, you may need to find a new one and replace.
        Also consider removing this test if it happens periodically.
        """

        df = (
            OnshoreInventoriesSearch()
            .search(
                measurement_ids=[
                    "00010ff9d5d026fbcaa9196be69287a2caffcfd222af99d15724ecbbfe0f070e"
                ]
            )
            .to_df()
        )
        # There should be exactly one result returned
        assert len(df) == 1

    def test_timeseries_returns_list(self):
        lst = (
            OnshoreInventoriesSearch()
            .search(crude_confidence=["probable"], storage_types=["refinery"])
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
