from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.api.product import Product
from vortexasdk.endpoints.products import Products


class TestProducts(TestCaseUsingMockAPI):
    def test_serialize(self) -> None:
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

        Product.model_validate(crude_dict)

    def test_serialize_with_missing_fields(self) -> None:
        crude_dict = {
            "id": "abc123",
            "name": "Crude",
            "layer": ["group"],
            "parent": [],
            "meta": {"api_min": 33.39586, "api_max": 33.39586},
            "ref_type": "product",
        }

        Product.model_validate(crude_dict)

    def test_search_ids_retrieves_names(self) -> None:
        products = Products().search().to_df()
        assert len(products) > 0

    def test_to_list(self) -> None:
        Products().search().to_list()
