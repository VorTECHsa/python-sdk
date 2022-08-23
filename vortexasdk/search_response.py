from typing import Any, Dict, List

from typing_extensions import TypedDict


class SearchResponse(TypedDict):
    reference: Dict[str, Any]
    data: List
