from datetime import datetime
from unittest import TestCase

from vortexasdk.api.shared_types import to_ISODate_Array


class TestToISODate(TestCase):
    def test_to_ISODate(self):
        assert to_ISODate_Array([]) == []

    def test_to_ISODate_with_time(self):
        assert to_ISODate_Array(
            [datetime(2018, 12, 31), datetime(2019, 12, 31)]
        ) == ["2018-12-31T00:00:00.000Z", "2019-12-31T00:00:00.000Z"]
