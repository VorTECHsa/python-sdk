from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselDiversions, Geographies, Products

from datetime import datetime, timedelta


class TestVesselDiversions(TestCaseUsingRealAPI):
    def test_search_to_list_runs(self):
        port = Geographies().search("Singapore", exact_term_match=True).to_list()[0].id

        diversions = VesselDiversions().search(
            filter_time_min=datetime.now() - timedelta(days=10),
            filter_locations=port,
            include_waypoints=True,
            unit='t'
        ).to_list()

        for d in diversions:
            print(d.next_declared_destination)

    def test_long_date_range_raises_exception(self):
        too_old_date = datetime.now() - timedelta(days=VesselDiversions()._MAX_DIVERSION_HISTORIC_DAYS + 1)

        self.assertRaises(ValueError, lambda: VesselDiversions().search(filter_time_min=too_old_date))

    def test_search_to_df_runs(self):
        port = Geographies().search("Singapore", exact_term_match=True).to_list()[0].id

        df = VesselDiversions().search(
            filter_time_min=datetime.now() - timedelta(days=10),
            filter_locations=port,
            include_waypoints=True,
            unit='t'
        ).to_df()

        print(df)

