from fastapi import APIRouter
from app.core.schemas import AgentRunRequest
from app.services.agent_service import AgentService

router = APIRouter()
service = AgentService()

@router.post("/run")
async def run_agent(payload: AgentRunRequest):
    state = {
        "user_input": payload.user_input,
        "parameters": payload.parameters
    }
    return await service.run(state)
