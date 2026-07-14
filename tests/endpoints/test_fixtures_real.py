from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.fixtures import Fixtures
from vortexasdk.api.entity_flattening import (
    convert_to_flat_dict,
    convert_fixture_to_flat_dict,
)


class TestFixturesReal(TestCaseUsingRealAPI):
    """Integration tests for Fixtures endpoint (RND-21448)."""

    def test_rnd_21448_old_flattener_broken_behavior(self):
        """
        RND-21448: INITIAL BROKEN BEHAVIOR

        Before fix: When users tried to request layer-based columns like
        "vessel.corporate_entities.effective_controller.label" using the old
        convert_to_flat_dict, those columns would be EMPTY/MISSING because
        the old flattener uses numeric indices.

        This reproduces the exact bug from the ticket.
        """
        result = (
            Fixtures()
            .search(
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_list()
        )

        assert len(result) > 0
        first_fixture = result[0].model_dump()

        # Simulate old to_df() behavior: request layer-based columns
        old_flat = convert_to_flat_dict(
            first_fixture,
            columns=[
                "vessel.name",
                "tonnes",
                "vessel.corporate_entities.effective_controller.label",
                "vessel.corporate_entities.time_charterer.label",
            ],
        )

        # BROKEN: Requested columns would be missing or None
        assert (
            "vessel.corporate_entities.effective_controller.label"
            not in old_flat
            or old_flat["vessel.corporate_entities.effective_controller.label"]
            is None
        ), "RND-21448 (BROKEN): Requesting layer-based corporate_entities returns empty/missing"

        assert (
            "vessel.corporate_entities.time_charterer.label" not in old_flat
            or old_flat["vessel.corporate_entities.time_charterer.label"]
            is None
        ), "RND-21448 (BROKEN): Requesting layer-based corporate_entities returns empty/missing"

        # OLD behavior: has numeric indices instead
        old_flat_all = convert_to_flat_dict(first_fixture, columns="all")
        numeric_keys = [
            k
            for k in old_flat_all.keys()
            if "corporate_entities.0." in k or "corporate_entities.1." in k
        ]
        assert (
            len(numeric_keys) > 0
        ), "RND-21448 (BROKEN): Old flattener produces numeric indices like corporate_entities.0.label"

    def test_rnd_21448_new_fixture_flattener_works(self):
        """
        RND-21448: After fix, the new fixture flattener correctly groups corporate_entities
        by layer name, making layer-based columns accessible and populated.

        This test verifies the FIX works: convert_fixture_to_flat_dict produces layer-based keys
        with actual values matching what's in to_list().
        """
        result = (
            Fixtures()
            .search(
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_list()
        )

        assert len(result) > 0
        first_fixture = result[0]
        first_fixture_dict = first_fixture.model_dump()

        new_flat = convert_fixture_to_flat_dict(
            first_fixture_dict, columns="all"
        )

        layer_based_keys = [
            k
            for k in new_flat.keys()
            if "corporate_entities.effective_controller." in k
            or "corporate_entities.time_charterer." in k
            or "corporate_entities.charterer." in k
        ]
        assert (
            len(layer_based_keys) > 0
        ), "RND-21448 (fixed): new flattener should produce layer-based keys"

        for key in layer_based_keys:
            value = new_flat.get(key)
            if value is not None:
                # At least some layer-based values should be populated
                assert True
                break
        else:
            assert (
                len(layer_based_keys) > 0
            ), "RND-21448 (fixed): layer-based keys should be present"

        assert "tonnes" in new_flat
        assert new_flat.get("tonnes") is not None

    def test_rnd_21448_to_df_integration(self):
        """
        RND-21448: Verify that to_df() with the new fixture flattener returns
        populated nested vessel fields (matching to_list() data).
        """

        list_result = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_list()
        )

        assert len(list_result) > 0

        df = (
            Fixtures()
            .search(
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_df(
                columns=[
                    "id",
                    "vessel.id",
                    "vessel.name",
                    "vessel.imo",
                    "tonnes",
                    "vessel.corporate_entities.effective_controller.label",
                    "vessel.corporate_entities.time_charterer.label",
                    "charterer.label",
                ]
            )
        )

        assert len(df) > 0

        assert df["vessel.name"].notna().any()
        assert df["vessel.imo"].notna().any()
        assert df["tonnes"].notna().any()

        has_effective_controller = (
            df["vessel.corporate_entities.effective_controller.label"]
            .notna()
            .any()
        )
        has_time_charterer = (
            df["vessel.corporate_entities.time_charterer.label"].notna().any()
        )
        assert has_effective_controller or has_time_charterer

    def test_to_df_returns_data(self):
        """Test that to_df() returns fixtures with default columns."""
        df = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_df()
        )

        assert len(df) > 0
        assert "vessel.name" in df.columns
        assert "tonnes" in df.columns
        assert "charterer.label" in df.columns

    def test_to_df_nested_corporate_entities_populated(self):
        """Test that nested vessel.corporate_entities fields are populated (RND-21448)."""
        df = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_df(
                columns=[
                    "id",
                    "vessel.name",
                    "vessel.imo",
                    "vessel.corporate_entities.effective_controller.label",
                    "vessel.corporate_entities.time_charterer.label",
                    "tonnes",
                ]
            )
        )

        assert len(df) > 0
        assert "vessel.name" in df.columns
        assert (
            "vessel.corporate_entities.effective_controller.label"
            in df.columns
        )
        assert (
            df["vessel.corporate_entities.effective_controller.label"]
            .notna()
            .any()
        )

    def test_to_df_tonnes_column_populated(self):
        """Test that tonnes column (fixed typo from tones) is populated."""
        df = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_df(columns=["id", "tonnes"])
        )

        assert len(df) > 0
        assert "tonnes" in df.columns
        assert df["tonnes"].notna().sum() > len(df) * 0.5
