from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["health"]
)

@router.get("/")
async def root():
    """Root endpoint to check if API is running."""
    return {"message": "Document Similarity API is running"} 