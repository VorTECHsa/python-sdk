from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexasdk import Geographies
from vortexasdk.client import default_client, set_client


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestGeographiesReal(TestCase):

    def setUp(self) -> None:
        set_client(default_client())

    def test_search(self):
        geographies = Geographies().search(term=["Liverpool", "Southampton"])
        names = [g['name'] for g in geographies]

        assert 'Liverpool [GB]' in names
