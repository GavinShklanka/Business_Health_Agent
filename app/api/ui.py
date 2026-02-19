from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.services.agent_service import AgentService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

service = AgentService()


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/run-ui", response_class=HTMLResponse)
async def run_ui(
    request: Request,
    user_input: str = Form(...),
    recipient_email: str = Form(...)
):
    state = {
        "user_input": user_input,
        "recipient_email": recipient_email,
        "parameters": {}
    }

    result = await service.run(state)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "result": result
        }
    )
