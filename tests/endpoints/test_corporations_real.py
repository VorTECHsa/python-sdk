from unittest import TestCase

from tests.mixins import CallRealAPI
from tests.utils import to_markdown
from vortexasdk import Corporations


class TestCorporationsReal(CallRealAPI, TestCase):

    def test_search(self):
        df = Corporations().search().to_df()

        print(to_markdown(df.head(2)))
