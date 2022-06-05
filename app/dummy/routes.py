from fastapi import APIRouter

dummy_router = APIRouter()


@dummy_router.get("/")
def dummy_endpoint() -> str:
    """Just a dummy endpoint."""

    return "hello dummy!"
