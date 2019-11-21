from unittest import TestCase

from tests.mixins import CallMockAPI
from vortexasdk.endpoints.products import Products


class TestProducts(CallMockAPI, TestCase):

    def test_search_ids_retreives_names(self):
        products = Products().search().to_df()
        assert len(products) > 0
