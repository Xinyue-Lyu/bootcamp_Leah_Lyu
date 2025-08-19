# config.py
# src/config.py

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Paths
PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"


def load_env(dotenv_path: Optional[str] = None) -> None:
    """
    Load environment variables from a .env file.
    If no path is provided, it will search in the current and parent directories.
    """
    if dotenv_path:
        load_dotenv(dotenv_path=dotenv_path)
    else:
        load_dotenv()  # default behavior
    print(".env loaded (if present)")


def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get an environment variable by name.
    Returns the value if found, otherwise returns the provided default.
    """
    return os.getenv(name, default)


# Debug logging (optional)
if __name__ == "__main__":
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:", DATA_DIR)
    load_env()
    print("Example: MY_SECRET =", get_key("MY_SECRET", "<not set>"))

