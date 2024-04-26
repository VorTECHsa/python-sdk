from vortexasdk.api.cargo_movement import CargoMovement

from unittest import TestCase


class TestMissingKeys(TestCase):
    def test_missing_cargo_movement_keys(self) -> None:
        cm = CargoMovement.model_validate(
            {
                "cargo_movement_id": "1234abc",
                "quantity": 100,
                "status": "unloaded_state",
                "parent_ids": [
                    {
                        "id": "abcdef",
                    }
                ],
            }
        )

        assert cm.cargo_movement_id == "1234abc"

        if cm.parent_ids is not None:
            assert cm.parent_ids[0].id == "abcdef"
