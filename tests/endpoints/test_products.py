from unittest import TestCase
from tests.mock_client import MockVortexaClient
from vortexa.client import set_client
from vortexa.endpoints.products import Products


class TestProducts(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        set_client(MockVortexaClient())

    def test_search_ids_retreives_names(self):
        products = Products().search().to_df()
        assert len(products) > 0


