"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fcargo_timeseries.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import CARGO_TIMESERIES_RESOURCE
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class CargoTimeSeries(Search):
    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_TIMESERIES_RESOURCE)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        filter_activity: str,
        timeseries_activity: str = None,
        timeseries_frequency: str = "day",
        timeseries_unit: str = "b",
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        filter_charterers: Union[ID, List[ID]] = None,
        filter_destinations: Union[ID, List[ID]] = None,
        filter_origins: Union[ID, List[ID]] = None,
        filter_owners: Union[ID, List[ID]] = None,
        filter_effective_controllers: Union[ID, List[ID]] = None,
        filter_products: Union[ID, List[ID]] = None,
        filter_vessels: Union[ID, List[ID]] = None,
        filter_vessel_classes: Union[ID, List[ID]] = None,
        filter_vessel_age_min: int = None,
        filter_vessel_age_max: int = None,
        filter_storage_locations: Union[ID, List[ID]] = None,
        filter_ship_to_ship_locations: Union[ID, List[ID]] = None,
        filter_waypoints: Union[ID, List[ID]] = None,
        disable_geographic_exclusion_rules: bool = None,
        intra_movements: str = None,
        timeseries_activity_time_span_min: int = None,
        timeseries_activity_time_span_max: int = None,
    ) -> TimeSeriesResult:
        """

        Find Aggregate flows between regions, for various products, for various vessels, or various corporations.

        Example questions that can be answered with this endpoint:

        * _How many Crude/Condensate barrels have been imported into China each day over the last year?_
        * _How many tonnes of Fuel Oil has company X exported from the United States each week over the last 2 years?_
        * _How have long-term Medium-Sour floating storage levels changed over time?_

        # Arguments
            filter_activity: Cargo movement activity on which to base the time filter. The endpoint only includes cargo
            movements matching that match this filter in the aggregations. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'storing_state', 'storing_start', 'storing_end', 'transiting_state', 'oil_on_water_state'].

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            filter_corporations: A corporation ID, or list of corporation IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_effective_controllers: An effective controller ID, or list of effective controller IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_vessel_classes: A vessel class, or list of vessel classes to filter on.

            filter_vessel_age_min: A number between 1 and 100 (representing years).

            filter_vessel_age_max: A number between 1 and 100 (representing years).

            filter_storage_locations: A geography ID, or list of geography IDs to filter on.

            filter_ship_to_ship_locations: A geography ID, or list of geography IDs to filter on.

            filter_waypoints: A geography ID, or list of geography IDs to filter on.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

            intra_movements: This enum controls a popular industry term intra-movements and determines the filter behaviour for cargo leaving then entering the same geographic area.
             One of `all`, `exclude_intra_country` or `exclude_intra_geography`

            timeseries_activity: The cargo movement activity we want to aggregate on. This param defaults to
            `filter_activity` if left blank. For example, Let's say we want to aggregate the unloading timestamps of
             all cargo movements that loaded in 2019, then we'd use `filter_time_min` and `filter_time_max` to specify
             1st Jan 2019 and 31st Dec 2019 respectively, we'd set `filter_activity='loading_state'` and
             `timeseries_activity='unloading_state'` to filter on loadings but aggregate on unloadings.
              `filter_activity` Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'storing_state', 'storing_start', 'storing_end', 'transiting_state'].

            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of ['day', 'week',
             'doe_week', 'month', 'quarter', 'year']

            timeseries_unit: A numeric metric to be calculated for each time bucket. Must be one of ['b', 'bpd', 't',
             'tpd', 'c', 'cpd'], corresponding to barrels, barrels per day, metric tonnes, metric tonnes per day,
              cargo movement count, cargo movement count per day, respectively.

            timeseries_activity_time_span_min: The minimum amount of time in milliseconds accounted for in a time series
             activity. Can be used to request long-term floating storage. For example, to only return floating storage
             movements that occurred for _more_ than 14 days enter
             `timeseries_activity_time_span_min=1000 * 60 * 60 * 24 * 14` in conjunction with
             `filter_activity='storing_state'`.

            timeseries_activity_time_span_max: The maximum amount of time in milliseconds accounted for in a time series
             activity. Can be used to request short-term floating storage. For example, to only return floating storage
             movements that occurred for _less_ than 14 days enter
             `timeseries_activity_time_span_max=1000 * 60 * 60 * 24 * 14` in conjunction with
             `filter_activity='storing_state'`.

        # Returns
        `TimeSeriesResult`

        # Example

        * _What was the monthly average barrels per day of crude loaded from Rotterdam over the last year?_

        ```python
        >>> from vortexasdk import CargoTimeSeries, Geographies, Products
        >>> rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        >>> crude = [p.id for p in Products().search("crude").to_list() if "Crude" == p.name]
        >>> search_result = CargoTimeSeries().search(
        ...    timeseries_unit='bpd',
        ...    timeseries_frequency='month',
        ...    filter_origins=rotterdam,
        ...    filter_products=crude,
        ...    filter_activity='loading_state',
        ...    filter_time_min=datetime(2018, 1, 1),
        ...    filter_time_max=datetime(2018, 12, 31))
        >>> df = search_result.to_df()

        ```

        Gives the following:

        |    | key                      |     count |     value |
        |---:|:-------------------------|----------:|----------:|
        |  0 | 2018-01-01T00:00:00.000Z | 0.354839  | 458665    |
        |  1 | 2018-02-01T00:00:00.000Z | 0.75      | 45024     |
        |  2 | 2018-03-01T00:00:00.000Z | 0.0645161 |  35663.5  |
        |  3 | 2018-04-01T00:00:00.000Z | 0.878777  |  12345.2  |
        |  4 | 2018-05-01T00:00:00.000Z | 0.455932  |   9999.32 |
        |  5 | 2018-06-01T00:00:00.000Z | 0.777667  |  12234.8  |
        |  6 | 2018-07-01T00:00:00.000Z | 0.555097  | 987666    |
        |  7 | 2018-08-01T00:00:00.000Z | 0.290323  | 5318008.1 |
        |  8 | 2018-09-01T00:00:00.000Z | 0.0333333 | 686888.87 |
        |  9 | 2018-10-01T00:00:00.000Z | 0.354839  | 234344    |
        | 10 | 2018-11-01T00:00:00.000Z | 0.2345    | 111111    |
        | 11 | 2018-12-01T00:00:00.000Z | 0.123129  |  34344.5  |


        """

        if disable_geographic_exclusion_rules is not None:
            logger.warning(
                f"\nYou are using the disable_geographic_exclusion_rules parameter. It will be deprecated in March 2024 in favour of the `intra_movements` filter.\nPlease refer to https://docs.vortexa.com/reference/intro-cargo-filters for more information.\n"
            )

        api_params: Dict[str, Any] = {
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "timeseries_activity_time_span_min": timeseries_activity_time_span_min,
            "timeseries_activity_time_span_max": timeseries_activity_time_span_max,
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_effective_controllers": convert_to_list(
                filter_effective_controllers
            ),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_vessel_classes": convert_to_list(filter_vessel_classes),
            "filter_vessel_age_min": filter_vessel_age_min,
            "filter_vessel_age_max": filter_vessel_age_max,
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_storage_locations": convert_to_list(
                filter_storage_locations
            ),
            "filter_ship_to_ship_locations": convert_to_list(
                filter_ship_to_ship_locations
            ),
            "filter_waypoints": convert_to_list(filter_waypoints),
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules,
            "intra_movements": intra_movements,
            "timeseries_frequency": timeseries_frequency,
            "timeseries_unit": timeseries_unit,
            "timeseries_activity": timeseries_activity or filter_activity,
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        response = super().search_with_client(**api_params)

        return TimeSeriesResult(
            records=response["data"], reference=response["reference"]
        )
