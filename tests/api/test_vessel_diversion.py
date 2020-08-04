from unittest import TestCase

import jsons

from vortexasdk.api.entity_flattening import convert_vessel_diversion_to_flat_dict
from vortexasdk.api.serdes import serialize_to_dict
from vortexasdk.api import GeographyEntity, Entity, CorporateEntity, ProductEntity
from vortexasdk.api.vessel_diversion import VesselDiversion, DiversionCargo


class TestVesselDiversion(TestCase):
    vessel_diversion = VesselDiversion(
        id="40fda5cdec443c02d9e699ca04f99b8f40fda5cdec443c02d9e699ca04f99b8f",
        timestamp="2020-01-28T16:02:14.000Z",
        origin=[GeographyEntity(
            id="c1698979b983b265490545013156924518af07faf7f25905a78a1813054860d8",
            layer="country",
            probability=1,
            source="model",
            label="Spain"
        )],
        is_considered_waypoint=False,

        prev_declared_destination="BRYANO",
        prev_destination=[Entity(
            id="83721a9f179522d7532170e28b57cc79f58e2346012ed977849ebad9f7153b46",
            label="Nouadhibou [MR]",
            layer="port"
        )],
        prev_eta="2020-01-20T06:00:00.000Z",

        next_declared_destination="MASTAF",
        next_destination=[Entity(
            id="8798b848ede7e47c72ce197a3b94c43b10815cdf2f0e3fbad8a857d66846cb72",
            label="Senegal",
            layer="country"
        )],
        next_eta="2020-01-31T01:00:00.000Z",
        vessel_id="52a40e17e22a1947c5c9f59a09ee445c612ba3dbc0a8fb2989effcc06a397280",
        vessel_class="general_purpose",
        vessel_corporate_entities=[CorporateEntity(
            id="043c42534f06710bcd4e1861a4bfc5bc777999cbc3257f4d39e790c98c817a64",
            layer="commercial_owner",
            label="Para Management",
            probability=1,
            source="external"
        )],
        vessel_imo=9117340,
        vessel_name="BIGGUS SHIPPUS",
        cargoes=[DiversionCargo(
            product_hierarchy=[ProductEntity(
                id="b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                label="Clean Petroleum Products",
                layer="group",
                source="external",
                probability=1
            )],
            quantity=91345
        )],
    )

    def test_serialize(self):
        with open("tests/api/examples/diversion1.json", "r") as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, VesselDiversion)

            assert self.vessel_diversion == deserialized

    def test_flatten(self):
        d = serialize_to_dict(self.vessel_diversion)
        flat = convert_vessel_diversion_to_flat_dict(d)

        expected = {
            "id": "40fda5cdec443c02d9e699ca04f99b8f40fda5cdec443c02d9e699ca04f99b8f",
            "prev_destination.port.id": "83721a9f179522d7532170e28b57cc79f58e2346012ed977849ebad9f7153b46",
            "prev_destination.port.label": "Nouadhibou [MR]",
            "prev_eta": "2020-01-20T06:00:00.000Z",
            "prev_declared_destination": "BRYANO",
            "next_eta": "2020-01-31T01:00:00.000Z",
            "next_destination.country.id": "8798b848ede7e47c72ce197a3b94c43b10815cdf2f0e3fbad8a857d66846cb72",
            "next_destination.country.label": "Senegal",
            "cargoes": [
                {
                    "product_hierarchy": [
                        {
                            "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
                            "layer": "group",
                            "probability": 1,
                            "source": "external",
                            "label": "Clean Petroleum Products"
                        }
                    ],
                    "quantity": 91345
                }
            ],
            "timestamp": "2020-01-28T16:02:14.000Z",
            "next_declared_destination": "MASTAF",
            "origin": [
                {
                    "id": "c1698979b983b265490545013156924518af07faf7f25905a78a1813054860d8",
                    "layer": "country",
                    "probability": 1,
                    "source": "model",
                    "label": "Spain"
                }
            ],
            "next_destination_timestamp": "2020-01-31T01:00:00.000Z",
            "vessel_id": "52a40e17e22a1947c5c9f59a09ee445c612ba3dbc0a8fb2989effcc06a397280",
            "vessel_name": "BIGGUS SHIPPUS",
            "vessel_class": "general_purpose",
            "vessel_imo": 9117340,
            "vessel_corporate_entities": [
                {
                    "id": "043c42534f06710bcd4e1861a4bfc5bc777999cbc3257f4d39e790c98c817a64",
                    "label": "Para Management",
                    "layer": "commercial_owner",
                    "probability": 1,
                    "source": "external"
                }
            ],
            "is_considered_waypoint": False
        }

        assert flat == expected


