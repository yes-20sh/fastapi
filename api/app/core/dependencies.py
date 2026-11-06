from collections.abc import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.database.session import get_db

__all__ = ["get_db"]
