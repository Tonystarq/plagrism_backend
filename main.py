from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

app = FastAPI(title="Document Similarity API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_text_file(file: UploadFile) -> str:
    """Read text content from uploaded file."""
    content = file.file.read()
    return content.decode('utf-8')

def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate similarity between two text documents using TF-IDF and cosine similarity."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return float(similarity)

@app.post("/compare")
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

@app.get("/")
async def root():
    """Root endpoint to check if API is running."""
    return {"message": "Document Similarity API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 