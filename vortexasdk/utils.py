from typing import Dict, List
import json
from urllib.request import urlopen
from distutils.version import StrictVersion, LooseVersion


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


def get_latest_package_version(package_name: str):
    """
    Retrieves the latest SDK version from PyPI and compares with the currently installed SDK version.
    """
    url = f"https://pypi.python.org/pypi/{package_name}/json"
    with urlopen(url) as u:
        data = json.loads(u.read())

    try:
        versions = data["releases"].keys()
    except KeyError:
        raise KeyError("No version related key found in PyPI")

    try:
        versions = sorted(versions, key=StrictVersion)
    except ValueError as e:
        if "invalid version number" in str(e):
            versions = sorted(versions, key=LooseVersion)
        else:
            raise e

    latest_version = versions[-1]

    return latest_version, versions
