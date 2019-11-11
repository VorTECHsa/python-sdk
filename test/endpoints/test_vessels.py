from unittest import TestCase

from test.mock_client import MockVortexaClient
from vortexa.client import set_client
from vortexa.endpoints.vessels import Vessels


class TestVessels(TestCase):

    def test_search_ids_retreives_names(self):
        set_client(MockVortexaClient())

        vessels = Vessels().search().to_list()

        names = [x.name for x in vessels]

        assert names == ['0', '058']
