from unittest import TestCase

from scripts.validate_proposed_package_version import (
    check_proposed_version_is_allowed,
)


class TestVersionProposal(TestCase):
    def test_incremental_bump_is_allowed(self):
        check_proposed_version_is_allowed("0.18.0", "1.0.0")

    def test_incremental_minor_is_allowed(self):
        check_proposed_version_is_allowed("0.18.0", "0.19.0")

    def test_incremental_patch_is_allowed(self):
        check_proposed_version_is_allowed("0.18.0", "0.18.1")

    def test_prerelease_is_allowed(self):
        check_proposed_version_is_allowed("0.18.0", "0.18.1a1")

    def test_non_semver_is_not_allowed(self):
        self.assertRaises(
            Exception,
            lambda: check_proposed_version_is_allowed("1.18.0", "foobar"),
        )

    def test_old_major_is_not_allowed(self):
        self.assertRaises(
            Exception,
            lambda: check_proposed_version_is_allowed("1.18.0", "0.18.0"),
        )

    def test_old_minor_is_not_allowed(self):
        self.assertRaises(
            Exception,
            lambda: check_proposed_version_is_allowed("0.18.0", "0.17.0"),
        )

    def test_old_bump_is_not_allowed(self):
        self.assertRaises(
            Exception,
            lambda: check_proposed_version_is_allowed("0.18.1", "0.18.0"),
        )
