from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

competitor_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@competitor_router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "¡Hola, Nestor!"})
