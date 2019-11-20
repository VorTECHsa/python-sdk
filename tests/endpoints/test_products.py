from unittest import TestCase
from tests.mock_client import MockVortexaClient
from vortexasdk.client import set_client
from vortexasdk.endpoints.products import Products


class TestProducts(TestCase):

    def setUp(self) -> None:
        set_client(MockVortexaClient())

    def test_search_ids_retreives_names(self):
        products = Products().search().to_df()
        assert len(products) > 0
