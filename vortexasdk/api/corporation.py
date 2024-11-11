from typing import List, Optional


from vortexasdk.api.shared_types import (
    EntityWithSingleLayerAndProbability,
    IDName,
)


class Corporation(IDName):
    """Represent a Corporation reference record returned by the API."""

    corporate_entity_type: Optional[List[str]] = None
    ref_type: Optional[str] = None
    leaf: Optional[bool] = None
    parent: Optional[List[str]] = None


class CorporateEntity(EntityWithSingleLayerAndProbability):
    """
    Represents a relationship between a corporation and another entity like a vessel.

    [Corporate Entity Further Documentation](https://docs.vortexa.com/reference/intro-corporate-entities)


    """
