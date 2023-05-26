"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Ffixtures.ipynb)
"""
from vortexasdk.endpoints.fixtures_result import FixtureResult
from vortexasdk.endpoints.endpoints import FIXTURES
from vortexasdk.operations import Search
from vortexasdk.api.shared_types import to_ISODate
from datetime import datetime
from typing import Any, Dict, List, Union
from vortexasdk.api import ID
from vortexasdk.utils import convert_to_list


class Fixtures(Search):
    """Fixtures Endpoint, use this to search through Vortexa's Fixtures data.

    A detailed explanation of the fixtures can be found [here](https://docs.vortexa.com/reference/intro-fixtures).
    Limitation

    Fixtures are available through the UI, API & SDK only by permission from our shipbroker partner only.
    If we limit API access to certain products then you can only pull the fixtures data for said product e.g. CPP only, then they only have access to CPP fixtures.

    For an API key to have access to the endpoint, it needs the scopes "v.r.fix" and "v.r.ais".

    # What conditions produce a Fixture 'fulfilled' status? - Internal

    In terms of the data, we use the laycan and the mapped fixture 'origin'.

    Historical movements: The start timestamp of the loading event must be within the 5-day laycan window
    (even if the laycan window is less than 5 days, we expand it to 5), or the laycan must be within the start and end
    timestamp of the loading event and the fixture's origin hierarchy must agree with the actual loading polygon's
    hierarchy.

    Future movements: The vessel can be in the reported fixture origin within the laycan window give or take 3 days.
    We also compare the predicted destination's hierarchy with the fixture's origin hierarchy.
    An agreement (given that the previous feasibility condition is met) is a sufficient condition to create a movement.
    When there is disagreement or we don't have a predicted destination, we take into account other factors
    (e.g. if the destination is a waypoint, we treat them as agreeing).

    # Fixture status
    Fixture status indicates the point that the deal has reached in its evolution from "Subs" for vessels on subjects,
    to "Fxd" for fixed vessels or sometimes "Failed" or "FLD" for failed fixtures or sometimes "RPLC" for a
    replacement fixture or "Conf" for confirmed and "Corr" for corrected.

    #### What does the model do in the case of exact duplicates?

    - For historical movements, we don't have a particular logic.
    - For future movements, we apply our own internal sorting procedure.

    #### When we have 2 fixtures that are near exact duplicates but with different freight rates or different charterers, how does the model pick?
    - For historical movements, randomly.
    - For future movements, we apply our own internal sorting procedure.

    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, FIXTURES)

    def search(
        self,
        filter_time_field: str = "fixing_timestamp",
        filter_time_min: datetime = datetime(2020, 1, 1),
        filter_time_max: datetime = datetime(2020, 1, 2),
        ids: Union[ID, List[ID]] = None,
        filter_charterers: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_effective_controllers: Union[ID, List[ID]] = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_vessel_flags: Union[ID, List[ID]] = None,
        exclude_origins: Union[ID, List[ID]] = None,
        exclude_destinations: Union[ID, List[ID]] = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[str, List[str]] = None,
        exclude_charterers: Union[ID, List[ID]] = None,
        exclude_vessel_flags: Union[ID, List[ID]] = None,
        order: str = None,
        order_direction: str = None,
        size: int = None,
    ) -> FixtureResult:
        """
        Find Fixtures matching filters and date range.

        # Arguments
        filter_time_field: The field that the time range should be filtered against.

        filter_time_min: The UTC start date of the time filter.

        filter_time_max: The UTC end date of the time filter.

        ids: Filter specific fixtures.

        filter_charterers: A charterer ID, or list of charterer IDs to filter on.

        filter_destinations: A geography ID, or list of geography IDs to filter on.

        filter_origins: A geography ID, or list of geography IDs to filter on.

        filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

        filter_products: A product ID, or list of product IDs to filter on.

        filter_vessels: A vessel ID, or list of vessel IDs to filter on.

        filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

        filter_vessel_age_min: A number between 1 and 100 (representing years).

        filter_vessel_age_max: A number between 1 and 100 (representing years).

        filter_vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

        filter_vessel_flags: A vessel flag, or list of vessel flags to filter on.

        exclude_origins: A geography ID, or list of geography IDs to exclude.

        exclude_destinations: A geography ID, or list of geography IDs to exclude.

        exclude_products: A product ID, or list of product IDs to exclude.

        exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

        exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

        exclude_charterers: A charterer ID, or list of charterer IDs to exclude.

        exclude_vessel_flags: A geography ID, or list of geography IDs to exclude.

        order: Used to sort the returned results.

        order_direction: Determines the direction of sorting.

        # Returns
        List of Fixtures objects.

        # Examples

        Find Fixtures from January 2020.
        ```python
        >>> from datetime import datetime
        >>> from vortexasdk import Fixtures
        >>> df = Fixtures().search(
        ...     filter_time_field="fixing_timestamp",
        ...     filter_time_min=datetime(2020, 1, 1),
        ...     filter_time_max=datetime(2020, 1, 2),
        ... ).to_df()

        ```

        returns

        | vessel.name              | tones            | origin.label | product.label |
        | ------------------------ | ---------------- | ------------ | ------------- |
        | ALPINE EAGLE             | 454.96048964485  | UK           | Crude         |

        Some values can be NULL: value, stocks, cover, runs. It can happen when:

        - The fixture scope is needed to access this endpoint.

        """

        exclude_params: Dict[str, Any] = {
            "filter_origins": convert_to_list(exclude_origins),
            "filter_destinations": convert_to_list(exclude_destinations),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_charterers": convert_to_list(exclude_charterers),
            "filter_vessel_flags": convert_to_list(exclude_vessel_flags),
        }

        api_params: Dict[str, Any] = {
            filter_time_field: filter_time_field,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "ids": convert_to_list(ids),
            "filter_products": convert_to_list(filter_products),
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_effective_controllers": convert_to_list(
                filter_effective_controllers
            ),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "filter_vessel_flags": convert_to_list(filter_vessel_flags),
            "order": order,
            "order_direction": order_direction,
            "exclude": exclude_params,
            "size": size if size is not None else self._MAX_PAGE_RESULT_SIZE,
        }

        response = super().search_with_client(**api_params)

        return FixtureResult(
            records=response["data"], reference=response["reference"]
        )
