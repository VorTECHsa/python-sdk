from semver import VersionInfo

from vortexasdk.version import __version__
from vortexasdk.version_utils import get_latest_sdk_version


def check_proposed_version_is_allowed(
    latest_version: str, proposed_version: str
) -> None:
    """Check that the proposed version is a valid incremental semver version, or a prerelease."""

    latest = VersionInfo.parse(latest_version)
    proposed = VersionInfo.parse(proposed_version)

    next_versions = {
        latest.bump_major(),
        latest.bump_minor(),
        latest.bump_patch(),
    }

    proposed_version_is_allowed = (
        proposed in next_versions or proposed.prerelease is not None
    )

    if not proposed_version_is_allowed:
        raise Exception(
            f"The proposed version {proposed} is not allowed. This might be because the proposed version "
            f"already exists, or it isn't one of the next sequential semver version bumps. The next version must be a "
            f"prerelease/build, or one of the following: "
            f"{[str(v) for v in next_versions]}"
        )


if __name__ == "__main__":
    check_proposed_version_is_allowed(
        latest_version=get_latest_sdk_version(), proposed_version=__version__
    )
