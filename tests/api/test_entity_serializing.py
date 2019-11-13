from unittest import TestCase

from vortexasdk.api.entity_serializing import serialize, _serialize_ve_layer
from tests.api.test_vessel_entity import ce1, ce2, ve


class TestEntitySerializing(TestCase):

    def test_group_vessel_entity_by_layer(self):
        group_by_layer = _serialize_ve_layer(ve)

        expected = serialize({"commercial_owner": ce1, "charterer": ce2})

        actual = group_by_layer['corporate_entities']
        assert actual == expected
