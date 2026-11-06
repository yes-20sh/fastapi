from sqlalchemy.orm import Session

class BaseService:
    """Optional base class for services that need a shared DB session."""
    def __init__(self, db: Session):
        self.db = db
