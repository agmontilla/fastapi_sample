from fastapi import APIRouter

ping_router = APIRouter()


@ping_router.get("/")
def ping() -> str:
    """Just a ping endpoint."""
    return "pong!"
