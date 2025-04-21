# Document Similarity API

A FastAPI-based backend service for comparing text documents and calculating their similarity scores.

## Features

- Compare two text documents and get a similarity score between 0 and 1
- Uses TF-IDF vectorization and cosine similarity for accurate comparison
- RESTful API endpoints
- CORS enabled for frontend integration

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Compare Documents
- **Endpoint**: `/compare`
- **Method**: POST
- **Description**: Compare two text documents and return their similarity score
- **Request**: Form data with two text files
- **Response**: JSON with similarity score

Example response:
```json
{
    "status": "success",
    "similarity_score": 0.85,
    "message": "Documents compared successfully"
}
```

### Health Check
- **Endpoint**: `/`
- **Method**: GET
- **Description**: Check if the API is running
- **Response**: JSON with status message

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 