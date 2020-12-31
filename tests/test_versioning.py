from distutils.version import StrictVersion
from unittest import TestCase

from vortexasdk.version_utils import (
    get_latest_sdk_version,
)


class TestVersionUtils(TestCase):
    def test_get_latest_sdk_version(self):
        sdk_old_version = "0.18.0"

        assert get_latest_sdk_version() > StrictVersion(sdk_old_version)
