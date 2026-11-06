import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class HealthCreate(BaseModel):
    name: str
    date_time: datetime | None = None


class HealthResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    date_time: datetime
