from unittest import TestCase

from tests.mock_client import MockVortexaClient
from vortexasdk.client import set_client
from vortexasdk.endpoints.vessels import Vessels


class TestVessels(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        set_client(MockVortexaClient())

    def test_search_ids_retreives_names(self):
        vessels = Vessels().search().to_list()

        names = [x.name for x in vessels]

        assert names == ['0', '058']
