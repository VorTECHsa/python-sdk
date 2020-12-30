import json
from urllib.request import urlopen
from distutils.version import LooseVersion
from vortexasdk import __name__ as sdk_pkg_name
from vortexasdk.version import __version__


def get_latest_sdk_version() -> str:
    """Retrieves the latest SDK version from PyPI."""
    url = f"https://pypi.python.org/pypi/{sdk_pkg_name}/json"
    with urlopen(url) as u:
        data = json.loads(u.read())

    versions = data["releases"].keys()
    sorted_versions = sorted(versions, key=LooseVersion)
    latest_version = sorted_versions[-1]

    return latest_version


def is_sdk_version_outdated():
    """Checks whether SDK version is outdated."""
    latest_version = get_latest_sdk_version()
    if LooseVersion(__version__) < latest_version:
        return latest_version, True
    else:
        return latest_version, False


