from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.asset_tanks import AssetTanks

from tests.mock_client import example_asset_tanks
from vortexasdk.endpoints.asset_tanks_result import AssetTankResult


class TestAssetTanks(TestCaseUsingMockAPI):
    at = AssetTankResult(records=example_asset_tanks, reference={})

    def test_search(self):
        asset_tanks = AssetTanks().search().to_df()
        assert len(asset_tanks) > 0

    def test_storage_type_search_term(self):
        asset_tanks = AssetTanks().search(storage_type=["refinery"]).to_df()
        assert len(asset_tanks) > 0

    def test_search_ids(self):
        asset_tanks = (
            AssetTanks()
            .search(
                ids=[
                    "6114b93026e61993797db33a46a5d2acbeacdbd63238a4271efaeafcee94b1d2"
                ]
            )
            .to_list()
        )
        names = [a.name for a in asset_tanks]
        assert "AAM001" in names

    def test_to_list(self):
        names = [x.name for x in self.at.to_list()]

        assert names == ["AAM001", "ASL011"]

    def test_check_columns(self):
        asset_tanks = AssetTanks().search().to_df()
        assert list(asset_tanks.columns) == [
            "id",
            "capacity_bbl",
            "crude_confidence",
            "location_id",
            "name",
            "storage_type",
            "lat",
            "lon",
        ]
