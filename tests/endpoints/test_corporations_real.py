from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from tests.utils import to_markdown
from vortexasdk import Corporations
from vortexasdk.client import create_client, set_client


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestCorporationsReal(TestCase):
    def setUp(self) -> None:
        set_client(create_client())

    def test_search(self):
        df = Corporations().search().to_df()

        print(to_markdown(df.head(2)))
