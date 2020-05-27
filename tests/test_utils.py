from unittest import TestCase
from distutils.version import StrictVersion

from vortexasdk.utils import (
    convert_to_list,
    convert_values_to_list,
    get_latest_package_version,
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

    def test_get_latest_package_version(self):
        pd_old_version = "0.25.3"

        lv, _ = get_latest_package_version("pandas")

        assert lv > StrictVersion(pd_old_version)
