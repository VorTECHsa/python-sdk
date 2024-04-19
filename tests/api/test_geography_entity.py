from unittest import TestCase
from vortexasdk.api.geography import GeographyEntity


class TestGeographyEntity(TestCase):
    def test_serialize(self) -> None:
        GeographyEntity.model_validate(
            {
                "id": "2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
                "layer": "country",
                "label": "United Kingdom",
                "source": "model",
                "probability": 1,
            }
        )
