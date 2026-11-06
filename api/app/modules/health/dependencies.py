from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.database.session import get_db
from app.modules.health.service import HealthService


def get_health_service(db: Session = Depends(get_db)) -> HealthService:
    return HealthService(db)

