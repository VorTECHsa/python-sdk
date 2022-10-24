"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fproducts.ipynb)
"""
from typing import Any, Dict, List, Union

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
        filter_layer: str = None,
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

            filter_layer: Must be one of product types ['group', 'group_product', 'category', 'grade'].

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
        api_params: Dict[str, Any] = {
            "term": convert_to_list(term),
            "ids": convert_to_list(ids),
            "product_parent": convert_to_list(product_parent),
            "allowTopLevelProducts": True,
            "filter_layer": convert_to_list(filter_layer),
        }

        response = super().search_with_client(
            exact_term_match=exact_term_match, **api_params
        )

        return ProductResult(
            records=response["data"], reference=response["reference"]
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
