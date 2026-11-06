from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.health import Health
from app.modules.health.schema import HealthCreate


class HealthService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Health]:
        stmt = select(Health).order_by(Health.date_time.desc())
        return list(self.db.scalars(stmt).all())

    def create(self, data: HealthCreate) -> Health:
        record_date_time = (
            data.date_time if data.date_time is not None else datetime.now(timezone.utc)
        )
        record = Health(name=data.name, date_time=record_date_time)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

