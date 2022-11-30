from unittest import TestCase
import json

from vortexasdk.api.vessel import VesselEntity

ve = VesselEntity(
    **{
        "id": "1f6d6ab80d90846cedddf1a4b470faf566fd72595e853bc769185fac6ae7af70",
        "mmsi": 403534000,
        "imo": 9779836,
        "name": "RIMTHAN",
        "dwt": 298855,
        "cubic_capacity": 327310,
        "vessel_class": "vlcc_plus",
        "corporate_entities": [
            {
                "id": "cbd7dfe8a9fb0fa0ce3252ce7643437db6a32d0947a0c23d68dc5dea2f2d65d7",
                "layer": "effective_controller",
                "probability": 1,
                "label": "NGM Energy",
                "source": "external",
            },
            {
                "id": "0bdf9acdc00ad52d9b8c44dad815087a89205a9c83f53ed89e029f7d15b9ac14",
                "layer": "charterer",
                "probability": 1,
                "label": "CHEVRON",
                "source": "external",
            },
        ],
        "start_timestamp": "2019-10-14T00:00:00+0000",
        "fixture_id": "cc4f364367db830da1d5d8ad89b02a7dc6f207402cd907a19c9d713e1a70b0ed",
        "fixture_fulfilled": False,
        "voyage_id": "813cb0baf01a335a5c74aded99b5c910bf627b24ff7b5eb9ed943579e902495d",
        "tags": [],
        "status": "vessel_status_laden_known",
    }
)


class TestVesselEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/vessel_entity1.json", "r") as f:
            serialized = json.load(f)
            deserialized = VesselEntity.parse_obj(serialized)

            assert ve == deserialized
