import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from vortexasdk.config import LOG_FILE, LOG_LEVEL

FORMATTER = logging.Formatter(
    "%(asctime)s %(name)s — %(levelname)s — %(message)s"
)


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    if LOG_FILE is not None:
        file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
        file_handler.setFormatter(FORMATTER)
        logger.addHandler(file_handler)

    logger.propagate = False
    return logger
