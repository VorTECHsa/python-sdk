from typing import Dict, List, Union
from datetime import datetime, timedelta


def chunk_time_series(
    time_min: datetime, time_max: datetime, chunk_size: int = 30
):
    """split the date range to smaller chunks"""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    if time_min > time_max:
        raise ValueError("time_min must be before time_max")

    days_in_time_series = (time_max - time_min).days

    chunked_time_series = []

    if days_in_time_series < chunk_size * 2:
        return [{"time_min": time_min, "time_max": time_max}]

    max_time_min = days_in_time_series - chunk_size
    should_add_last_chunk = False

    for i in range(0, max_time_min, chunk_size):
        new_time_min = time_min if i == 0 else time_min + timedelta(days=i + 1)
        new_time_min = new_time_min.replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        new_time_max = time_min + timedelta(days=i + chunk_size)
        new_time_max = new_time_max.replace(
            hour=23, minute=59, second=59, microsecond=999999
        )

        chunked_time_series.append(
            {
                "time_min": new_time_min,
                "time_max": new_time_max,
            }
        )

        should_add_last_chunk = time_max > new_time_max

    if should_add_last_chunk > 0:
        new_time_min = chunked_time_series[-1]["time_max"] + timedelta(days=1)
        new_time_min = new_time_min.replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        chunked_time_series.append(
            {
                "time_min": new_time_min,
                "time_max": time_max,
            }
        )

    return chunked_time_series


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
