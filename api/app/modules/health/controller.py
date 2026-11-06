from app.modules.health.schema import HealthCreate, HealthResponse
from app.modules.health.service import health_service
from app.shared.decorator.route_decorator import GET, POST


@GET()
def get_all_health() -> list[HealthResponse]:
    return health_service.get_all()


@POST()
def create_health(data: HealthCreate) -> HealthResponse:
    return health_service.create(data)
