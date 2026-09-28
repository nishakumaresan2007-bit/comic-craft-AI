from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
router = APIRouter()

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.post("/api/generate")
async def generate(request: Request):
    try:
        data = await request.json()
        from app.services.gemini_pro import generate_story
        story = generate_story(data.get("prompt",""), data.get("genre","adventure"))
        return {"story": story}
    except Exception as e:
        print(f"ERROR: {e}")
        return {"story": f"Error da: {e} - Check terminal"}