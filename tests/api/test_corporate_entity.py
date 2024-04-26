from unittest import TestCase

from vortexasdk.api.corporation import CorporateEntity


class TestCorporateEntity(TestCase):
    def test_serialize(self) -> None:
        CorporateEntity.model_validate(
            {
                "id": "cbd7dfe8a9fb0fa0ce3252ce7643437db6a32d0947a0c23d68dc5dea2f2d65d7",
                "layer": "effective_controller",
                "probability": 1,
                "source": "external",
                "label": "NGM Energy",
            }
        )
