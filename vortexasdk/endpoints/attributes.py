"""Attributes Endpoint."""
from typing import List, Union
from vortexasdk.endpoints.endpoints import ATTRIBUTES_REFERENCE
from vortexasdk.endpoints.attributes_result import AttributeResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class Attributes(Reference, Search):
    """
        Attributes endpoint.

        An Attribute is a reference value that corresponds to an ID associated with other entities.

        For example, a vessel object from the Vessel reference endpoint may have the following keys:

        ```json
        {
            "ice_class": "b09ed4e2bd6904dd",
            "propulsion": "3ace0e050724707b"
        }
        ```

        These IDs represent attributes which can be found via the Attributes reference endpoint.

        When the attributes endpoint is searched with those ids as parameters:

        ```python
            >>> from vortexasdk import Attributes
            >>> df = Attributes().search(ids=["b09ed4e2bd6904dd", "3ace0e050724707b"]).to_df()

        ```

        Returns

        |    | id               | type       | label    |
        |---:|:-----------------|:-----------|:---------|
        |  0 | b09ed4e2bd6904dd | ice_class  | UNKNOWN  |
        |  1 | 3ace0e050724707b | propulsion | DFDE     |


    """

    def __init__(self):
        Reference.__init__(self, ATTRIBUTES_REFERENCE)
        Search.__init__(self, ATTRIBUTES_REFERENCE)

    def load_all(self) -> AttributeResult:
        """
            Load all attributes.
        """
        return self.search()

    # noinspection PyShadowingBuiltins
    def search(
        self,
        type: str = None,
        term: Union[str, List[str]] = None,
        ids: Union[str, List[str]] = None,
    ) -> AttributeResult:
        """
        Find all attributes matching given type.

        # Arguments
            type: The type of attribute we're filtering on. Type can be: `ice_class`, `propulsion`, `scrubber`

        # Returns
        List of attributes matching `type`


        # Examples

        Find all attributes with a type of `ice_class`.
        ```python
        >>> from vortexasdk import Attributes
        >>> df = Attributes().search(type="scrubber").to_df()

        ```
        returns

        |    | id               | name       | type        |
        |---:|:-----------------|:-----------|:------------|
        |  0 | 14c7b073809eb565 | Open Loop  | scrubber    |
        |  1 | 478fca39000c49d6 | Unkown     | scrubber    |

        """

        search_params = {
            "term": [str(e) for e in convert_to_list(term)],
            "ids": convert_to_list(ids),
            "type": type,
        }

        return AttributeResult(super().search(**search_params))
