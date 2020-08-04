from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselDiversions, Geographies, Products

from datetime import datetime, timedelta


class TestVesselDiversions(TestCaseUsingRealAPI):
    def test_search(self):

        crude_id = "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"
        rotterdam = Geographies().search("Rotterdam [NL]", exact_term_match=True).to_list()[0].id

        diversions = VesselDiversions().search(
            filter_time_min=datetime.now() - timedelta(days=1),
            # filter_locations=rotterdam,
            # filter_products=crude_id,
        ).to_list()

        for d in diversions:
            print(d.next_declared_destination)
