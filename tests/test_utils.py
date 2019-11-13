from unittest import TestCase

from vortexasdk.utils import convert_values_to_list


class TestUtils(TestCase):
    def test_convert_values_to_list(self):
        d = {1: None, 2: "b", 3: ["c"]}

        expected = {1: [], 2: ["b"], 3: ["c"]}

        assert convert_values_to_list(d) == expected
