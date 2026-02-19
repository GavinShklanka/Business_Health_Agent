from fastapi import APIRouter
from app.api import agents

router = APIRouter(prefix="/api")

router.include_router(agents.router, prefix="/agents", tags=["Agents"])
