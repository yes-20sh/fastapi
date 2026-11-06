import os
import sys
from contextlib import asynccontextmanager
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

API_DIR = Path(__file__).resolve().parent.parent
load_dotenv(API_DIR / ".env")
sys.pycache_prefix = str(API_DIR / ".pycache")

from app.core.config.database import Base, check_db_connection, engine
from app.core.middleware.exceptions import register_exception_handlers
from app.core.middleware.middleware import register_middleware
from app.modules.health.controller import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    check_db_connection()
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="FastAPI Modular Backend", version="1.0.0", lifespan=lifespan)
register_middleware(app)
register_exception_handlers(app)

app.include_router(health_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
@app.get("/health", tags=["Health"], include_in_schema=False)
def ping():
    return {"status": "ok"}


def start():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    start()
