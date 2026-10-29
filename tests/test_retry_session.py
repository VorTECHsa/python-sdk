from unittest import TestCase

from vortexasdk.retry_session import _requests_retry_session


class TestRetrySession(TestCase):
    def test_does_not_retry_401(self):
        session = _requests_retry_session()
        retry = session.get_adapter("https://example.com").max_retries

        assert 401 not in retry.status_forcelist

    def test_retries_server_errors(self):
        session = _requests_retry_session()
        retry = session.get_adapter("https://example.com").max_retries

        assert set(retry.status_forcelist) == {500, 502, 504}
