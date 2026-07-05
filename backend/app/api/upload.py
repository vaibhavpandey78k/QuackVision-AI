from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
from app.pipeline.video_pipeline import process_video

router = APIRouter(prefix="/api", tags=["Upload"])

UPLOAD_FOLDER = Path("app/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    # Save uploaded video
    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create a folder for this video's frames
    video_name = Path(file.filename).stem
    frames_folder = UPLOAD_FOLDER / "frames" / video_name

    # Extract frames
    result = process_video(str(destination))

    # Return response
    return {
    "message": "Upload successful",
    "filename": file.filename,
    "pipeline": result
}