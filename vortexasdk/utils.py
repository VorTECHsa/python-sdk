def to_list(a) -> list:
    """Convert wraps element in list if element isn't a list already."""
    if a is None:
        return []
    elif isinstance(a, list):
        return a
    else:
        return [a]


def convert_values_to_list(data: dict) -> dict:
    """Convert each value to a list."""
    return {k: to_list(v) for k, v in data.items()}
