from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.id import split_ids_other
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search

logger = get_logger(__name__)


def _convert_to_ids(
    ids_or_names_list: List[Union[ID, str]], searcher: Search
) -> List[ID]:
    """Convert list containing a mix of IDs and names to a list of IDs."""
    ids, others = split_ids_other(ids_or_names_list)
    if len(others) == 0:
        return ids
    else:
        return ids + _search_ids(searcher, term=others)


def _search_ids(searcher: Search, **kwargs) -> List[ID]:
    """Find IDs matching a given list of search terms."""
    results = searcher.search(**kwargs)

    id_to_name = {r["id"]: r["name"] for r in results}

    logger.info(
        f"Searched term: {kwargs.items()},"
        f" found {len(results)} {searcher.__class__.__name__}"
        f" : {id_to_name}"
    )

    return list(id_to_name.keys())
