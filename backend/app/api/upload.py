from fastapi import APIRouter, UploadFile, File
from fastapi.concurrency import run_in_threadpool
from pathlib import Path
import shutil
import traceback

from app.pipeline.video_pipeline import process_video

router = APIRouter()

UPLOAD_FOLDER = Path("app/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):

    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        result = await run_in_threadpool(
            process_video,
            str(destination)
        )

        return {
            "message": "Upload successful",
            "filename": file.filename,
            "pipeline": result,
        }

    except Exception:

        print("\n========== PIPELINE ERROR ==========")
        traceback.print_exc()
        print("====================================\n")

        return {
            "message": "Pipeline Failed",
            "error": "Pipeline execution failed"
        }