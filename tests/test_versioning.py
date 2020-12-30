from unittest import TestCase
from distutils.version import LooseVersion

from vortexasdk.version_utils import (
    get_latest_sdk_version,
)


class TestVersionUtils(TestCase):
    def test_get_latest_sdk_version(self):
        sdk_old_version = "0.18.0"

        lv = get_latest_sdk_version()

        assert lv > LooseVersion(sdk_old_version)
