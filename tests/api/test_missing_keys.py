from vortexasdk.api import CargoMovement

from unittest import TestCase


class TestMissingKeys(TestCase):
    def test_missing_cargo_movement_keys(self):
        dictionary = {
            "cargo_movement_id": "1234abc",
            "quantity": 100,
            "status": "unloaded_state",
            "parent_ids": [
                {
                    "id": "abcdef",
                }
            ],
        }

        cm = CargoMovement.parse_obj(dictionary)

        assert cm.cargo_movement_id == "1234abc"
        assert cm.parent_ids[0].id == "abcdef"
