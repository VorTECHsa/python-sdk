from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexa.client import default_client, set_client
from vortexa.endpoints.vessels import Vessels


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestVesselsReal(TestCase):

    def test_search_ids(self):
        set_client(default_client())
        ids = [
            "9c85cdb9941fb063b6761da4ad1c48ed6ce15allowed_high_entropy_string",
            "3b6761d9c85cdb9941fb06a4ad1c48ed6ce15allowed_high_entropy_string"
        ]

        vessels = Vessels().search(ids=ids).to_list()
        assert len(vessels) == 2

        print([x.name for x in vessels])

    def test_search_filters_vessel_class(self):
        set_client(default_client())
        vessel_classes = [
            "vlcc_plus",
            "aframax"
        ]

        vessels = Vessels().search(vessel_classes=vessel_classes).to_list()

        actual = {x.vessel_class for x in vessels}

        assert actual == set(vessel_classes)

    def test_search_vessel_class_dataframe(self):
        set_client(default_client())
        ids = [
            "9c85cdb9941fb063b6761da4ad1c48ed6ce15allowed_high_entropy_string",
            "3b6761d9c85cdb9941fb06a4ad1c48ed6ce15allowed_high_entropy_string"
        ]

        df = Vessels().search(ids=ids).to_df()
        print(df)
