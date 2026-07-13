from unittest import TestCase

from vortexasdk.api.entity_flattening import (
    convert_to_flat_dict,
    convert_fixture_to_flat_dict,
)


class TestFixtureFlattening(TestCase):
    """Test that convert_fixture_to_flat_dict groups corporate_entities by layer."""

    FIXTURE = {
        "id": "abc123",
        "vessel": {
            "id": "v1",
            "name": "ALPINE EAGLE",
            "imo": 9480980,
            "mmsi": 255804460,
            "dwt": 300000,
            "cubic_capacity": 330000,
            "vessel_class": "vlcc",
            "classes": [],
            "corporate_entities": [
                {
                    "id": "ec1",
                    "layer": "effective_controller",
                    "label": "Frontline Ltd",
                    "probability": 1,
                    "source": "external",
                },
                {
                    "id": "tc1",
                    "layer": "time_charterer",
                    "label": "Shell",
                    "probability": 0.8,
                    "source": "model",
                    "start_timestamp": "2023-06-01",
                    "end_timestamp": "2024-06-01",
                },
            ],
            "tags": [],
            "flag": [],
            "scrubber": [],
        },
        "tonnes": 270000,
        "laycan_from": "2024-01-01T00:00:00+0000",
        "laycan_to": "2024-01-03T00:00:00+0000",
        "fixing_timestamp": "2023-12-28T14:30:00+0000",
        "vtx_fulfilled": True,
        "origin": {"id": "org1", "label": "Arabian Gulf"},
        "destination": {"id": "dst1", "label": "South Korea"},
        "product": {"id": "prd1", "label": "Crude"},
        "charterer": {"id": "c1", "label": "Trafigura"},
    }

    def test_generic_flattener_uses_numeric_indices(self):
        flat = convert_to_flat_dict(self.FIXTURE, columns="all")
        assert "vessel.corporate_entities.0.label" in flat
        assert "vessel.corporate_entities.effective_controller.label" not in flat

    def test_fixture_flattener_groups_by_layer(self):
        flat = convert_fixture_to_flat_dict(self.FIXTURE, columns="all")
        assert flat["vessel.corporate_entities.effective_controller.label"] == "Frontline Ltd"
        assert flat["vessel.corporate_entities.time_charterer.label"] == "Shell"

    def test_fixture_flattener_preserves_flat_fields(self):
        flat = convert_fixture_to_flat_dict(self.FIXTURE, columns="all")
        assert flat["vessel.name"] == "ALPINE EAGLE"
        assert flat["vessel.imo"] == 9480980
        assert flat["tonnes"] == 270000
        assert flat["charterer.label"] == "Trafigura"

    def test_fixture_flattener_column_filter(self):
        cols = ["vessel.name", "vessel.corporate_entities.effective_controller.label"]
        flat = convert_fixture_to_flat_dict(self.FIXTURE, columns=cols)
        assert set(flat.keys()) == set(cols)
