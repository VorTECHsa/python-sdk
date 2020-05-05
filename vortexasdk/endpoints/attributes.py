"""Attributes Endpoint."""
from typing import List, Union
from vortexasdk.endpoints.endpoints import ATTRIBUTES_REFERENCE
from vortexasdk.endpoints.attributes_result import AttributeResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class Attributes(Reference, Search):
    """Attributes endpoint."""

    def __init__(self):
        Reference.__init__(self, ATTRIBUTES_REFERENCE)
        Search.__init__(self, ATTRIBUTES_REFERENCE)

    def load_all(self) -> AttributeResult:
        """Load all attributes."""
        return self.search()

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
        >>> df = Attributes().search(type="ice_class").to_df()

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
