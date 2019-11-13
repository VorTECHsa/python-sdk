"""Products Endpoint."""
from vortexasdk.operations import Reference
import jsons
import pandas as pd
from vortexa.api.shared_types import ID
from vortexa.api.product import Product
from vortexa.endpoints.endpoints import PRODUCTS_REFERENCE
from vortexa.operations import Reference, Search
from vortexa.api.search_result import Result
from vortexa.utils import convert_values_to_list


class ProductResult(Result):
    """Container class that holds the result obtained from calling the `Product` endpoint."""

    def to_list(self) -> List[Product]:
        """Represent products as a list."""
        list_of_dicts = super().to_list()
        return jsons.loads(jsons.dumps(list_of_dicts), List[Product])

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent products as a `pd.DataFrame`.

        # Arguments
            columns: The product features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name']`.


        # Returns
        `pd.DataFrame` of products.

        """
        if columns is None:
            columns = ['id', 'name']

        df = pd.DataFrame(super().to_list())

        if columns == 'all':
            return df
        else:
            return df[columns]



class Products(Reference):
    """Not implemented yet."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, PRODUCTS_REFERENCE)
        Search.__init__(self, PRODUCTS_REFERENCE)

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

    def search(self,
               term: Union[str, List[str]] = None,
               ids: Union[str, List[str]] = None,
               #vessel_classes: Union[str, List[str]] = None,
               #vessel_product_types: Union[str, List[str]] = None,
               ) -> ProductResult:
        """
        Find all products matching given search terms.

        # Arguments
            term: The name(s) (or partial name(s)) of a product we'd like to search

            ids: ID or IDs of products we'd like to search

        # Returns
        List of vessels matching the search arguments.


        # Examples

        Let's find all the products with 'sul' in their name, or related names.

        ```python
        >>> Products().search(term='sul').to_df(columns='all')
        ```

        |    | id         |     name |
        |---:|:-------------|--------:|
        |  0 | 'a250444936b94aadb... | Marlim Sul |


        Note the `term` search also looks for products with matching `related_names`


        # Further Documentation

        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/POST/reference/products)

        """
        search_params = convert_values_to_list({
            "term": term,
            "ids": ids,
        })

        return ProductResult(super().search(**search_params))
