from distutils.version import StrictVersion

from vortexasdk.version import __version__
from vortexasdk.version_utils import get_latest_sdk_version


def check_proposed_version_is_allowed(
    latest_version: str, proposed_version: str
) -> None:
    """Check that the proposed version is a valid future semver version, or a prerelease."""

    latest = StrictVersion(latest_version)
    proposed = StrictVersion(proposed_version)

    if proposed < latest:
        raise Exception(
            f"The proposed version {proposed} is not allowed. \n"
            f"This might be because the proposed version already exists, or because it isn't valid semver.\n"
            f"Valid versions are of the form X.Y.Z. Pre-releases take the form X.Y.Z.a1, X.Y.Z.a2 \n"
            f"You must change the vortexasdk/__version__.py file to a valid next version, following semver guidelines.\n"
            f"Refer to https://semver.org for more information on semantic versioning."
        )
    else:
        print(f"Latest version:  {latest_version}")
        print(f"Proposed version {proposed_version} is allowed.")


if __name__ == "__main__":
    check_proposed_version_is_allowed(
        latest_version=get_latest_sdk_version(), proposed_version=__version__
    )
