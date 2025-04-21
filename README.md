# Document Similarity API

A FastAPI-based backend service for comparing text documents and calculating their similarity scores. This is the backend service for the Document Similarity Checker application.

## 🌐 Live Links

- Frontend Application: [https://plagrism.vercel.app/](https://plagrism.vercel.app/)
- Backend API: [https://plagrism-backend-1.onrender.com/](https://plagrism-backend-1.onrender.com/)
- API Documentation: [https://plagrism-backend-1.onrender.com/docs](https://plagrism-backend-1.onrender.com/docs)
- Frontend Repository: [https://github.com/Tonystarq/plagrism](https://github.com/Tonystarq/plagrism)
- Backend Repository: [https://github.com/Tonystarq/plagrism_backend](https://github.com/Tonystarq/plagrism_backend)

## 📋 Features

- Compare two text documents and get a similarity score between 0 and 1
- Uses TF-IDF vectorization and cosine similarity for accurate comparison
- RESTful API endpoints
- CORS enabled for frontend integration
- Automatic encoding detection for uploaded files
- Error handling and validation
- Deployed on Render with proper configuration

## 🏗️ Project Structure

```
plagrism_backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   │   ├── __init__.py
│   │   ├── compare.py       # Document comparison endpoint
│   │   └── health.py        # Health check endpoint
│   └── utils/
│       ├── __init__.py
│       └── text_utils.py    # Text processing utilities
├── .gitignore
├── README.md
├── requirements.txt
└── render.yaml              # Render deployment configuration
```

## 📦 Dependencies

Listed in `requirements.txt`:
```
fastapi==0.115.12
uvicorn==0.34.2
python-multipart==0.0.9
numpy==1.26.4
scikit-learn==1.4.1.post1
python-dotenv==1.0.1
chardet==5.2.0
```

## 🚀 Setup and Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Tonystarq/plagrism_backend.git
cd plagrism_backend
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Unix or MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Production Deployment (Render)

The application is configured for deployment on Render using `render.yaml`:

```yaml
services:
  - type: web
    name: document-similarity-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.10.0
```

## 📡 API Endpoints

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

Example response:
```json
{
    "message": "Document Similarity API is running"
}
```

## 🔧 API Documentation

The API documentation is available at:
- Swagger UI: `https://plagrism-backend-1.onrender.com/docs`
- ReDoc: `https://plagrism-backend-1.onrender.com/redoc`

## 🛠️ Technical Details

### Text Processing
- Automatic encoding detection using `chardet`
- Support for multiple text encodings (UTF-8, Latin-1, ISO-8859-1, CP1252)
- Error handling for invalid encodings

### Similarity Calculation
- Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
- Cosine similarity for document comparison
- Handles different document lengths and formats

### Security
- CORS middleware enabled for frontend integration
- Input validation and error handling
- Secure file handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- [@Tonystarq](https://github.com/Tonystarq)

## 🙏 Acknowledgments

- FastAPI for the web framework
- scikit-learn for text processing
- Render for hosting
- Vercel for frontend hosting 