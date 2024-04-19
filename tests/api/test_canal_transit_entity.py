from unittest import TestCase

import json

from vortexasdk.api.canal_transit import CanalTransitRecord


class TestCanalTransitEntity(TestCase):
    def test_serialize(self) -> None:
        with open("tests/api/examples/canal_transit_entity.json", "r") as f:
            serialized = json.load(f)
            CanalTransitRecord.model_validate_json(serialized)
