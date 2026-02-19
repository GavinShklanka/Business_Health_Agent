from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router as api_router
from app.api.ui import router as ui_router
from app.api.newsletter import router as newsletter_router

app = FastAPI(title="Business Health Agent")

# --- Mount Static Files ---
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# --- Include Routers ---
app.include_router(api_router)        # /api/agents/run (dev mode)
app.include_router(ui_router)         # UI routes (/ and /run-ui)
app.include_router(newsletter_router) # Newsletter routes
