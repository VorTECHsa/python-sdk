from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexasdk import Geographies
from vortexasdk.client import create_client, set_client
from vortexasdk.conversions import convert_to_charterer_ids, convert_to_geography_ids, convert_to_vessel_ids


class TestConvert(TestCase):

    @skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
    def test_convert_to_geography_ids(self):
        set_client(create_client())

        rotterdam_id = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        rotterdam_name = Geographies().reference(rotterdam_id)[0]['name']

        result = convert_to_geography_ids([rotterdam_name])

        assert [rotterdam_id] == result

    @skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
    def test_convert_to_charterer_ids(self):
        set_client(create_client())

        result = convert_to_charterer_ids(["DHT"])

        assert len(result) >= 1

    @skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
    def test_convert_to_vessel_ids(self):
        set_client(create_client())

        result = convert_to_vessel_ids(["OCEAN"])

        assert len(result) >= 10

    @skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
    def test_convert_to_ids_retains_id_argument(self):
        set_client(create_client())

        id = "f00e3068faf65af1345067f11dc6723b8da324a6f33c000118fccd81947deb4e"
        charterer_result = convert_to_charterer_ids(["DHT"])
        charterer_result_with_id = convert_to_charterer_ids(["DHT", id])

        assert charterer_result_with_id == [id] + charterer_result
