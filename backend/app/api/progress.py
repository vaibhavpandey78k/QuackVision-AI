from fastapi import APIRouter
from app.pipeline.progress_tracker import get_progress

router = APIRouter()

@router.get("/progress")
def progress():
    return get_progress()