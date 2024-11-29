import json
from urllib.request import urlopen
from packaging.version import Version
from vortexasdk import __name__ as sdk_pkg_name
from vortexasdk.version import __version__


def get_latest_sdk_version() -> str:
    """Retrieves the latest SDK version from PyPI."""
    url = f"https://pypi.python.org/pypi/{sdk_pkg_name}/json"
    with urlopen(url) as u:
        data = json.load(u)

    versions = [Version(release) for release in data["releases"].keys()]

    filtered_out_prerelease_versions = [
        v for v in versions if not v.is_prerelease
    ]

    latest_version = sorted(filtered_out_prerelease_versions)[-1]

    return str(latest_version)


def is_sdk_version_outdated():
    """Checks whether SDK version is outdated."""
    latest_version = get_latest_sdk_version()
    if Version(__version__) < Version(latest_version):
        return latest_version, True
    else:
        return latest_version, False
