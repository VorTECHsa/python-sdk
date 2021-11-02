from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.storage_terminals import StorageTerminals

from tests.mock_client import example_storage_terminals
from vortexasdk.endpoints.storage_terminals_result import StorageTerminalResult


class TestStorageTerminals(TestCaseUsingMockAPI):
    st = StorageTerminalResult(example_storage_terminals)

    def test_search(self):
        asset_tanks = StorageTerminals().search().to_df()
        assert len(asset_tanks) > 0

    def test_name_search_term(self):
        asset_tanks = StorageTerminals().search(name=['Military']).to_df()
        assert len(asset_tanks) > 0

    def test_search_ids(self):
        asset_tanks = (
            StorageTerminals().search(ids=['08bbaf7a67ab30036d73b9604b932352a73905e16b8342b27f02ae34941b7db5']).to_list()
        )
        names = [a.name for a in asset_tanks]
        assert 'Military Oil Depot' in names

    def test_to_list(self):
        names = [x.name for x in self.st.to_list()]

        assert names == ['Waypoints', 'South Pars Kangan Site - Phase 13', 'Military Oil Depot']
