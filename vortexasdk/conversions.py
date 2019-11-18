from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.id import split_ids_names
from vortexasdk.endpoints.charterers import Charterers
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.vessels import Vessels
from vortexasdk.operations import Search


def convert_to_geography_ids(ids_or_names_list: List[Union[ID, str]]) -> List[ID]:
    """
    Convert a mixed list of names or IDs to geography ids.

    # Example
    ```
        >>> convert_to_geography_ids(["Rotterdam [NL]"])
    ['3a063ec309f2fe486ca3d2e58b61d683b514a3bfd0b87d91984f43d9ee5071fb', '95d76e403920bf0b2ffc49b7439fd8a9b376980e8ab37241b4581549f50afca2',...]
    ```

    # Example
    ```
        >>> convert_to_geography_ids(["Rotterdam [NL]", "b514a3bfd0b87d91984f43d9ee5071fb3a063ec309f2fe486ca3d2e58b61d683"])
    ['b514a3bfd0b87d91984f43d9ee5071fb3a063ec309f2fe486ca3d2e58b61d683', '95d76e403920bf0b2ffc49b7439fd8a9b376980e8ab37241b4581549f50afca2',...]
    ```

    """
    return _convert_to_ids(ids_or_names_list, Geographies())


def convert_to_charterer_ids(ids_or_names_list: List[Union[ID, str]]) -> List[ID]:
    """
    Convert a mixed list of names or IDs to charterer ids.

    # Example
    ```
        >>> convert_to_charterer_ids(["Exon"])
    ['e486ca3d2e58b61d683b5143a063ec309f2fa3bfd0b87d91984f43d9ee5071fb',...]
    ```
    """
    return _convert_to_ids(ids_or_names_list, Charterers())


def convert_to_vessel_ids(ids_or_names_list: List[Union[ID, str]]) -> List[ID]:
    """
    Convert a mixed list of names or IDs to vessel ids.

    # Example
    ```
        >>> convert_to_vessel_ids(["Stallion"])
    ['e486ca3d2e58b61d683b5143a063ec309f2fa3bfd0b87d91984f43d9ee5071fb',...]
    ```
    """
    return _convert_to_ids(ids_or_names_list, Vessels())


def _convert_to_ids(ids_or_names_list: List[Union[ID, str]], searcher: Search) -> List[ID]:
    """Convert list containing a mix of IDs and names to a list of IDs."""
    ids, names = split_ids_names(ids_or_names_list)
    if len(names) == 0:
        return ids
    else:
        return ids + _search_ids(names, searcher)


def _search_ids(names, searcher: Search) -> List[ID]:
    results = searcher.search(term=names)

    id_to_name = {r['id']: r['name'] for r in results}

    print(f'Searched term: {names},'
          f' found {len(results)} {searcher.__class__.__name__}'
          f' : {id_to_name}')

    return list(id_to_name.keys())
