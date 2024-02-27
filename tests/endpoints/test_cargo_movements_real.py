from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from tests.timer import Timer
from vortexasdk import Geographies, Corporations, Products
from vortexasdk.endpoints.cargo_movements import CargoMovements


class TestCargoMovementsReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        CargoMovements().search(filter_activity="loading_state")

    def test_full_search_with_pagination(self):
        CargoMovements().search(
            filter_activity="loading_state",
            filter_time_min=datetime(2023, 4, 30),
            filter_time_max=datetime(2023, 5, 1),
        )

    def test_search_returns_unique_results(self):
        result = CargoMovements().search(
            filter_activity="loading_state",
            filter_origins=[
                "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
            ],
            filter_time_min=datetime(2017, 8, 29),
            filter_time_max=datetime(2017, 10, 29),
        )

        n_results = len(result)

        n_unique_results = len(set([str(k) for k in result]))

        assert n_results == n_unique_results

    def test_search_single_filter_id(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_products="6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_exlusion_filter(self):
        arab_medium = [
            p.id
            for p in Products().search("Arab Medium").to_list()
            if p.layer == ["grade"]
        ]
        meg = [
            g.id
            for g in Geographies().search("MEG/AG").to_list()
            if "trading_region" in g.layer
        ]
        iraq = [
            g.id
            for g in Geographies().search("Iraq").to_list()
            if "country" in g.layer
        ]

        cols = [
            "cargo_movement_id",
            "vessels.0.name",
            "events.cargo_port_load_event.0.location.port.id",
            "events.cargo_port_load_event.0.location.port.label",
            "events.cargo_port_load_event.0.location.country.id",
            "events.cargo_port_load_event.0.location.country.label",
            "events.cargo_port_load_event.0.start_timestamp",
            "events.cargo_port_load_event.0.end_timestamp",
            "product.grade.id",
            "product.grade.label",
            "product.group_product.label",
            "parent_ids.0.id",
            "parent_ids.0.splinter_timestamp",
        ]

        df = (
            CargoMovements()
            .search(
                filter_activity="loading_end",
                filter_products=[
                    "54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11"
                ],
                filter_origins=meg,
                exclude_origins=iraq[0],
                exclude_products=arab_medium,
                filter_time_min=datetime(2019, 10, 1),
                filter_time_max=datetime(2019, 11, 1),
                cm_unit="b",
            )
            .to_df(columns=cols)
        )

        df_excl = df.loc[
            (
                df["events.cargo_port_load_event.0.location.country.id"]
                == iraq[0]
            )
            | (df["product.grade.id"] == arab_medium[0])
        ]

        assert df_excl.empty

    def test_to_df_all_columns(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_products="6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )
            .to_df(columns="all")
            .head(2)
        )

        assert len(df) == 2

    def test_timestamp_columns(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_products="6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )
            .to_df(columns="all")
            .head(2)
        )

        self.assertEqual(
            str(df["events.cargo_port_load_event.0.end_timestamp"].dtypes),
            "datetime64[ns, UTC]",
        )
        self.assertEqual(
            str(df["events.cargo_port_unload_event.0.end_timestamp"].dtypes),
            "datetime64[ns, UTC]",
        )

    def test_search_single_filter_origin_name(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_origins=[
                    g.id
                    for g in Geographies().search(term="rotterdam").to_list()
                    if "port" in g.layer
                ],
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_search_filters_on_timeseries_max_activity(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="storing_state",
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_filter_vessel_classes(self):
        start = datetime(2021, 1, 1)
        end = datetime(2021, 1, 11)

        vlcc_plus = "oil_vlcc"

        vlcc_plus_movements = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
                filter_vessel_classes=[vlcc_plus],
            )
            .to_df()
        )

        all_vessel_classes_movements = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        assert (
            all_vessel_classes_movements.shape[0]
            > vlcc_plus_movements.shape[0]
        )

    def test_search_single_filter_owner_name(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="loading_state",
                filter_effective_controllers=[
                    c.id for c in Corporations().search(term="DHT").to_list()
                ],
                filter_time_min=datetime(2018, 10, 12, 0),
                filter_time_max=datetime(2018, 10, 13, 1),
            )
            .to_df()
            .head(2)
        )
        assert len(df) >= 1

    def test_search_single_filter_waypoint_name(self):
        df = (
            CargoMovements()
            .search(
                filter_activity="any_activity",
                filter_waypoints=[
                    g.id for g in Geographies().search(term="suez").to_list()
                ],
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_search_list_filter_id(self):
        df = (
            CargoMovements()
            .search(
                filter_products=[
                    "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"
                ],
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
                filter_activity="loading_state",
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_search_to_list(self):
        CargoMovements().search(
            filter_products=[
                "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"
            ],
            filter_time_min=datetime(2019, 8, 29),
            filter_time_max=datetime(2019, 8, 29, 0, 10),
            filter_activity="loading_state",
        ).to_list()

    def test_speed(self):
        with Timer("Search") as t_search:
            cms = CargoMovements().search(
                filter_activity="loading_state",
                filter_time_min=datetime(2019, 8, 29),
                filter_time_max=datetime(2019, 8, 29, 0, 10),
            )

        with Timer("to_list") as t_to_list:
            cms.to_list()

        with Timer("df") as t_to_df:
            df = cms.to_df()

        # Check we load a reasonable number of cargo movements in a short enough period of time
        assert len(df) > 500
        assert t_search.interval < 10
        assert t_to_list.interval < 10
        assert t_to_df.interval < 5

    def test_get_single_cargo_movement_by_long_id(self):
        cms = CargoMovements().search(
            filter_activity="loading_state",
            filter_time_min=datetime(2019, 8, 29),
            filter_time_max=datetime(2019, 8, 29, 0, 10),
        )
        longId = cms[0]["cargo_movement_id"]
        cm = CargoMovements().record(longId)
        assert cm["cargo_movement_id"] == longId

    def test_get_single_cargo_movement_by_short_id(self):
        cms = CargoMovements().search(
            filter_activity="loading_state",
            filter_time_min=datetime(2019, 8, 29),
            filter_time_max=datetime(2019, 8, 29, 0, 10),
        )
        shortId = cms[0]["cargo_movement_id"][:16]
        cm = CargoMovements().record(shortId)
        assert cm["cargo_movement_id"] == cms[0]["cargo_movement_id"]

    def test_get_single_cargo_movement_with_unit_param(self):
        cms = CargoMovements().search(
            filter_activity="loading_state",
            filter_time_min=datetime(2019, 8, 29),
            filter_time_max=datetime(2019, 8, 29, 0, 10),
        )
        shortId = cms[0]["cargo_movement_id"][:16]
        unitT = {"unit": "t"}
        unitB = {"unit": "b"}
        unitCBM = {"unit": "cbm"}
        cmT = CargoMovements().record(shortId, unitT)
        cmB = CargoMovements().record(shortId, unitB)
        cmCBM = CargoMovements().record(shortId, unitCBM)

        assert cmT["quantity"] != cmB["quantity"]
        assert cmT["quantity"] != cmCBM["quantity"]
