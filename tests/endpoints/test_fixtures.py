from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.fixtures import Fixtures
from datetime import datetime


class TestFixtures(TestCaseUsingRealAPI):
    def test_search_fixtures_by_ids(self):
        fixtures = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_df()
        )
        assert len(fixtures) > 0

    def test_to_list(self):
        fixtures = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_list()
        )
        assert len(fixtures) > 0
