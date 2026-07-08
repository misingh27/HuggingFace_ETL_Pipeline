"""
config.py

Central configuration file for the Hugging Face ETL Pipeline.
Stores project paths, API settings, and reusable constants.
"""

from pathlib import Path

# ==========================================================
# Project Root
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Directories
# ==========================================================

DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "database"
LOG_DIR = BASE_DIR / "logs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# ==========================================================
# File Paths
# ==========================================================

RAW_JSON_PATH = DATA_DIR / "raw_models.json"

CSV_PATH = DATA_DIR / "cleaned_models.csv"

DATABASE_PATH = DATABASE_DIR / "huggingface.db"

LOG_FILE = LOG_DIR / "pipeline.log"

# ==========================================================
# API Configuration
# ==========================================================

API_URL = "https://huggingface.co/api/models"

REQUEST_TIMEOUT = 30

# ==========================================================
# Database
# ==========================================================

TABLE_NAME = "huggingface_models"

# ==========================================================
# Business Rules
# ==========================================================

POPULAR_DOWNLOAD_THRESHOLD = 100000
