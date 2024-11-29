from unittest import TestCase

from vortexasdk.api.canal_transit import CanalTransitRecord


class TestCanalTransitEntity(TestCase):
    def test_serialize(self) -> None:
        CanalTransitRecord.model_validate(
            {
                "id": "0004e233f16e15c0fcb3189332807e21306a3b3b06f0a778e3a3d9f276f233bd",
                "vessel_name": "A.I.E.S.A. Boarding Pontoon",
                "vessel_class": [
                    {"id": "vlcc_plus", "label": "VLCC+", "layer": "legacy"},
                    {"id": "oil", "label": "Oil Tankers", "layer": "group"},
                ],
                "canal": "canal1",
                "direction": "southbound",
                "lock": "panamax",
                "cargoes": [
                    {
                        "cargo_movement_id": "1234",
                        "quantity_barrels": 1000,
                        "product": [
                            {
                                "id": "3456",
                                "layer": "group",
                                "label": "Product",
                            }
                        ],
                    }
                ],
                "origin": [],
                "destination": [],
                "queue_arrival_time": "2021-12-20T17:05:00.000Z",
                "canal_entry_time": "2021-12-23T20:00:00.000Z",
                "canal_exit_time": "2021-12-24T22:55:00.000Z",
                "updated_at": "2024-03-14T16:19:30.000Z",
                "created_at": "2024-03-14T16:19:30.000Z",
            }
        )
