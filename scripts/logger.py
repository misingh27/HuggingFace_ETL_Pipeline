"""
logger.py

Creates a centralized logger for the ETL pipeline.
"""

import logging

from config import LOG_FILE

# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger("HF_ETL")

logger.setLevel(logging.INFO)

# Prevent duplicate logs
if not logger.handlers:

    file_handler = logging.FileHandler(LOG_FILE)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
"""
logger.py

Central logging configuration.
"""

import logging

from config import LOG_FILE

# Create parent folder if it doesn't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="a",
)

logger = logging.getLogger("HF_ETL")
