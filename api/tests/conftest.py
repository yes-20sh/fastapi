import sys
from pathlib import Path

if sys.pycache_prefix is None:
    sys.pycache_prefix = str(Path(__file__).resolve().parent.parent / ".pycache")

import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
