from pathlib import Path

# Project Root Directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAMPLE_DATA_DIR = DATA_DIR / "sample"

# Dataset Files
AUTH_LOG_FILE = RAW_DATA_DIR / "auth.txt.gz"
REDTEAM_FILE = RAW_DATA_DIR / "redteam.txt.gz"