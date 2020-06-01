from typing import Dict, List
import json
from urllib.request import urlopen
from distutils.version import LooseVersion
from vortexasdk import __name__ as sdk_pkg_name
from vortexasdk.version import __version__


def convert_to_list(a) -> List:
    """Convert wraps element in list if element isn't a list already."""
    if a is None:
        return []
    elif isinstance(a, list):
        return a
    else:
        return [a]


def convert_values_to_list(data: Dict) -> Dict:
    """Convert each value to a list."""
    return {k: convert_to_list(v) for k, v in data.items()}


def filter_empty_values(data: Dict) -> Dict:
    return {
        k: v for k, v in data.items() if not (v is None or v == [] or v == {})
    }


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
