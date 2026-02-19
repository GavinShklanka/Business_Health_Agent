from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse

from app.database.newsletter import init_db, add_subscriber

router = APIRouter()

init_db()


@router.post("/newsletter/subscribe")
async def subscribe(email: str = Form(...)):
    success = add_subscriber(email)

    return RedirectResponse(
        url="/?subscribed=true" if success else "/?subscribed=exists",
        status_code=303
    )
