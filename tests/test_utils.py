from unittest import TestCase

from vortexasdk.utils import (
    convert_to_list,
    convert_values_to_list,
    convert_values_to_list_abstract,
)


class TestUtils(TestCase):
    def test_single_item_list(self):
        assert convert_to_list("a") == ["a"]

    def test_multiple_items_list(self):
        actual = convert_to_list(["a", "b"])
        assert actual == ["a", "b"] or actual == ["b", "a"]

    def test_convert_values_to_list(self):
        d = {1: None, 2: "b", 3: ["c"]}

        expected = {1: [], 2: ["b"], 3: ["c"]}

        assert convert_values_to_list(d) == expected

    def test_convert_values_to_list_abstract(self):
        d = {"a": "v1", "b": "v2", "c": ["v3"]}

        expected = {"a": ["v1"], "b": ["v2"], "c": ["v3"]}

        assert convert_values_to_list_abstract(d) == expected
