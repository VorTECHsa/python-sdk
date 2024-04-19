from unittest import TestCase

from vortexasdk.api.product import ProductEntityWithSingleLayer


class TestProductEntity(TestCase):
    def test_serialize(self) -> None:
        ProductEntityWithSingleLayer.model_validate(
            {
                "id": "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
                "layer": "group",
                "probability": 0.9369364,
                "source": "model",
                "label": "Crude & Condensates",
            }
        )

    def test_instantiate_from_dict(self) -> None:
        ProductEntityWithSingleLayer.model_validate(
            {
                "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                "layer": "group",
                "probability": 0.4756425,
                "source": "model",
                "label": "Clean products",
            }
        )
