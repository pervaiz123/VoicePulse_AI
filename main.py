import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel, Field
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlencode

load_dotenv(find_dotenv(), override=True)

app = FastAPI(
    title="VoicePulse AI Enterprise Engine",
    description="Real-Time Sales QA, Diarization, and Compliance Intelligence",
    version="4.0.0"
)

class ComprehensiveQAEvaluation(BaseModel):
    call_id: str
    risk_score: float
    detected_category: str
    compliance_violation: bool
    supervisor_whisper: str
    sentiment_tone: str

@app.get("/api/token")
def get_realtime_token():
    api_key = os.getenv("ASSEMBLYAI_API_KEY", "3de74bbb2f0e485ba1db797990091d1e")
    if not api_key:
        raise HTTPException(status_code=500, detail="Missing API Key")
    
    cleaned_key = api_key.strip().replace('"', '').replace("'", "").replace("\n", "").replace("\r", "")
    url = "https://streaming.assemblyai.com/v3/token"
    endpoint = f"{url}?{urlencode({'expires_in_seconds': 300})}"
    
    response = requests.get(endpoint, headers={"Authorization": cleaned_key})
    if response.status_code == 200:
        return response.json()
        
    raise HTTPException(status_code=500, detail=f"Authentication Failed: {response.text}")

@app.post("/api/qa/evaluate")
def evaluate_call_transcript(data: dict):
    text = data.get("text", "").lower()
    
    high_risk_phrases = ["guaranteed return", "no risk", "definitely will profit", "100% safe", "act now or lose"]
    medium_risk_phrases = ["trust me", "secret strategy", "easy money", "hurry"]
    
    violation = any(phrase in text for phrase in high_risk_phrases)
    medium_warning = any(phrase in text for phrase in medium_risk_phrases)
    
    if violation:
        risk = 0.95
        category = "Regulatory Financial Guarantee Violation"
        whisper = "CRITICAL: Absolute financial guarantee detected. Intervene immediately!"
        sentiment = "High Risk / Aggressive"
    elif medium_warning:
        risk = 0.60
        category = "High-Pressure Sales Tactic"
        whisper = "WARNING: Avoid high-pressure urgency phrases. Maintain transparency."
        sentiment = "Cautionary"
    else:
        risk = 0.05
        category = "Compliant"
        whisper = "Good rapport and compliant phrasing. Continue execution."
        sentiment = "Professional / Safe"

    eval_result = ComprehensiveQAEvaluation(
        call_id=data.get("call_id", "VOICEPULSE-SECURE-01"),
        risk_score=risk,
        detected_category=category,
        compliance_violation=violation,
        supervisor_whisper=whisper,
        sentiment_tone=sentiment
    )
    
    return {"status": "success", "evaluation_result": eval_result.model_dump()}

@app.get("/")
def serve_dashboard():
    if not os.path.exists("index.html"):
        return HTMLResponse(content="<h1>Dashboard missing index.html</h1>", status_code=404)
    return FileResponse("index.html")