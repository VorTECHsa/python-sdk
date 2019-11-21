from unittest import TestCase

from tests.mixins import CallRealAPI
from vortexasdk import Geographies


class TestGeographiesReal(CallRealAPI, TestCase):

    def test_search(self):
        geographies = Geographies().search(term=["Liverpool", "Southampton"])
        names = [g['name'] for g in geographies]

        assert 'Liverpool [GB]' in names
