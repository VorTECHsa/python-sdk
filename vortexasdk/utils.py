from typing import Dict, List, Union


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


def filter_exact_match(
    allowed_name: Union[str, List[str]], search_result: List[Dict]
) -> List[Dict]:
    """
    Filter search results on items with exact matching names.

    # Arguments
        allowed_name: An allowed name, or list of allowed names
        search_result: A list of dictionaries. Each dictionary must contain the key "name".

    """
    allowed_names_list = convert_to_list(allowed_name)
    return [s for s in search_result if s["name"] in allowed_names_list]


def filter_empty_values(data: Dict) -> Dict:
    return {
        k: v for k, v in data.items() if not (v is None or v == [] or v == {})
    }


def sts_param_value(param):
    """
    If sts filter is True, apply cross filter.

    If sts filter is False, apply exclude param.

    Else - don't apply any filters
    """
    if param == True:
        return {"exclude": False, "x_filter": True}
    elif param == False:
        return {"exclude": True, "x_filter": False}
    else:
        return {"exclude": False, "x_filter": False}
