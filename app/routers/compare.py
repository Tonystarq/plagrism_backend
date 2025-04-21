from fastapi import APIRouter, UploadFile, File
from app.utils.text_utils import read_text_file, calculate_similarity

router = APIRouter(
    prefix="/compare",
    tags=["compare"]
)

@router.post("/")
async def compare_documents(
    file1: UploadFile = File(...),
    file2: UploadFile = File(...)
):
    """Compare two text documents and return their similarity score."""
    try:
        # Read the content of both files
        text1 = await read_text_file(file1)
        text2 = await read_text_file(file2)
        
        # Calculate similarity
        similarity_score = calculate_similarity(text1, text2)
        
        return {
            "status": "success",
            "similarity_score": similarity_score,
            "message": "Documents compared successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        } 