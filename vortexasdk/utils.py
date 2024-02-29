from typing import Any, Dict, List, Optional, Union
from enum import Enum
from datetime import datetime, timedelta


def is_arrival_or_departure_mode(
    voyage_date_range_activity: Optional[str] = None,
):
    """
    When the mode is arrival or departure, we do not need a multi-state aggregation
    This is because the arrival and departure doesn't need daily granularity,
    because they are determined by only one type of event.

    The breakdowns on departures and arrivals are the resume of the voyages properties and
    do not require a daily progression to be displayed.

    E.g. In arrival or departure, the tonne miles or the avg distance are the max value that voyage have.
    indifferently of the moment when the cargo was loaded or unloaded.
    """
    return (
        voyage_date_range_activity is not None
        and voyage_date_range_activity in ["arrivals", "departures"]
    )


def is_breakdown_property_multi_state(
    breakdown_property: Optional[str] = None,
    breakdown_split_property: Optional[str] = None,
) -> bool:
    """
    Check if the breakdown property should be considered as multi-state
    Some breakdowns should be considered as multi-state even to ensure consistency in the data
    """
    if breakdown_property is None:
        return False

    """
        Some breakdowns should always be considered as multi-state to ensure consistency in the data.
        E.G. AvgSpeed and AvgDistance because they require daily granularity
        """
    if breakdown_property in [
        "cargo_quantity",
        "avg_wait_time",
        "dwt",
        "cubic_capacity",
    ]:
        return True

    """
        Some breakdowns should be considered as multi-state only when a valid breakdown split is provided
        Tonne miles aggregations are multi-state when the breakdown is by tonne miles
        and the split property is not "none", because the split require an aggregation accessing the
        nested "metrics" property of the cargo events twice.
        """
    if (
        breakdown_property in ["tonne_miles", "avg_distance", "avg_speed"]
        and breakdown_split_property is not None
        and breakdown_split_property != "none"
    ):
        return True

    return False


def is_multi_state(api_params: Dict[str, Any]) -> bool:
    """
    Some states (e.g. cargo_status, commitment_status) will change across the timespan of a voyage,
    when we are filtering in the aggregation stage, we cannot determine multiple states when just looking at 1 event.
    So what we need to do is to split the aggregation by 1 day, then only valid voyages will be filtered in the query stage,
    and we don't need to do filtering in aggregation stage anymore.

                       |-- day1 --|-- day2 --|-- day3 --|-- day4 --|-- day5  --|
    Movement status:   |--- Moving ------|----waiting--|----- Moving ----------| from movement status event
    Commitment status: |---unknown---------------|--------committed------------| from commitment status event
    Location status:   |------- on the sea -------------------|------berth-----| from location status event
    """

    """
        If the mode is arrival or departure, we do not need a multi-state aggregation
        no matter the other filters provided.
        """
    if is_arrival_or_departure_mode(
        api_params.get("voyage_date_range_activity")
    ):
        return False

    """
        If some breakdown properties are provided, we need to do a multi-state aggregation
        """
    if is_breakdown_property_multi_state(
        api_params.get("breakdown_property"),
        api_params.get("breakdown_split_property"),
    ):
        return True

    effective_state_params_count = 0

    """
        These filters are determined by the cargo events, that means that the combination of all the filters
        will determine if a multi state by cargo info is required.
        """
    if (
        api_params.get("origins")
        or api_params.get("destinations")
        or api_params.get("products")
    ):
        effective_state_params_count += 1

    # exclusions are not needed because they will be handled at the filter level
    state_param_keys = [
        "cargo_status",
        "location_status",
        "movement_status",
        "commitment_status",
        "locations",
    ]

    for key in state_param_keys:
        if api_params.get(key):
            effective_state_params_count += 1

    return effective_state_params_count > 1


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


class PAGINATION_STRATEGIES(Enum):
    OFFSET = "OFFSET"
    SEARCH_AFTER = "SEARCH_AFTER"
