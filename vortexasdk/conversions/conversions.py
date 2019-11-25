from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.id import split_ids_names
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search

logger = get_logger(__name__)


def _convert_to_ids(
    ids_or_names_list: List[Union[ID, str]], searcher: Search
) -> List[ID]:
    """Convert list containing a mix of IDs and names to a list of IDs."""
    ids, names = split_ids_names(ids_or_names_list)
    if len(names) == 0:
        return ids
    else:
        return ids + _search_ids(names, searcher)


def _search_ids(names: List[str], searcher: Search) -> List[ID]:
    """Find IDs matching a given list of names."""
    results = searcher.search(term=names)

    id_to_name = {r["id"]: r["name"] for r in results}

    logger.debug(
        f"Searched term: {names},"
        f" found {len(results)} {searcher.__class__.__name__}"
        f" : {id_to_name}"
    )

    return list(id_to_name.keys())
