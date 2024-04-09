from unittest import TestCase

import json

from vortexasdk.api.canal_transit import CanalTransitRecord


class TestCanalTransitEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/canal_transit_entity.json", "r") as f:
            serialized = json.load(f)
            deserialized = CanalTransitRecord.parse_obj(serialized)

            expected = CanalTransitRecord(
                id="0004e233f16e15c0fcb3189332807e21306a3b3b06f0a778e3a3d9f276f233bd",
                canal="canal1",
                vessel_class=[
                    {"id": "vlcc_plus", "label": "VLCC+", "layer": "legacy"},
                    {"id": "oil", "label": "Oil Tankers", "layer": "group"},
                ],
                vessel_name="A.I.E.S.A. Boarding Pontoon",
                lock="panamax",
                direction="southbound",
                queue_arrival_time="2021-12-20T17:05:00.000Z",
                canal_entry_time="2021-12-23T20:00:00.000Z",
                canal_exit_time="2021-12-24T22:55:00.000Z",
                updated_at="2024-03-14T16:19:30.000Z",
                created_at="2024-03-14T16:19:30.000Z",
            )

            assert expected == deserialized
