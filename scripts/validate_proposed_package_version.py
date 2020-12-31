from distutils.version import StrictVersion

from vortexasdk.version import __version__
from vortexasdk.version_utils import get_latest_sdk_version


def check_proposed_version_is_allowed(
        latest_version: str, proposed_version: str
) -> None:
    """Check that the proposed version is a valid future semver version, or a prerelease."""

    print(f"Latest version:  {latest_version}")
    print(f"Proposed version {proposed_version}")

    try:
        latest = StrictVersion(latest_version)
        proposed = StrictVersion(proposed_version)

        assert proposed > latest
    except Exception as e:
        raise Exception(
            f"The proposed version {proposed_version} is not allowed. "
            f"This might be because the proposed version already exists, or because it isn't valid semver. "
            f"Valid versions are of the form X.Y.Z. Pre-releases take the form X.Y.Z.a1, X.Y.Z.a2 "
            f"You must change the vortexasdk/__version__.py file to a valid next version, following semver guidelines. "
            f"Refer to https://semver.org for more information on semantic versioning.", e
        )

    print(f"Proposed version {proposed_version} is allowed")


if __name__ == "__main__":
    check_proposed_version_is_allowed(
        latest_version=get_latest_sdk_version(), proposed_version=__version__
    )
