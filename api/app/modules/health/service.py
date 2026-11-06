from fastapi import HTTPException
from sqlalchemy import select
from app.core.config.database import SessionLocal
from app.models.health import Health
from app.modules.health.schema import HealthCreate


class HealthService:
    def get_all(self):
        with SessionLocal() as db:
            try:
                stmt = select(Health).order_by(Health.date_time.desc())
                return list(db.scalars(stmt).all())
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to fetch health records: {str(e)}",
                )

    def create(self, data: HealthCreate):
        with SessionLocal() as db:
            try:
                record = Health(**data.model_dump(exclude_none=True))
                db.add(record)
                db.commit()
                db.refresh(record)
                return record
            except Exception as e:
                db.rollback()
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to create health record: {str(e)}",
                )


health_service = HealthService()
