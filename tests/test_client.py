from unittest import TestCase

from vortexasdk.client import VortexaClient


class TestClient(TestCase):
    def test__cleanse_payload(self):
        payload = {"a": [], "b": None, "d": 3, "c": [1, 2]}

        cleansed = VortexaClient._cleanse_payload(payload)

        assert str(cleansed) == str({"c": [1, 2], "d": 3})
