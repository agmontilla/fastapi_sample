from fastapi import FastAPI
from app.ping.routes import ping_router
from app.dummy.routes import dummy_router

app = FastAPI()

app.include_router(ping_router, prefix="/ping", tags=["ping"])
app.include_router(dummy_router, prefix="/dummy", tags=["Dummy"])
