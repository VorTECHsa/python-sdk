import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
LOG_FILE = os.getenv("LOG_FILE", None)

HTTP_PROXY = os.getenv("HTTP_PROXY", None)
HTTPS_PROXY = os.getenv("HTTPS_PROXY", None)
