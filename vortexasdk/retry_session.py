from requests import Response, Session
from requests.adapters import HTTPAdapter
from urllib3 import Retry


# Inspired by https://www.peterbe.com/plog/best-practice-with-retries-with-requests
def _requests_retry_session(
        retries=6,
        backoff_factor=1,
        status_forcelist=(500, 502, 504),
        session=None,
) -> Session:
    """Instantiate a session with Retry backoff."""
    session = session or Session()

    retry = Retry(
        raise_on_redirect=False,
        raise_on_status=False,
        method_whitelist=["POST", "GET"],
        status=retries,
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


_headers = {"Content-Type": "application/json"}


def retry_get(*args, **kwargs) -> Response:
    with _requests_retry_session() as s:
        return s.get(headers=_headers, *args, **kwargs)


def retry_post(*args, **kwargs) -> Response:
    with _requests_retry_session() as s:
        return s.post(headers=_headers, *args, **kwargs)
