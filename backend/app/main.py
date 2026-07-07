from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.progress import router as progress_router

app = FastAPI(
    title="QuackVision AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routes
app.include_router(upload_router, prefix="/api", tags=["Upload"])
app.include_router(progress_router, prefix="/api", tags=["Progress"])


@app.get("/")
def root():
    return {
        "project": "QuackVision AI",
        "status": "Backend Running",
        "version": "1.0.0",
    }