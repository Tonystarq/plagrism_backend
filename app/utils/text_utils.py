from fastapi import UploadFile
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import chardet

async def read_text_file(file: UploadFile) -> str:
    """Read text content from uploaded file with encoding detection."""
    try:
        content = await file.read()
        
        # Detect the encoding
        encoding_result = chardet.detect(content)
        encoding = encoding_result['encoding']
        
        # If encoding detection failed, try common encodings
        if not encoding:
            encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
            for enc in encodings:
                try:
                    return content.decode(enc)
                except UnicodeDecodeError:
                    continue
            raise ValueError("Could not decode file with any of the attempted encodings")
        
        # Try to decode with detected encoding
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            # Fallback to latin-1 if detected encoding fails
            return content.decode('latin-1')
            
    except Exception as e:
        raise ValueError(f"Error reading file: {str(e)}")

def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate similarity between two text documents using TF-IDF and cosine similarity."""
    try:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(similarity)
    except Exception as e:
        raise ValueError(f"Error calculating similarity: {str(e)}") 