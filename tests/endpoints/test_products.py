from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.api import Product
from vortexasdk.endpoints.products import Products


class TestProducts(TestCaseUsingMockAPI):
    def test_serialize(self):
        crude_dict = {
            "id": "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
            "name": "Crude",
            "layer": ["group"],
            "leaf": False,
            "parent": [],
            "meta": {"api_min": 33.39586, "api_max": 33.39586},
            "ref_type": "product",
            "hierarchy": [
                {
                    "id": "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
                    "layer": "group",
                    "label": "Crude",
                }
            ],
        }

        Product.from_dict(crude_dict)

    def test_search_ids_retreives_names(self):
        products = Products().search().to_df()
        assert len(products) > 0
