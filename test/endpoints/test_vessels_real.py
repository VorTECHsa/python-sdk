from unittest import TestCase, skipIf

from test.config import SKIP_TAGS
from vortexa.client import default_client, set_client
from vortexa.endpoints.vessels import Vessels


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestVesselsReal(TestCase):

    def test_search_ids(self):
        set_client(default_client())
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
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
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
        ]

        df = Vessels().search(ids=ids).to_df()
        print(df)
