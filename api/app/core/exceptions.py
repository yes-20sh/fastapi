from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def unexpected_error_handler(request: Request, exc: Exception):
        # Log the exception in production; don't expose internal details.
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )
