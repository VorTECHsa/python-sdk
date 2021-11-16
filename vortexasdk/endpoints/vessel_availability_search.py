"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Favailability_search.ipynb)
"""
from typing import Dict, List, Union
from vortexasdk.endpoints.vessel_availability_result import VesselAvailabilityResult

from vortexasdk.api import ID
from vortexasdk.endpoints.endpoints import VESSEL_AVAILABILITY_SEARCH_RESOURCE
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class VesselAvailabilitySearch(Search):
    """
    Vessel Availability Endpoint, use this to search through Vortexa's vessel availability data.
    Please note: you will require a subscription to our Freight module to access this endpoint.
    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, VESSEL_AVAILABILITY_SEARCH_RESOURCE)

    def search(
        self,
        filter_region: str = None,
        filter_port: str = None,
        use_reference_port: bool = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[str, List[str]] = None,
        filter_vessel_status: str = None,
        filter_vessel_location: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_destination: Union[ID, List[ID]] = None,
        filter_days_to_arrival: List[Dict[str, int]] = None,
        filter_vessel_dwt_min: int = None,
        filter_vessel_dwt_max: int = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_vessel_idle_min: int = None,
        filter_vessel_idle_max: int = None,
        filter_vessel_scrubbers: str = "disabled",
        filter_recent_visits: str = None,
        exclude_products: Union[ID, List[ID]] = None,
        exclude_vessels: Union[ID, List[ID]] = None,
        exclude_vessel_classes: Union[str, List[str]] = None,
        exclude_vessel_status: str = None,
        exclude_vessel_location: Union[ID, List[ID]] = None,
        exclude_owners: Union[ID, List[ID]] = None,
        exclude_destination: Union[ID, List[ID]] = None,
        offset: int = None,
        order: str = None,
        order_direction: str = None,
    ) -> VesselAvailabilityResult:
        """
        List of vessels that can be available to load a given cargo at a given port on a future date.

        # Arguments

            order: Used to sort the returned results. Must be one of the following: [‘vessel_status’,
            ‘days_to_arrival’, ‘days_idle’].

            order_direction: Determines the direction of sorting. ‘asc’ for ascending, ‘desc’ for
            descending.

            offset: Used to page results. The offset from which records should be returned.

            size: Used to page results. The size of the result set. Between 0 and 500.

            filter_owners: An corporation ID, or list of corporation IDs to filter on.

            filter_destination: A geography ID, or list of geography IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessel_status: The vessel status on which to base the filter. Enter 'vessel_status_ballast' for ballast vessels, 'vessel_status_laden_known' for laden vessels with known cargo (i.e. a type of cargo that Vortexa currently tracks) or 'any_activity' for any other vessels

            filter_vessel_location: A location ID, or list of location IDs to filter on.

            filter_port: Filter by port ID.

            filter_region: Filter by region ID - takes precedence over filter_port if provided. This should be used in conjunction with `use_reference_port`

            filter_days_to_arrival: Filter availability by time to arrival in days`

            use_reference_port: If this flag is enabled, we will return data for
            the reference port instead of the user selected one,

            filter_vessel_age_min: A number between 1 and 100 (representing years).

            filter_vessel_age_max: A number between 1 and 100 (representing years).

            filter_vessel_idle_min: A number greater than 0 (representing idle days).

            filter_vessel_idle_max: A number greater than 0 and filter_vessel_idle_min (representing idle days).

            filter_vessel_dwt_min: A number between 0 and 550000.

            filter_vessel_dwt_max: A number between 0 and 550000.

            filter_vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

            filter_recent_visits: Filter availability by each vessel's recent visits

            exclude_products: A product ID, or list of product IDs to exclude.

            exclude_vessels: A vessel ID, or list of vessel IDs to exclude.

            exclude_vessel_classes: A vessel class, or list of vessel classes to exclude.

            exclude_vessel_status: The vessel status on which to base the filter. Enter 'vessel_status_ballast' for ballast vessels, 'vessel_status_laden_known' for laden vessels with known cargo (i.e. a type of cargo that Vortexa currently tracks) or 'any_activity' for any other vessels

            exclude_owners: An owner ID, or list of owner IDs to exclude.

            exclude_vessel_location: A location ID, or list of location IDs to filter on.

            exclude_destination: A location ID, or list of location IDs to filter on.


        # Returns
        `VesselAvailabilityResult`


        # Example
        Top 2 available vessels arriving at Rotterdam port in the next 5 days.

        ```python
        >>> from vortexasdk import VesselAvailabilitySearch, Geographies
        >>> rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        >>> df = VesselAvailabilitySearch().search(
        ...        filter_port=rotterdam,
        ...        filter_days_to_arrival={"min": 0, "max": 35}
        ... ).to_df(columns=['available_at','vessel_name','vessel_class']).head(2)

        ```

        |    | available_at             | vessel_name              | vessel_class |
        |---:|:-------------------------|:-------------------------|-------------:|
        |  0 | 2017-09-30 15:30:27+00:00| STAR RIVER               |  handysize   |
        |  1 | 2017-08-29 14:51:32+00:00| AMALTHEA                 |  aframax     |

        """

        exclude_params = {
            "filter_destination": convert_to_list(exclude_destination),
            "filter_products": convert_to_list(exclude_products),
            "filter_vessels": convert_to_list(exclude_vessels),
            "filter_vessel_classes": convert_to_list(exclude_vessel_classes),
            "filter_owners": convert_to_list(exclude_owners),
            "filter_vessel_status": convert_to_list(exclude_vessel_status),
            "filter_vessel_location": convert_to_list(
                exclude_vessel_location
            ),
        }

        api_params = {
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(
                filter_vessel_classes
            ),
            "filter_vessel_status": filter_vessel_status,
            "filter_vessel_location": convert_to_list(filter_vessel_location),
            "filter_owners": convert_to_list(filter_owners),
            "filter_destination": convert_to_list(filter_destination),
            "filter_region": filter_region,
            "filter_port": filter_port,
            "use_reference_port": use_reference_port,
            "filter_days_to_arrival": convert_to_list(
                filter_days_to_arrival
            ),
            "filter_vessel_dwt_min": filter_vessel_dwt_min,
            "filter_vessel_dwt_max": filter_vessel_dwt_max,
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_vessel_idle_min": filter_vessel_idle_min,
            "filter_vessel_idle_max": filter_vessel_idle_max,
            "filter_vessel_scrubbers": filter_vessel_scrubbers,
            "filter_recent_visits": filter_recent_visits,
            "exclude": exclude_params,
            "offset": offset,
            "order": order,
            "order_direction": order_direction,
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        return VesselAvailabilityResult(super().search(**api_params))
