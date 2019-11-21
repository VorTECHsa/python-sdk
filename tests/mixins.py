from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from tests.mock_client import MockVortexaClient
from vortexasdk.client import create_client, set_client


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class CallRealAPI(TestCase):
    def setUp(self) -> None:
        set_client(create_client())


class CallMockAPI(TestCase):
    def setUp(self) -> None:
        set_client(MockVortexaClient())
