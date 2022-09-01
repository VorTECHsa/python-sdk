from abc import ABC
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Union

from vortexasdk.api.id import ID

IDsNames = Union[List[Union[ID, str]], str, ID]

ISODate = str


# noinspection PyPep8Naming
def to_ISODate(utc_datetime: datetime) -> ISODate:
    return utc_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def to_ISODate_Array(days: List[datetime]) -> List[ISODate]:
    return [to_ISODate(date) for date in days]


class EntityWithSingleLayer(BaseModel):
    """Holds commonly used properties."""

    id: ID
    layer: Optional[str] = None
    label: Optional[str] = None


class EntityWithSingleLayerAndTimespan(BaseModel):
    id: ID
    layer: Optional[str] = None
    label: Optional[str] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


class EntityWithListLayer(BaseModel):
    """Holds commonly used properties."""

    id: ID
    layer: Optional[List[str]] = None
    label: Optional[str] = None


class EntityWithSingleLayerAndProbability(BaseModel):
    """
    Extension of `Entity`, containing additional properties.

    - `probability` the probability of an entity occurring.
    - `source` the source of this entity, (is typically one of `['model', 'external_data']`
    """

    id: ID
    probability: Optional[float] = None
    source: Optional[str] = None
    layer: Optional[str] = None
    label: Optional[str] = None


class EntityWithListLayerAndProbability(BaseModel):
    """
    Extension of `Entity`, containing additional properties.

    - `probability` the probability of an entity occurring.
    - `source` the source of this entity, (is typically one of `['model', 'external_data']`
    """

    id: ID
    probability: Optional[float] = None
    source: Optional[str] = None
    layer: Optional[List[str]]
    label: Optional[str] = None


class IDName(BaseModel):
    """Tuple containing `id` and `name`."""

    id: ID
    name: Optional[str] = None


class IDLayer(BaseModel):
    """Tuple containing `id` and `layer`."""

    id: ID
    layer: Optional[str] = None
    label: Optional[str] = None


class IDNameLayer(BaseModel):
    """Triple holding `id`, `name`, and `layer`."""

    id: ID
    layer: Optional[List[str]] = None
    name: Optional[str] = None


class Node(ABC, IDName, BaseModel):
    """
    Abstract Base Class holding a node of a tree.

    # Attributes:
        ref_type: Optional[Identifies the reference type data] = None
        leaf: Is this node a leaf of the hierarchical tree?
        parent: List of parents

    """

    ref_type: Optional[str] = None
    leaf: Optional[bool] = None
    parent: Optional[List[IDNameLayer]] = None


class Tag(BaseModel):
    """

    Represents a property that is associated with a period of time.

    A good example is if a vessel has acted as an FSO during a time period.

    [Tags Further Documentation](https://docs.vortexa.com/reference/intro-tags)

    """

    tag: Optional[str] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


class Flag(BaseModel):
    """

    Represents a property that is associated with a vessel's flag.

    - `flag` key will be a Geography Entity ID.
    - `flag_country` key will be the ISO code for the country

    [Geography Entity Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)

    """

    tag: Optional[str] = None
    flag: Optional[str] = None
    flag_country: Optional[str] = None


class Scrubber(BaseModel):
    """

    Represents information about scrubbers fitted to a vessel.

    - `scrubber` key will be the type of scrubber.
    - `planned` key is if this scrubber has not yet been fitted but is planned.

    An empty `scrubber` List may mean the scrubber status is unknown or a vessel has none fitted.

    """

    tag: Optional[str] = None
    scrubber: Optional[str] = None
    planned: Optional[bool] = None
