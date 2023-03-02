from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import Products, Geographies, Corporations, Vessels

endpoints_and_searchterms = [
    (Products(), "Gasoil"),
    (Geographies(), "China"),
    (Corporations(), "Oil"),
    (Vessels(), "Ocean"),
]


class TestSearchReal(TestCaseUsingRealAPI):
    def test_search_exact_match_yields_fewer_results_than_non_exact_match(
        self,
    ):
        for endpoint, term in endpoints_and_searchterms:
            result_loose_match = endpoint.search(
                term=term, exact_term_match=False
            )
            result_exact_match = endpoint.search(
                term=term, exact_term_match=True
            )

            assert len(result_exact_match) < len(result_loose_match)

    def test_search_exact_match_yields_exact_matches_only(self):
        for endpoint, term in endpoints_and_searchterms:
            result_exact_match = endpoint.search(
                term=term, exact_term_match=True
            )

            actual_names = {e["name"] for e in result_exact_match}

            # result must be the exact term, or must contain no results if there's no reference objects with that names
            assert actual_names == {term} or actual_names == set()
