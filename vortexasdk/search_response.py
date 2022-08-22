from typing import Any, Dict, List

from typing import TypedDict


class SearchResponse(TypedDict):
    reference: Dict[str, Any]
    data: List
