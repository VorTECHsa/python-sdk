import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "ERROR").upper()
LOG_FILE = os.getenv("LOG_FILE", None)
