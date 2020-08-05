from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselMovements, Geographies, Corporations, Attributes
from vortexasdk.endpoints import vessel_movements_result


class TestVesselMovementsReal(TestCaseUsingRealAPI):
    def test_search(self):
        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        v = VesselMovements().search(
            filter_time_min=datetime(2017, 10, 1, 0, 0),
            filter_time_max=datetime(2017, 10, 1, 0, 10),
            filter_origins=rotterdam,
        )

        assert len(v) > 10

    def test_search_vessel_status(self):
        v = VesselMovements().search(
            filter_time_min=datetime(2019, 10, 1),
            filter_time_max=datetime(2019, 10, 15),
            filter_vessel_classes=["vlcc"],
            filter_vessel_status="vessel_status_ballast",
        )

        assert len(v) > 50

    def test_exclusion_filter(self):
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
        bahri = [c.id for c in Corporations().search("BAHRI").to_list()]

        cols = [
            "vessel_movement_id",
            "vessel.name",
            "start_timestamp",
            "end_timestamp",
            "origin.location.country.id",
            "origin.location.country.label",
            "destination.location.country.id",
            "destination.location.country.label",
            "cargoes.0.product.group.label",
            "vessel.corporate_entities.charterer.id",
            "vessel.corporate_entities.charterer.label",
        ]

        df = (
            VesselMovements()
            .search(
                filter_origins=meg,
                exclude_origins=iraq,
                exclude_charterers=bahri[0],
                filter_time_min=datetime(2019, 10, 15),
                filter_time_max=datetime(2019, 11, 1),
            )
            .to_df(columns=cols)
        )

        mask = (df["origin.location.country.id"] == iraq[0]) | (
            df["vessel.corporate_entities.charterer.id"] == bahri[0]
        )
        df_excl = df.loc[mask]

        assert df_excl.empty

    def test_to_df_all_columns(self):
        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins=rotterdam,
            )
            .to_df(columns="all")
            .head(2)
        )

        assert len(df) == 2

    def test_search_to_dataframe(self):
        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins=rotterdam,
            )
            .to_df()
            .head(2)
        )

        assert list(df.columns) == vessel_movements_result.DEFAULT_COLUMNS
        assert len(df) == 2

    def test_search_to_dataframe_subset_of_columns(self):
        cols = ["vessel.imo", "vessel.name"]

        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins=rotterdam,
            )
            .to_df(columns=cols)
            .head(2)
        )

        assert list(df.columns) == cols
        assert len(df) == 2

    def test_filter_activity(self):
        df = (
            VesselMovements()
            .search(
                filter_activity="storing_state",
                filter_time_min=datetime(2017, 10, 1),
                filter_time_max=datetime(2017, 10, 1),
            )
            .to_df()
            .head(2)
        )

        print(df.head())
        assert len(df) == 2

    def test_age_flag_scrubbers_filters(self):
        panama = [
            g.id
            for g in Geographies().search("panama").to_list()
            if "country" in g.layer
        ]

        df = (
            VesselMovements()
            .search(
                filter_vessel_scrubbers="inc",
                filter_vessel_age_min=2,
                filter_vessel_age_max=15,
                filter_vessel_flags=panama,
                filter_time_min=datetime(2017, 10, 1),
                filter_time_max=datetime(2017, 10, 1),
            )
            .to_df()
            .head(2)
        )

        print(df.head())
        assert len(df) == 2

    def test_ice_class_filters(self):
        ice_classes = [
            g.id for g in Attributes().search(type="ice_class").to_list()
        ]

        propulsion = [
            g.id for g in Attributes().search(type="propulsion").to_list()
        ]

        df = (
            VesselMovements()
            .search(
                filter_vessel_ice_class=ice_classes,
                filter_vessel_propulsion=propulsion,
                filter_time_min=datetime(2017, 10, 1),
                filter_time_max=datetime(2017, 10, 1),
            )
            .to_df()
            .head(2)
        )

        print(df.head())
        assert len(df) == 2
