import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "vortexasdk.log")

END_OF_AVAILABLE_DATA = datetime.utcnow() + relativedelta(months=6)
BEGINNING_OF_AVAILABLE_DATA = END_OF_AVAILABLE_DATA - relativedelta(years=4)
