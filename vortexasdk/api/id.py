import re
from typing import List, Tuple

ID = str


def is_valid_id(string: str) -> bool:
    """Check string is valid SHA256 hash."""
    return re.match("^[A-Fa-f0-9]{64}$", string) is not None


def split_ids_names(names_or_ids: List) -> Tuple[List[ID], List[str]]:
    """Extract IDs and names from a list, returning a list of IDs, and a list of names."""
    ids = []
    names = []

    for item in names_or_ids:
        if is_valid_id(item):
            ids.append(item)
        else:
            names.append(item)

    return ids, names
