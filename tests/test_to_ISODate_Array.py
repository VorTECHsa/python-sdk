from datetime import datetime
from unittest import TestCase

from vortexasdk.api.shared_types import to_ISODate_array


class TestToISODate(TestCase):
    def test_to_ISODate(self):
        assert to_ISODate_array(None) == None

    def test_to_ISODate_with_time(self):
        assert (
            to_ISODate_array([datetime(2018, 12, 31, 23, 59, 59, 123456), datetime(2019, 12, 31, 23, 59, 59, 123456)])
            == ["2018-12-31T23:59:59.123Z", "2019-12-31T23:59:59.123Z"]
        )
