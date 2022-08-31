from typing import Optional
from pydantic import BaseModel

from vortexasdk.api.id import ID


class AggregationBreakdownItem(BaseModel):
    """
    Generic container class holding a `id <> value` pair, a `count` a `label`.

    For example, this class could hold a number of vessels (`value`) in East Asia ('label') with id of "212fb4cfc862391f" (`id`) and the number of voyages in this location (count).

    If the `AggregationBreakdownItem` is enriched by reference data (e.g. in `/voyages/top-hits`), `id` is the short ID of the reference entity, `label` holds its name
    and `value` and `count` correspond to numeric values of the returned record.
    """

    id: ID
    count: Optional[int] = None
    value: Optional[float] = None
    label: Optional[str] = None
