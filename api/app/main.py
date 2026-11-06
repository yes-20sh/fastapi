import os
import sys
from pathlib import Path

_pycache_dir = str(Path(__file__).resolve().parent.parent / ".pycache")
if sys.pycache_prefix is None:
    sys.pycache_prefix = _pycache_dir
os.environ["PYTHONPYCACHEPREFIX"] = _pycache_dir

from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI
from app.config.database.connection import engine
from app.config.database.base import Base
from app.models.health import Health  # noqa: F401
from app.modules.health.controller import router as health_router
from app.config.config import settings
from app.core.middleware import register_middleware
from app.core.exceptions import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # For local development only. Use Alembic migrations in production.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.APP_NAME, version="1.0.0", lifespan=lifespan)
register_middleware(app)
register_exception_handlers(app)

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
app.include_router(api_router)


@app.get("/health", tags=["Health"])
def ping():
    return {"status": "ok"}
