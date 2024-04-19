from typing import Any
from vortexasdk.api.cargo_movement import CargoMovement

from unittest import TestCase


class TestMissingKeys(TestCase):
    def test_missing_cargo_movement_keys(self) -> None:
        dictionary: dict[str, Any] = {
            "cargo_movement_id": "1234abc",
            "quantity": 100,
            "status": "unloaded_state",
            "parent_ids": [
                {
                    "id": "abcdef",
                }
            ],
        }

        cm = CargoMovement.model_validate(dictionary)

        assert cm.cargo_movement_id == "1234abc"
        assert cm.parent_ids[0].id == "abcdef"
