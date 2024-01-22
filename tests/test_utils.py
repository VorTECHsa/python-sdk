from datetime import datetime
from unittest import TestCase

from vortexasdk.utils import (
    convert_to_list,
    convert_values_to_list,
    filter_exact_match,
    chunk_time_series,
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

    def test_chunk_time_series_large_time_frame(self):
        time_min = datetime.fromisoformat("2022-07-30")
        time_max = datetime.fromisoformat("2022-08-30")
        result = chunk_time_series(time_min, time_max, chunk_size=14)
        expected = [
            {
                "time_max": datetime.fromisoformat(
                    "2022-08-13T23:59:59.999999"
                ),
                "time_min": datetime.fromisoformat("2022-07-30T00:00:00"),
            },
            {
                "time_max": datetime.fromisoformat(
                    "2022-08-27T23:59:59.999999"
                ),
                "time_min": datetime.fromisoformat("2022-08-14T00:00:00"),
            },
            {
                "time_max": datetime.fromisoformat("2022-08-30T00:00:00"),
                "time_min": datetime.fromisoformat("2022-08-28T00:00:00"),
            },
        ]
        self.assertEqual(result, expected)

    def test_chunk_time_series_small_time_frame(self):
        time_min = datetime.fromisoformat("2022-07-30")
        time_max = datetime.fromisoformat("2022-08-30")
        result = chunk_time_series(time_min, time_max, chunk_size=28)
        expected = [
            {
                "time_min": datetime.fromisoformat("2022-07-30T00:00:00"),
                "time_max": datetime.fromisoformat("2022-08-30T00:00:00"),
            },
        ]
        self.assertEqual(result, expected)

    def test_chunk_time_series_dates_with_times(self):
        time_min = datetime.fromisoformat("2021-01-24T00:00:00")
        time_max = datetime.fromisoformat("2021-06-30T23:59:59.999999")
        result = chunk_time_series(time_min, time_max, chunk_size=15)
        expected = [
            {
                "time_min": datetime.fromisoformat("2021-01-24T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-02-08T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-02-09T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-02-23T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-02-24T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-03-10T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-03-11T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-03-25T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-03-26T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-04-09T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-04-10T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-04-24T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-04-25T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-05-09T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-05-10T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-05-24T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-05-25T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-06-08T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-06-09T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-06-23T23:59:59.999999"
                ),
            },
            {
                "time_min": datetime.fromisoformat("2021-06-24T00:00:00"),
                "time_max": datetime.fromisoformat(
                    "2021-06-30T23:59:59.999999"
                ),
            },
        ]
        self.assertEqual(result, expected)

    def test_invalid_time_min(self):
        with self.assertRaises(ValueError):
            chunk_time_series("invalid-date", "2022-08-30", chunk_size=14)

    def test_time_max_before_time_min(self):
        with self.assertRaises(ValueError):
            time_min = datetime.fromisoformat("2022-08-30")
            time_max = datetime.fromisoformat("2022-07-30")
            chunk_time_series(time_min, time_max, chunk_size=14)

    def test_chunk_size_zero(self):
        with self.assertRaises(ValueError):
            time_min = datetime.fromisoformat("2022-07-30")
            time_max = datetime.fromisoformat("2022-08-30")
            chunk_time_series(time_min, time_max, chunk_size=0)

    def test_chunk_size_negative(self):
        with self.assertRaises(ValueError):
            time_min = datetime.fromisoformat("2022-07-30")
            time_max = datetime.fromisoformat("2022-08-30")
            chunk_time_series(time_min, time_max, chunk_size=-14)

    def test_same_date_time_frame(self):
        time_min = datetime.fromisoformat("2022-07-30")
        time_max = datetime.fromisoformat("2022-07-30")
        result = chunk_time_series(time_min, time_max, chunk_size=14)
        expected = [
            {
                "time_min": datetime.fromisoformat("2022-07-30T00:00:00"),
                "time_max": datetime.fromisoformat("2022-07-30T00:00:00"),
            }
        ]
        self.assertEqual(result, expected)

    def test_chunk_size_apart(self):
        time_min = datetime.fromisoformat("2022-07-30")
        time_max = datetime.fromisoformat("2022-08-13")
        result = chunk_time_series(time_min, time_max, chunk_size=14)
        expected = [
            {
                "time_min": datetime.fromisoformat("2022-07-30T00:00:00"),
                "time_max": datetime.fromisoformat("2022-08-13T00:00:00"),
            }
        ]
        self.assertEqual(result, expected)

    def test_default_chunk_size(self):
        time_min = datetime.fromisoformat("2022-07-30")
        time_max = datetime.fromisoformat("2022-08-19")
        result = chunk_time_series(time_min, time_max)
        self.assertEqual(len(result), 1)
