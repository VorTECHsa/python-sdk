from typing import List

from python_sdk.constants import CHARTERERS_REFERENCE, GEOGRAPHIES_REFERENCE, VESSELS_REFERENCE
from python_sdk.operations import Reference, Search


class Geographies(Reference, Search):

    def __init__(self):
        Reference.__init__(self, GEOGRAPHIES_REFERENCE)
        Search.__init__(self, GEOGRAPHIES_REFERENCE)

    def search(self, term):
        """

        # Arguments
            term: The geography name we're filtering on

        # Returns
        List of geographies matching `term`


        # Examples

            >>> [x["name"] for x in Geographies().search(term="portsmouth")]
            ['Portsmouth [GB]', 'Portsmouth, NH [US]']

        """

        search_params = {"term": term}
        return super().search(**search_params)


class Charterers(Reference, Search):

    def __init__(self):
        Reference.__init__(self, CHARTERERS_REFERENCE)
        Search.__init__(self, CHARTERERS_REFERENCE)

    def search(self, term):
        """

        # Arguments
            term: The charterer name we're filtering on

        # Returns
        List of charterers matching `term`


        # Examples

            >>> [x["name"] for x in Charterers().search(term="do")]
            ['Donsotank', 'Dorval SC']

        """

        search_params = {"term": term}
        return super().search(**search_params)


class Vessels(Reference, Search):

    def __init__(self):
        Reference.__init__(self, VESSELS_REFERENCE)
        Search.__init__(self, VESSELS_REFERENCE)

    def search(self,
               term: str = None,
               ids: List[str] = None,
               vessel_classes=None,
               vessel_product_types: List[str] = None):
        """

        # Arguments
            term: The name (or partial name) of a vessel we'd like to search
            ids: List of IDS of vessels we'd like to search
            vessel_classes: List of #::python_sdk.api.resources.vessel.VesselClass
            vessel_product_types: List of product IDs, searching vessels currently (or recently) carrying these products.

        # Returns
        List of vessels matching the search arguments.


        # Examples

        ```python
        >>> Vessels.search(vessel_classes=[VesselClass.aframax, VesselClass.handymax],
                 vessel_product_types=["6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"])
        ```
        """

        if vessel_classes is None:
            vessel_classes = []

        search_params = {
            "term": term,
            "ids": ids,
            "vessel_classes": [v.name for v in vessel_classes],
            "vessel_product_types": vessel_product_types,
        }

        return super().search(**search_params)


class Products(Reference):

    def __init__(self):
        super().__init__("")
