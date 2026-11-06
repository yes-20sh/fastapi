import os
import sys
from pathlib import Path

_pycache_dir = str(Path(__file__).resolve().parent.parent / ".pycache")
if sys.pycache_prefix is None:
    sys.pycache_prefix = _pycache_dir
os.environ["PYTHONPYCACHEPREFIX"] = _pycache_dir

import uvicorn


def start():
    """Run the development server."""
    os.environ["PYTHONPYCACHEPREFIX"] = _pycache_dir
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    start()
