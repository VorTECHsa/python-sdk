from unittest import TestCase

from vortexa.endpoints.vessels import Vessels


class TestVessels(TestCase):

    def test_search_ids(self):
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
        ]

        vessels = Vessels().search(ids=ids).to_list()
        assert len(vessels) == 2

        print([x['name'] for x in vessels])

    def test_search_vessel_class(self):
        vessel_classes = [
            "vlcc_plus",
            "aframax"
        ]

        vessels = Vessels().search(vessel_classes=vessel_classes).to_list()

        print([x['name'] for x in vessels])

    def test_search_vessel_class_dataframe(self):
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
        ]

        vessels = Vessels().search(ids=ids)
        print(vessels)
