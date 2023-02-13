"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fvoyages_search_enriched.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import Tag, to_ISODate
from vortexasdk.endpoints.endpoints import VOYAGES_SEARCH_ENRICHED
from vortexasdk.endpoints.voyages_search_enriched_result import (
    VoyagesSearchEnrichedFlattenedResult,
    VoyagesSearchEnrichedListResult,
)

from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class VoyagesSearchEnriched(Search):

    _MAX_PAGE_RESULT_SIZE = 500
    _CSV_HEADERS = {"Content-Type": "application/json", "accept": "text/csv"}

    def __init__(self):
        Search.__init__(self, VOYAGES_SEARCH_ENRICHED)

    # noinspection PyUnresolvedReferences
    def search(
        self,
        order: str = None,
        order_direction: str = None,
        offset: int = None,
        unit: str = None,
        columns: Union[str, List[str]] = None,
        time_min: datetime = datetime(2022, 1, 1, 0),
        time_max: datetime = datetime(2022, 1, 1, 1),
        voyage_id: Union[ID, List[ID]] = None,
        cargo_movement_id: Union[ID, List[ID]] = None,
        voyage_status: Union[str, List[str]] = None,
        voyage_status_excluded: Union[str, List[str]] = None,
        movement_status: Union[str, List[str]] = None,
        movement_status_excluded: Union[str, List[str]] = None,
        cargo_status: Union[str, List[str]] = None,
        cargo_status_excluded: Union[str, List[str]] = None,
        location_status: Union[str, List[str]] = None,
        location_status_excluded: Union[str, List[str]] = None,
        commitment_status: Union[str, List[str]] = None,
        commitment_status_excluded: Union[str, List[str]] = None,
        exclude_overlapping_entries: bool = None,
        products: Union[ID, List[ID]] = None,
        products_excluded: Union[ID, List[ID]] = None,
        latest_products: Union[ID, List[ID]] = None,
        latest_products_excluded: Union[ID, List[ID]] = None,
        charterers: Union[ID, List[ID]] = None,
        charterers_excluded: Union[ID, List[ID]] = None,
        effective_controllers: Union[ID, List[ID]] = None,
        effective_controllers_excluded: Union[ID, List[ID]] = None,
        origins: Union[ID, List[ID]] = None,
        origins_excluded: Union[ID, List[ID]] = None,
        destinations: Union[ID, List[ID]] = None,
        destinations_excluded: Union[ID, List[ID]] = None,
        locations: Union[ID, List[ID]] = None,
        locations_excluded: Union[ID, List[ID]] = None,
        vessels: Union[ID, List[ID]] = None,
        vessels_excluded: Union[ID, List[ID]] = None,
        flags: Union[ID, List[ID]] = None,
        flags_excluded: Union[ID, List[ID]] = None,
        ice_class: Union[ID, List[ID]] = None,
        ice_class_excluded: Union[ID, List[ID]] = None,
        vessel_propulsion: Union[ID, List[ID]] = None,
        vessel_propulsion_excluded: Union[ID, List[ID]] = None,
        vessel_age_min: int = None,
        vessel_age_max: int = None,
        vessel_dwt_min: int = None,
        vessel_dwt_max: int = None,
        vessel_cbm_min: int = None,
        vessel_cbm_max: int = None,
        vessel_wait_time_min: int = None,
        vessel_wait_time_max: int = None,
        vessel_scrubbers: str = None,
        vessels_tags: Union[Tag, List[Tag]] = None,
        vessels_tags_excluded: Union[Tag, List[Tag]] = None,
        vessel_risk_level: Union[str, List[str]] = None,
        vessel_risk_level_excluded: Union[str, List[str]] = None,
        has_ship_to_ship: str = None,
        has_charterer: str = None,
    ) -> Union[
        VoyagesSearchEnrichedFlattenedResult, VoyagesSearchEnrichedListResult
    ]:
        """

        Returns one record per voyage, containing a selection of information about the voyage.

        NOTE: To display results as a list (`to_list()`), please set the columns parameter to `None`. To display results as dataframe (`to_df()`), please set the columns parameter to `all` or a list of selected columns.

        # Arguments
            time_min: The UTC start date of the time filter.

            time_max: The UTC end date of the time filter.

            voyage_id: An array of unique voyage ID(s) to filter on.

            cargo_movement_id: An array of unique cargo movement ID(s) to filter on.

            voyage_status: A voyage status, or list of voyage statuses to filter on. Can be one of: `'ballast'`, `'laden'`.

            voyage_status_excluded: A voyage status, or list of voyage statuses to exclude.

            movement_status: A movement status, or list of movement statuses to filter on. Can be one of: `'moving'`, `'stationary'`, `'waiting'`, `'congestion'`, `'slow'`.

            movement_status_excluded: A movement status, or list of movement statuses to exclude.

            cargo_status: A cargo status, or list of cargo statuses to filter on. Can be one of: `'in-transit'`, `'floating-storage'`, `'loading'`, `'discharging'`.

            cargo_status_excluded: A cargo status, or list of cargo statuses to exclude.

            location_status: A location status, or list of location statuses to filter on. Can be one of: `'berth'`, `'anchorage-zone'`, `'dry-dock'`, `'on-the-sea'`.

            location_status_excluded: A location status, or list of location statuses to exclude.

            commitment_status: A commitment status, or list of commitment statuses to filter on. Can be one of: `'committed'`, `'uncommitted'`, `'open'`, `'unknown'`.

            commitment_status_excluded: A commitment status, or list of commitment statuses to exclude.

            exclude_overlapping_entries: A boolean to only consider the latest voyage in days where two or more Voyages overlap.

            products: A product ID, or list of product IDs to filter on.

            products_excluded: A product ID, or list of product IDs to exclude.

            latest_products: A product ID, or list of product IDs of the latest cargo on board to filter on.

            latest_products_excluded: A product ID, or list of product IDs of the latest cargo on board to exclude.

            charterers: A charterer ID, or list of charterer IDs to filter on.

            charterers_excluded: A charterer ID, or list of charterer IDs to exclude.

            effective_controllers: A vessel effective controller ID, or list of vessel effective controller IDs to filter on.

            effective_controllers_excluded: A effective controller ID, or list of effective controller IDs to exclude.

            origins: An origin ID, or list of origin IDs to filter on.

            origins_excluded: An origin ID, or list of origin IDs to exclude.

            destinations: A destination ID, or list of destination IDs to filter on.

            destinations_excluded: A destination ID, or list of destination IDs to exclude.

            locations: A location ID, or list of location IDs to filter on.

            locations_excluded: A location ID, or list of location IDs to exclude.

            vessels: A vessel ID or vessel class, or list of vessel IDs/vessel classes to filter on.

            vessels_excluded: A vessel ID or vessel class, or list of vessel IDs/vessel classes to exclude.

            flags: A flag, or list of flags to filter on.

            flags_excluded: A flag, or list of flags to exclude.

            ice_class: An ice class, or list of ice classes to filter on.

            ice_class_excluded: An ice class, or list of ice classes to ęxclude.

            vessel_propulsion: A propulsion method, or list of propulsion methods to filter on.

            vessel_propulsion_excluded: A propulsion method, or list of propulsion methods to ęxclude.

            vessel_age_min: A number between 1 and 100 (representing years).

            vessel_age_max: A number between 1 and 100 (representing years).

            vessel_dwt_min: A number representing minimum deadweight tonnage of a vessel.

            vessel_dwt_max: A number representing maximum deadweight tonnage of a vessel.

            vessel_cdm_min: A number representing minimum cubic capacity of a vessel.

            vessel_cbm_max: A number representing maximum cubic capacity of a vessel.

            vessel_wait_time_min: A number representing a minimum number of days until a vessel becomes available.

            vessel_wait_time_max: A number representing a maximum number of days until a vessel becomes available.

            vessel_scrubbers: Either inactive 'disabled', or included 'inc' or excluded 'exc'.

            vessels_tags: A time bound vessel tag, or list of time bound vessel tags to filter on.

            vessels_tags_excluded: A time bound vessel tag, or list of time bound vessel tags to exclude.

            vessel_risk_level: A vessel risk level, or list of vessel risk levels to filter on.

            vessel_risk_level_excluded: A vessel risk level, or list of vessel risk levels to exclude.

            has_ship_to_ship: Filter data where at least one STS transfer occurs, or none. - one of `disabled`, `inc`, `exc`. Passing disabled means the filter is not active.

            has_charterer: Filter data where at least one charterer is specified, or none. - one of `disabled`, `inc`, `exc`. Passing disabled means the filter is not active.

            order: Used to sort the returned results. Can be one of:`'vessel_name'`,`'dwt'`,`'vessel_class'`,
            `'start_date'`,`'end_date'`.

            order_direction: Determines the direction of sorting. ‘asc’ for ascending, ‘desc’ for descending.

            offset: Used to page results. The offset from which records should be returned.

            unit: Unit of measurement. Enter `'b'` for barrels or `'t'` for tonnes or `'cbm'` for cubic metres.

            columns: Determines what columns are visible in the output. Enter "all" for all columns, or any of:
            `'vessel_name'`,`'imo'`,`'dwt'`,`'capacity'`,`'vessel_class'`,`'voyage_status'`,`'cargo_status'`,
            `'origin'`,`'origin_shipping_region'`,`'origin_region'`,`'origin_country'`,`'origin_port'`,`'origin_terminal'`,
            `'destination'`,`'destination_shipping_region'`,`'destination_region'`,`'destination_country'`,`'destination_port'`,`'destination_terminal'`,`'destination_eta'`,
            `'charterer'`,`'effective_controller'`,`'voyage_type'`,`'quantity'`,`'latest_product'`,`'latest_product_group'`,`'latest_product_category'`,`'latest_product_grade'`,
            `'time_charterer'`,`'flag'`,`'scrubber'`,`'build_year'`,`'risk_rating'`,`'coating'`,`'start_date'`,`'end_date'`,`'tonne_miles'`,`'distance'`,
            `'voyage_id'`,`'previous_voyage_id'`,`'next_voyage_id'`,`'duration'`,
            `'first_origin'`,`'first_origin_shipping_region'`,`'first_origin_country'`,`'first_origin_port'`,`'first_origin_terminal'`,
            `'final_destination'`,`'final_destination_shipping_region'`,`'final_destination_country'`,`'final_destination_port'`,`'final_destination_terminal'`.

        # Returns
        `VoyagesSearchEnrichedListResult` or `VoyagesSearchEnrichedFlattenedResult`

        # Example
        _Voyages as of 13th Feb 2023 for vessels carrying crude departing from Rotterdam._

        ```python
        >>> from vortexasdk import VoyagesSearchEnriched, Geographies
        >>> from datetime import datetime
        >>> rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        >>> start = datetime(2023, 2, 13)
        >>> end = datetime(2023, 2, 13, 23, 59)
        >>> search_result = VoyagesSearchEnriched().search(
        ... time_min=start,
        ... time_max=end,
        ... origins=rotterdam,
        ... columns="all",
        ... ).to_df().head()

        ```
        Gives the following result:

        ```
        |    | VESSEL NAME          |     IMO |   DWT (t) |   CAPACITY (cbm) | VESSEL CLASS    | VOYAGE STATUS   | ORIGIN                          | ORIGIN TERMINAL         | ORIGIN PORT                     | ORIGIN COUNTRY      | ORIGIN SHIPPING REGION   | DESTINATION    | DESTINATION TERMINAL   | DESTINATION PORT   | DESTINATION COUNTRY   | DESTINATION SHIPPING REGION   | START DATE   | END DATE    | LATEST PRODUCT                  | LATEST PRODUCT GROUP     | LATEST PRODUCT CATEGORY       | LATEST PRODUCT GRADE   |   QUANTITY (bbl) | CHARTERER   | EFFECTIVE CONTROLLER   | TIME CHARTERER   |   BUILD YEAR | FLAG   | RISK RATING   | SCRUBBERS   | COATING   | TONNE-MILES   |   DURATION (h) | DISTANCE   | VOYAGE ID                                                        | PREVIOUS VOYAGE ID                                               | NEXT VOYAGE ID   | ORIGIN GEOGRAPHIC REGION   | DESTINATION GEOGRAPHIC REGION   | FIRST ORIGIN      | FIRST ORIGIN TERMINAL   | FIRST ORIGIN PORT   | FIRST ORIGIN COUNTRY   | FIRST ORIGIN SHIPPING REGION   | FINAL DESTINATION   | FINAL DESTINATION TERMINAL   | FINAL DESTINATION PORT   | FINAL DESTINATION COUNTRY   | FINAL DESTINATION SHIPPING REGION   |
        |---:|:---------------------|--------:|----------:|-----------------:|:----------------|:----------------|:--------------------------------|:------------------------|:--------------------------------|:--------------------|:-------------------------|:---------------|:-----------------------|:-------------------|:----------------------|:------------------------------|:-------------|:------------|:--------------------------------|:-------------------------|:------------------------------|:-----------------------|-----------------:|:------------|:-----------------------|:-----------------|-------------:|:-------|:--------------|:------------|:----------|:--------------|---------------:|:-----------|:-----------------------------------------------------------------|:-----------------------------------------------------------------|:-----------------|:---------------------------|:--------------------------------|:------------------|:------------------------|:--------------------|:-----------------------|:-------------------------------|:--------------------|:-----------------------------|:-------------------------|:----------------------------|:------------------------------------|
        |  0 | YM NEPTUNE           | 9464106 |      6970 |             8091 | Tiny tanker     | Laden           | Frontignan [FR], Rotterdam [NL] | , Vopak Terminal Botlek | Frontignan [FR], Rotterdam [NL] | France, Netherlands | West Med, UK Cont        |                |                        |                    |                       |                               | 28 Dec 2022  |             | Biodiesel, Other Clean Products | Clean Petroleum Products | Finished Biodiesel, Chemicals |                        |            19058 |             |                        |                  |         2009 | MT     | Low           |             | Coated    | 15708783      |           1139 | 7570       | 0edb92ac9addd29b42ede8a8b4843ceb0edb92ac9addd29b42ede8a8b4843ceb | f2b314f245a391ee4e1ebcc41d9a2d2741526f0f3625183440e7e280092cfe91 |                  | Europe, Europe             |                                 | Frontignan [FR]   |                         | Frontignan [FR]     | France                 | West Med                       |                     |                              |                          |                             |                                     |
        |  1 | YASA POLARIS         | 9907457 |    157300 |           167231 | Suezmax         | Ballast         | Rotterdam [NL]                  | TEAM Terminal B.V.      | Rotterdam [NL]                  | Netherlands         | UK Cont                  | Rotterdam [NL] |                        | Rotterdam [NL]     | Netherlands           | UK Cont                       | 13 Feb 2023  |             | Crude                           | Crude/Condensates        | Light-Sour                    | CPC Blend              |                0 |             | Ya-Sa Shipping         |                  |         2021 | MH     | Medium        |             |           |               |             14 |            | ac6c49388567f546d4f57a3e8e8c984e2188f68407394bbe3fde99a0aaff72d7 | f9cab95f35202ab0b273d6d646202080f9cab95f35202ab0b273d6d646202080 |                  | Europe                     | Europe                          | Rotterdam [NL]    | TEAM Terminal B.V.      | Rotterdam [NL]      | Netherlands            | UK Cont                        | Rotterdam [NL]      |                              | Rotterdam [NL]           | Netherlands                 | UK Cont                             |
        |  2 | XING HAI WAN         | 9570113 |      6123 |             6022 | Tiny tanker     | Laden           | Rotterdam [NL]                  | Shell - Rotterdam       | Rotterdam [NL]                  | Netherlands         | UK Cont                  |                |                        |                    |                       |                               | 07 Feb 2023  |             | Asphalt/Bitumen                 | Dirty Petroleum Products |                               |                        |            18513 |             |                        |                  |         2009 | PA     | Low           |             |           | 3848284       |            144 | 1257       | 2bb322f03f203bf2570654e6dc22c52e2bb322f03f203bf2570654e6dc22c52e | 2cec64d13c15f4e8999068c63a898335a75bc99b600f97768655ae748b75a2d7 |                  | Europe                     |                                 | Rotterdam [NL]    | Shell - Rotterdam       | Rotterdam [NL]      | Netherlands            | UK Cont                        |                     |                              |                          |                             |                                     |
        |  3 | XANTHIA              | 9246152 |     17031 |            17829 | General purpose | Laden           | Rotterdam [NL]                  | Vopak Terminal Botlek   | Rotterdam [NL]                  | Netherlands         | UK Cont                  | Amsterdam [NL] |                        | Amsterdam [NL]     | Netherlands           | UK Cont                       | 12 Feb 2023  | 15 Feb 2023 | Diesel/Gasoil                   | Clean Petroleum Products | Gasoil                        |                        |            43370 |             | Neda Maritime          |                  |         2003 | NO     | Low           |             | Coated    | 8334          |             85 | 1          | 640a7b6ae43683ef52bdc5141b5b11a7640a7b6ae43683ef52bdc5141b5b11a7 | 3a7353f9128d669f31e9d775ef53d9355d34928f1a77801da59576d523cb95c5 |                  | Europe                     | Europe                          | Rotterdam [NL]    | Vopak Terminal Botlek   | Rotterdam [NL]      | Netherlands            | UK Cont                        | Amsterdam [NL]      |                              | Amsterdam [NL]           | Netherlands                 | UK Cont                             |
        |  4 | WOODSIDE REES WITHER | 9810367 |     96000 |           173400 | Conventional    | Ballast         | Gate LNG Terminal               | Gate LNG Terminal       | Rotterdam [NL]                  | Netherlands         | UK Cont                  |                |                        |                    |                       |                               | 01 Feb 2023  |             | LNG                             | Liquefied Natural Gas    | Lean                          | Corpus Christi LNG     |                0 |             | MARAN GAS MARITIME     |                  |         2019 | GR     | Low           |             |           |               |            280 | 3967       | 0fa825ab44e6dc5d352db9e8ef47f41e003a794b97b69677ba5f64b2398456e3 | d51d7fc4c74ed04ec69646d297c2f19cd51d7fc4c74ed04ec69646d297c2f19c |                  | Europe                     |                                 | Gate LNG Terminal | Gate LNG Terminal       | Rotterdam [NL]      | Netherlands            | UK Cont                        |                     |                              |                          |                             |                                     |
        ```
        """
        api_params: Dict[str, Any] = {
            "voyage_id": convert_to_list(voyage_id),
            "cargo_movement_id": convert_to_list(cargo_movement_id),
            "voyage_status": convert_to_list(voyage_status),
            "cargo_status": convert_to_list(cargo_status),
            "location_status": convert_to_list(location_status),
            "commitment_status": convert_to_list(commitment_status),
            "movement_status": convert_to_list(movement_status),
            "products": convert_to_list(products),
            "latest_products": convert_to_list(latest_products),
            "charterers": convert_to_list(charterers),
            "effective_controllers": convert_to_list(effective_controllers),
            "origins": convert_to_list(origins),
            "destinations": convert_to_list(destinations),
            "locations": convert_to_list(locations),
            "flags": convert_to_list(flags),
            "ice_class": convert_to_list(ice_class),
            "vessel_propulsion": convert_to_list(vessel_propulsion),
            "vessels": convert_to_list(vessels),
            "vessels_tags": convert_to_list(vessels_tags),
            "vessel_risk_level": convert_to_list(vessel_risk_level),
            "vessel_age_min": vessel_age_min,
            "vessel_age_max": vessel_age_max,
            "vessel_dwt_min": vessel_dwt_min,
            "vessel_dwt_max": vessel_dwt_max,
            "vessel_cbm_min": vessel_cbm_min,
            "vessel_cbm_max": vessel_cbm_max,
            "vessel_wait_time_min": vessel_wait_time_min,
            "vessel_wait_time_max": vessel_wait_time_max,
            "vessel_scrubbers": vessel_scrubbers,
            "has_charterer": has_charterer,
            "has_ship_to_ship": has_ship_to_ship,
            "exclude_overlapping_entries": exclude_overlapping_entries,
            "time_max": to_ISODate(time_max) if time_max else None,
            "time_min": to_ISODate(time_min) if time_min else None,
            "order_direction": order_direction,
            "order": order,
            "offset": offset,
            "size": self._MAX_PAGE_RESULT_SIZE,
            "unit": unit,
            "csv_columns": columns,
            "voyage_status_excluded": convert_to_list(voyage_status_excluded),
            "cargo_status_excluded": convert_to_list(cargo_status_excluded),
            "location_status_excluded": convert_to_list(
                location_status_excluded
            ),
            "commitment_status_excluded": convert_to_list(
                commitment_status_excluded
            ),
            "movement_status_excluded": convert_to_list(
                movement_status_excluded
            ),
            "products_excluded": convert_to_list(products_excluded),
            "latest_products_excluded": convert_to_list(
                latest_products_excluded
            ),
            "charterers_excluded": convert_to_list(charterers_excluded),
            "effective_controllers_excluded": convert_to_list(
                effective_controllers_excluded
            ),
            "origins_excluded": convert_to_list(origins_excluded),
            "destinations_excluded": convert_to_list(destinations_excluded),
            "locations_excluded": convert_to_list(locations_excluded),
            "flags_excluded": convert_to_list(flags_excluded),
            "ice_class_excluded": convert_to_list(ice_class_excluded),
            "vessel_propulsion_excluded": convert_to_list(
                vessel_propulsion_excluded
            ),
            "vessels_excluded": convert_to_list(vessels_excluded),
            "vessels_tags_excluded": convert_to_list(vessels_tags_excluded),
            "vessel_risk_level_excluded": convert_to_list(
                vessel_risk_level_excluded
            ),
        }

        if columns is None:
            response = super().search_with_client(**api_params)
            return VoyagesSearchEnrichedListResult(
                records=response["data"], reference=response["reference"]
            )
        else:
            response = super().search_with_client(
                headers=self._CSV_HEADERS, **api_params
            )
            return VoyagesSearchEnrichedFlattenedResult(
                records=response["data"], reference=response["reference"]
            )
