"""Products Endpoint."""
from typing import List, Union

from vortexasdk.api.shared_types import ID
from vortexasdk.endpoints.endpoints import PRODUCTS_REFERENCE
from vortexasdk.endpoints.products_result import ProductResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import to_list


class Products(Reference, Search):
    """Vessels endpoint."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, PRODUCTS_REFERENCE)
        Search.__init__(self, PRODUCTS_REFERENCE)

    def search(self,
               term: Union[str, List[str]] = None,
               ids: Union[str, List[str]] = None,
               product_parent: Union[str, List[str]] = None,
               ) -> ProductResult:
        """
        Find all products matching given search terms.

        # Arguments
            term: The name(s) (or partial name(s)) of a product we'd like to search

            ids: ID or IDs of products we'd like to search

            product_parent: ID, or list of IDs of the immediate product parent. E.g. `product_parent ='12345'` will return all children of product `12345`.

        # Returns
        List of products matching the search arguments.


        # Examples

        Let's find all the products with 'sul' in their name, or related names.

        ```python
        >>> from vortexasdk import Products
        >>> Products().search(term='sul').to_df()
        ```

        |    | id         |     name   |             parent                     |
        |---:|:-----------|------------|---------------------------------------:|
        |  0 | 'a250444...| Marlim Sul |[{'name': 'Heavy-Sour', 'layer': ['su...|


        Note the `term` search also looks for products with matching `related_names`


        # Further Documentation

        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/POST/reference/products)

        """
        search_params = {
            "term": to_list(term),
            "ids": to_list(ids),
            "product_parent": to_list(product_parent),
            "allowTopLevelProducts": True
        }

        return ProductResult(super().search(**search_params))

    def reference(self, id: ID):
        """
        Perform a product lookup.

        # Arguments
            id: Product ID to lookup

        # Returns
        Product record matching the ID

        # Further Documentation:
        [VortexaAPI Product Reference](https://docs.vortexa.com/reference/POST/reference/products)

        """
        return super().reference(id)
