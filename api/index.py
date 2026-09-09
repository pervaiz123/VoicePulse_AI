from main import app
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from urllib.parse import urlencode
import os
import requests

app = FastAPI(title="VoicePulse AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_frontend():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "VoicePulse AI Backend Active"}

@app.get("/api/token")
@app.get("/token")
def get_token():
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ASSEMBLYAI_API_KEY is not configured.")

    url = "https://streaming.assemblyai.com/v3/token"
    query_params = urlencode({"expires_in_seconds": 3600})
    
    response = requests.get(
        f"{url}?{query_params}",
        headers={"Authorization": api_key}
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, 
            detail=f"AssemblyAI V3 Error: {response.text}"
        )

    return response.json()