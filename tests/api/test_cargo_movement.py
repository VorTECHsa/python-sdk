from unittest import TestCase

import json

from vortexasdk.api import (
    CargoMovement,
)
from vortexasdk.api.entity_flattening import (
    convert_cargo_movement_to_flat_dict,
)


class TestCargoMovement(TestCase):
    dictionary = {
        "cargo_movement_id": "00886b05a0747522b67322f50123ee60e61e219fc9a9c6011be1a1dade65f63e",
        "quantity": 4401,
        "status": "unloaded_state",
        "vessels": [
            {
                "id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
                "mmsi": 255804460,
                "imo": 9480980,
                "name": "JOHANN ESSBERGER",
                "dwt": 5260,
                "cubic_capacity": 6100,
                "vessel_class": "tiny_tanker",
                "classes": [
                    {"id": "vlcc_plus", "label": "VLCC+", "layer": "legacy"},
                    {"id": "oil", "label": "Oil Tankers", "layer": "group"},
                    {"id": "oil_vlcc", "label": "VLCC+", "layer": "coarse"},
                    {"id": "oil_vlcc", "label": "VLCC+", "layer": "granular"},
                ],
                "corporate_entities": [
                    {
                        "id": "f9bd45e65e292909a7b751b0026dcf7795c6194b3c0712910a241caee32c99b8",
                        "label": "Essberger J.T.",
                        "layer": "effective_controller",
                        "probability": 1.0,
                        "source": "external",
                    }
                ],
                "start_timestamp": "2019-10-18T21:38:34+0000",
                "end_timestamp": "2019-10-25T00:40:46+0000",
                "fixture_fulfilled": False,
                "voyage_id": "401f0e74fc42401248a484aca2e9955dea885378796f7f4d0bc8e92c35ea270a",
                "tags": [],
                "status": "vessel_status_laden_known",
            }
        ],
        "product": [
            {
                "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                "layer": "group",
                "probability": 0.4756425,
                "source": "model",
                "label": "Clean products",
            },
            {
                "id": "a75fcc09bfc7d16496de3336551bc52b5891838bb7c22356d2cb65451587d1e5",
                "layer": "group_product",
                "probability": 0.4756425,
                "source": "model",
                "label": "Biodiesel",
            },
            {
                "id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
                "layer": "grade",
                "probability": 0.4756425,
                "source": "model",
                "label": "Biodiesel Feedstock",
            },
        ],
        "events": [
            {
                "event_type": "cargo_port_load_event",
                "location": [
                    {
                        "id": "2dfc3d43a21697c02ec3b2700b3b570a6ed1abb66d01c4fe6310ef362fcf6653",
                        "layer": "country",
                        "label": "Netherlands",
                        "source": "model",
                        "probability": 1.0,
                    }
                ],
                "vessel_id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
                "probability": 1.0,
                "pos": [4.29914090037834, 51.87936163368058],
                "start_timestamp": "2019-10-18T21:38:34+0000",
                "end_timestamp": "2019-10-20T16:41:49+0000",
            }
        ],
        "parent_ids": [
            {
                "id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
                "splinter_timestamp": "2019-10-20T16:41:49+0000",
            }
        ],
    }

    cm = CargoMovement.parse_obj(dictionary)

    def test_serialize(self):
        with open("tests/api/examples/cargo_movements.json", "r") as f:
            serialized = json.load(f)[0]
            deserialized = CargoMovement.parse_obj(serialized)

            assert self.cm == deserialized

    def test_convert_to_flat_dict(self):
        flat = convert_cargo_movement_to_flat_dict(self.cm.dict())

        expected = {
            "cargo_movement_id": "00886b05a0747522b67322f50123ee60e61e219fc9a9c6011be1a1dade65f63e",
            "events.cargo_port_load_event.0.end_timestamp": "2019-10-20T16:41:49+0000",
            "events.cargo_port_load_event.0.event_type": "cargo_port_load_event",
            "events.cargo_port_load_event.0.location.country.id": "2dfc3d43a21697c02ec3b2700b3b570a6ed1abb66d01c4fe6310ef362fcf6653",
            "events.cargo_port_load_event.0.location.country.label": "Netherlands",
            "events.cargo_port_load_event.0.location.country.layer": "country",
            "events.cargo_port_load_event.0.location.country.probability": 1.0,
            "events.cargo_port_load_event.0.location.country.source": "model",
            "events.cargo_port_load_event.0.pos.0": 4.29914090037834,
            "events.cargo_port_load_event.0.pos.1": 51.87936163368058,
            "events.cargo_port_load_event.0.probability": 1.0,
            "events.cargo_port_load_event.0.start_timestamp": "2019-10-18T21:38:34+0000",
            "events.cargo_port_load_event.0.vessel_id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
            "product.group.id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
            "product.group.label": "Clean products",
            "product.group.layer": "group",
            "product.group.probability": 0.4756425,
            "product.group.source": "model",
            "product.group_product.id": "a75fcc09bfc7d16496de3336551bc52b5891838bb7c22356d2cb65451587d1e5",
            "product.group_product.label": "Biodiesel",
            "product.group_product.layer": "group_product",
            "product.group_product.probability": 0.4756425,
            "product.group_product.source": "model",
            "product.grade.id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
            "product.grade.label": "Biodiesel Feedstock",
            "product.grade.layer": "grade",
            "product.grade.probability": 0.4756425,
            "product.grade.source": "model",
            "quantity": 4401,
            "status": "unloaded_state",
            "vessels.0.corporate_entities.effective_controller.id": "f9bd45e65e292909a7b751b0026dcf7795c6194b3c0712910a241caee32c99b8",
            "vessels.0.corporate_entities.effective_controller.label": "Essberger J.T.",
            "vessels.0.corporate_entities.effective_controller.layer": "effective_controller",
            "vessels.0.corporate_entities.effective_controller.probability": 1.0,
            "vessels.0.corporate_entities.effective_controller.source": "external",
            "vessels.0.corporate_entities.effective_controller.start_timestamp": None,
            "vessels.0.corporate_entities.effective_controller.end_timestamp": None,
            "vessels.0.cubic_capacity": 6100,
            "vessels.0.end_timestamp": "2019-10-25T00:40:46+0000",
            "vessels.0.fixture_fulfilled": False,
            "vessels.0.fixture_id": None,
            "vessels.0.id": "9cbf7c0fc6ccf1dfeacde02b87f3b6b1653030f560d4fc677bf1d7d0be8f8449",
            "vessels.0.imo": 9480980,
            "vessels.0.mmsi": 255804460,
            "vessels.0.name": "JOHANN ESSBERGER",
            "vessels.0.dwt": 5260,
            "vessels.0.year": None,
            "vessels.0.ice_class": None,
            "vessels.0.propulsion": None,
            "vessels.0.start_timestamp": "2019-10-18T21:38:34+0000",
            "vessels.0.status": "vessel_status_laden_known",
            "vessels.0.vessel_class": "tiny_tanker",
            "vessels.0.classes.0.id": "vlcc_plus",
            "vessels.0.classes.0.layer": "legacy",
            "vessels.0.classes.0.label": "VLCC+",
            "vessels.0.classes.1.id": "oil",
            "vessels.0.classes.1.layer": "group",
            "vessels.0.classes.1.label": "Oil Tankers",
            "vessels.0.classes.2.id": "oil_vlcc",
            "vessels.0.classes.2.layer": "coarse",
            "vessels.0.classes.2.label": "VLCC+",
            "vessels.0.classes.3.id": "oil_vlcc",
            "vessels.0.classes.3.layer": "granular",
            "vessels.0.classes.3.label": "VLCC+",
            "vessels.0.scrubber": None,
            "vessels.0.flag": None,
            "vessels.0.voyage_id": "401f0e74fc42401248a484aca2e9955dea885378796f7f4d0bc8e92c35ea270a",
            "parent_ids.0.id": "9d52ede1cff0421a8cd7283b0171afe8d23f519dca5f4e489734522f9cdf804c",
            "parent_ids.0.splinter_timestamp": "2019-10-20T16:41:49+0000",
        }

        assert flat == expected
