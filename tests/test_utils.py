from unittest import TestCase

from vortexasdk.utils import (
    convert_to_list,
    convert_values_to_list,
    filter_exact_match,
)


class TestUtils(TestCase):
    def test_single_item_list(self):
        self.assertEqual(convert_to_list("a"), ["a"])

    def test_multiple_items_list(self):
        self.assertCountEqual(convert_to_list(["a", "b"]), ["a", "b"])

    def test_convert_values_to_list(self):
        actual = convert_values_to_list({1: None, 2: "b", 3: ["c"]})

        expected = {1: [], 2: ["b"], 3: ["c"]}

        assert actual == expected

    def test_filter_doesn_not_match_part_name(self):
        search_result = [{"name": "China"}, {"name": "South China"}]

        self.assertEqual(filter_exact_match("Chi", search_result), [])

    def test_filter_exact_match_single_name(self):
        search_result = [{"name": "China"}, {"name": "South China"}]

        actual = filter_exact_match("China", search_result)

        expected = [{"name": "China"}]

        self.assertEqual(actual, expected)

    def test_filter_exact_match_multiple_names(self):
        search_result = [
            {"name": "China"},
            {"name": "South China"},
            {"name": "United States"},
            {"name": "United Arab Emirates"},
        ]

        actual = filter_exact_match(["China", "United States"], search_result)
        expected = [{"name": "China"}, {"name": "United States"}]

        self.assertCountEqual(actual, expected)
