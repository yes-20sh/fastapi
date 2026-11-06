import sys
from fastapi import APIRouter


def _get_router(module_name: str) -> APIRouter:
    mod = sys.modules[module_name]
    if not hasattr(mod, "router"):
        mod.router = APIRouter(tags=[module_name.split(".")[-2].capitalize()])
    return mod.router


def _route(method: str):
    def wrapper(arg=None):
        def decorator(func):
            router = _get_router(func.__module__)
            return getattr(router, method.lower())(f"/{func.__name__}")(func)

        return decorator(arg) if callable(arg) else decorator

    return wrapper


GET = _route("GET")
POST = _route("POST")
PUT = _route("PUT")
DELETE = _route("DELETE")
PATCH = _route("PATCH")

