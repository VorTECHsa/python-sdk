def _to_list(a) -> list:
    if a is None:
        return []
    elif isinstance(a, list):
        return a
    else:
        return [a]


def convert_values_to_list(data: dict) -> dict:
    return {k: _to_list(v) for k, v in data.items()}
