from requests import Session
from requests.adapters import HTTPAdapter
from urllib3 import Retry


# Inspired by https://www.peterbe.com/plog/best-practice-with-retries-with-requests
def _requests_retry_session(
    retries=3, backoff_factor=0.5, status_forcelist=(502, 504), session=None,
) -> Session:
    """Instantiate a session with Retry backoff."""
    session = session or Session()

    retry = Retry(
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


def retry_get(*args, **kwargs):
    with _requests_retry_session() as s:
        return s.get(*args, **kwargs)


def retry_post(*args, **kwargs):
    with _requests_retry_session() as s:
        return s.post(*args, **kwargs)
