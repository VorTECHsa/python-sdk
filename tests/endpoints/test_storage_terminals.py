from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.storage_terminals import StorageTerminals

from tests.mock_client import example_storage_terminals
from vortexasdk.endpoints.storage_terminals_result import StorageTerminalResult


class TestStorageTerminals(TestCaseUsingMockAPI):
    st = StorageTerminalResult(records=example_storage_terminals, reference={})

    def test_search(self):
        terminals = StorageTerminals().search().to_df()
        assert len(terminals) > 0

    def test_term_search_term(self):
        terminals = StorageTerminals().search(term=["Military"]).to_df()
        assert len(terminals) > 0

    def test_search_ids(self):
        terminals = (
            StorageTerminals()
            .search(
                ids=[
                    "08bbaf7a67ab30036d73b9604b932352a73905e16b8342b27f02ae34941b7db5"
                ]
            )
            .to_list()
        )
        names = [a.name for a in terminals]
        assert "Military Oil Depot" in names

    def test_to_list(self):
        terms = [x.name for x in self.st.to_list()]

        assert terms == [
            "Waypoints",
            "South Pars Kangan Site - Phase 13",
            "Military Oil Depot",
        ]

    def test_check_columns(self):
        terminals = StorageTerminals().search().to_df()
        assert list(terminals.columns) == ["id", "name", "lat", "lon"]
