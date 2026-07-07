from unittest.mock import patch

from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.api.shared_types import Tag
from vortexasdk.endpoints.vessels import Vessels


class TestVessels(TestCaseUsingMockAPI):
    def test_search_ids_retreives_names(self):
        vessels = Vessels().search().to_list()

        names = [x.name for x in vessels]

        assert names == ["0", "058"]

    def test_convert_to_df(self):
        df = Vessels().search().to_df()
        assert len(df) > 0

    @patch("vortexasdk.operations.default_client")
    def test_search_with_vessel_tags(self, mock_client):
        mock_client.return_value.search_base.return_value = {
            "data": [],
            "reference": {},
        }

        Vessels().search(
            vessel_tags=[Tag(tag="vessel_fso_tag")],
        )

        _, kwargs = mock_client.return_value.search_base.call_args
        assert kwargs["vessel_tags"] == [{"tag": "vessel_fso_tag"}]

    @patch("vortexasdk.operations.default_client")
    def test_search_with_vessel_tags_excluded(self, mock_client):
        mock_client.return_value.search_base.return_value = {
            "data": [],
            "reference": {},
        }

        Vessels().search(
            vessel_tags_excluded=[Tag(tag="vessel_fso_tag")],
        )

        _, kwargs = mock_client.return_value.search_base.call_args
        assert kwargs["vessel_tags_excluded"] == [{"tag": "vessel_fso_tag"}]

    @patch("vortexasdk.operations.default_client")
    def test_search_with_single_vessel_tag(self, mock_client):
        mock_client.return_value.search_base.return_value = {
            "data": [],
            "reference": {},
        }

        Vessels().search(
            vessel_tags=Tag(tag="vessel_decommissioned_tag"),
        )

        _, kwargs = mock_client.return_value.search_base.call_args
        assert kwargs["vessel_tags"] == [{"tag": "vessel_decommissioned_tag"}]

    @patch("vortexasdk.operations.default_client")
    def test_search_with_multiple_vessel_tags(self, mock_client):
        mock_client.return_value.search_base.return_value = {
            "data": [],
            "reference": {},
        }

        Vessels().search(
            vessel_tags=[
                Tag(tag="vessel_fso_tag"),
                Tag(tag="vessel_decommissioned_tag"),
            ],
        )

        _, kwargs = mock_client.return_value.search_base.call_args
        assert kwargs["vessel_tags"] == [
            {"tag": "vessel_fso_tag"},
            {"tag": "vessel_decommissioned_tag"},
        ]
