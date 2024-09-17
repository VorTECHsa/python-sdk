from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VoyagesSearchEnriched
from vortexasdk.api.shared_types import VoyageDateRangeActivity

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"


class TestVoyagesSearchEnrichedEnriched(TestCaseUsingRealAPI):
    def test_search_returns_dataframe(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesSearchEnriched()
            .search(
                time_min=start, time_max=end, origins=rotterdam, columns="all"
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_search_pagination_on_df(self):
        start = datetime(2021, 1, 1)
        end = datetime(2021, 2, 28)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start, time_max=end, origins=rotterdam, columns="all"
            )
            .to_df()
        )

        assert len(res) > 1000

    def test_search_pagination_on_lists(self):
        start = datetime(2021, 1, 1)
        end = datetime(2021, 2, 28)

        res = (
            VoyagesSearchEnriched()
            .search(time_min=start, time_max=end, origins=rotterdam)
            .to_list()
        )

        assert len(res) > 1000

    def test_search_returns_some_cols(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)

        df = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                columns=["vessel_name", "imo", "voyage_status", "destination"],
            )
            .to_df()
        )

        assert len(df.columns) == 4
        assert list(df.columns) == [
            "VESSEL NAME",
            "IMO",
            "VOYAGE STATUS",
            "DESTINATION",
        ]

    def test_search_from_description_df(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start, time_max=end, origins=rotterdam, columns="all"
            )
            .to_df()
            .head()
        )

        assert len(res) > 0

    def test_search_from_description_raw(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(time_min=start, time_max=end, origins=rotterdam)
            .to_list()
        )

        assert len(res) > 0
        assert res[0].vessel is not None
        assert len(res[0].events) > 0
        assert res[0].events[0].event_group is not None
        assert res[0].start_timestamp is not None
        assert res[0].corporate_entities is not None
        assert res[0].tags is not None
        assert res[0].voyage_status is not None

    def test_has_charterer_param(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                has_charterer="inc",
            )
            .to_list()
        )

        assert len(res) > 0

    def test_has_ship_to_ship_param(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                has_ship_to_ship="inc",
            )
            .to_list()
        )

        assert len(res) > 0

    def test_departure_mode_with_first_load(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_date_range_activity=VoyageDateRangeActivity.DEPARTURES.value,
                origin_behaviour="first_load",
            )
            .to_list()
        )

        assert len(res) > 0

    def test_reduced_events_fetching_only_cargo_events(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_status=["laden"],
                event_types=["cargo"],
            )
            .to_list()
        )

        invalid_events = [
            event
            for event in res[0].events
            if event is not None
            and (event.event_type == "vessel" or event.event_type == "status")
        ]

        assert len(res) > 0
        assert len(res[0].events) > 0
        assert len(invalid_events) == 0

    def test_reduced_events_fetching_only_vessel_events(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_status=["laden"],
                event_types=["vessel"],
            )
            .to_list()
        )

        invalid_events = [
            event
            for event in res[0].events
            if event is not None
            and (event.event_type == "cargo" or event.event_type == "status")
        ]

        assert len(res) > 0
        assert len(res[0].events) > 0
        assert len(invalid_events) == 0

    def test_reduced_events_fetching_only_status_events(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 26, 23, 59)

        res = (
            VoyagesSearchEnriched()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_status=["laden"],
                event_types=["status"],
            )
            .to_list()
        )

        invalid_events = [
            event
            for event in res[0].events
            if event is not None
            and (event.event_type == "cargo" or event.event_type == "vessel")
        ]

        assert len(res) > 0
        assert len(res[0].events) > 0
        assert len(invalid_events) == 0
