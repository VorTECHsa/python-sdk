from pydantic import BaseModel
from typing import List


from vortexasdk.api.shared_types import (
    EntityWithSingleLayerAndProbability,
    IDName
)



class Corporation(IDName, BaseModel):
    """Represent a Corporation reference record returned by the API."""

    corporate_entity_type: List[str]
    ref_type: str
    leaf: bool
    parent: List[str]
    filterable: bool



class CorporateEntity(EntityWithSingleLayerAndProbability, BaseModel):
    """
    Represents a relationship between a corporation and another entity like a vessel.

    [Corporate Entity Further Documentation](https://docs.vortexa.com/reference/intro-corporate-entities)


    """
