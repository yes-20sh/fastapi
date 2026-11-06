from fastapi import APIRouter, Depends, status
from app.modules.health.dependencies import get_health_service
from app.modules.health.schema import HealthCreate, HealthResponse
from app.modules.health.service import HealthService

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=list[HealthResponse])
@router.get("/", response_model=list[HealthResponse], include_in_schema=False)
def get_all_health(service: HealthService = Depends(get_health_service)):
    """Get all health records stored in the database."""
    return service.get_all()


@router.post("", response_model=HealthResponse, status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=HealthResponse, status_code=status.HTTP_201_CREATED, include_in_schema=False)
def create_health(
    data: HealthCreate,
    service: HealthService = Depends(get_health_service),
):
    """Create a new health record with name and date/time."""
    return service.create(data)

