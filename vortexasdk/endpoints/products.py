"""Products Endpoint."""
from typing import Dict, List, Union

from vortexasdk.api.shared_types import ID
from vortexasdk.endpoints.endpoints import PRODUCTS_REFERENCE
from vortexasdk.endpoints.products_result import ProductResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class Products(Reference, Search):
    """Products endpoint."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, PRODUCTS_REFERENCE)
        Search.__init__(self, PRODUCTS_REFERENCE)

    def load_all(self) -> ProductResult:
        """Load all products."""
        return self.search()

    def search(
        self,
        term: Union[str, List[str]] = None,
        ids: Union[str, List[str]] = None,
        product_parent: Union[str, List[str]] = None,
        exact_term_match: bool = False,
    ) -> ProductResult:
        """
        Find all products matching given search terms.

        # Arguments
            term: The name(s) (or partial name(s)) of a product we'd like to search

            ids: ID or IDs of products we'd like to search

            product_parent: ID, or list of IDs of the immediate product parent. E.g. `product_parent ='12345'` will return all children of product `12345`.

            exact_term_match: By default, the SDK returns all products which name _includes_ the search term. For example, searching for "Gasoil" will return
                results including "Gasoil", "Gasoil 0.4pc", "Gasoil 500ppm" etc. Setting `exact_search_match` to true ensure that only exact term matches are
                returned, ie just "Gasoil" in this case.

        # Returns
        List of products matching the search arguments.


        # Examples

        Let's look for products with in one of `['diesel', 'fuel oil', 'grane']` their name, or related names.

        ```python
        >>> from vortexasdk import Products
        >>> df = Products().search(term=['diesel', 'fuel oil', 'grane']).to_df('all')

        ```
        Returns

        |    | id                 | name          | layer.0   | leaf   | parent.0.name   | parent.0.layer.0   | parent.0.id       |   meta.api_min |   meta.api_max | ref_type   |   meta.sulphur_min |   meta.sulphur_max |
        |---:|:-------------------|:--------------|:----------|:-------|:----------------|:-------------------|:------------------|---------------:|---------------:|:-----------|-------------------:|-------------------:|
        |  0 | 1c107b4317bc2c8... | Fuel Oil      | category  | False  | Dirty products  | product            | 5de0b00094e0fd... |        12.8878 |        12.8878 | product    |             nan    |             nan    |
        |  1 | fddedd17e02507f... | Grane         | grade     | True   | Medium-Sour     | subproduct_group   | a7e26956fbb917... |        29.2955 |        29.2955 | product    |               0.62 |               0.62 |
        |  2 | deda35eb9ca56b5... | Diesel/Gasoil | category  | False  | Clean products  | product            | b68cbb7746f8b9... |        35.9556 |        35.9556 | product    |             nan    |             nan    |


        # Further Documentation

        [VortexaAPI Product Reference](https://docs.vortexa.com/reference/POST/reference/products)

        """
        api_params = {
            "term": convert_to_list(term),
            "ids": convert_to_list(ids),
            "product_parent": convert_to_list(product_parent),
            "allowTopLevelProducts": True,
        }

        return ProductResult(
            super().search(exact_term_match=exact_term_match, **api_params)
        )

    def reference(self, id: ID) -> Dict:
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
