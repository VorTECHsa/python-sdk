import os
from typing import Any

SKIP_TAGS = os.getenv("SKIP_TAGS", "").split()

# The AFP API takes the ID of a routing zone to avoid. The SDK types `avoid_zone` as zone names, so the ID is typed as Any.
SUEZ_CANAL_ID: Any = "f5634597081459985237dc54fcbe518d4b0a4f4af618b7719abda334b95538d1"
