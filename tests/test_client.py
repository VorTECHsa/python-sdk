from unittest import TestCase

from vortexasdk.client import VortexaClient


class TestClient(TestCase):
    def test__cleanse_payload(self):
        payload = {"a": [], "b": None, "d": 3, "c": [1, 2]}

        cleansed = VortexaClient._cleanse_payload(payload)

        assert cleansed == {"c": [1, 2], "d": 3}

    def test__cleanse_payload_removes_exclude_empties(self):
        payload = {
            "layer1_k1": [],
            "layer1_k2": None,
            "layer1_k3": 3,
            "exclude": {"layer2_k1": [], "layer2_k2": [1]},
        }

        cleansed = VortexaClient._cleanse_payload(payload)

        assert cleansed == {"layer1_k3": 3, "exclude": {"layer2_k2": [1]}}
