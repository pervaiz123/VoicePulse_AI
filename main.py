import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
from urllib.parse import urlencode
import re
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="VoicePulse AI", version="2.0.0")

class EvaluationRequest(BaseModel):
    text: str
    call_id: str = "VOICEPULSE-SECURE-01"

@app.get("/", response_class=HTMLResponse)
def serve_dashboard():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>VoicePulse AI Dashboard (index.html missing)</h3>"

@app.get("/api/token")
def generate_assemblyai_token():
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ASSEMBLYAI_API_KEY environment variable is not set.")
    
    clean_key = api_key.strip().strip('"').strip("'")
    url = "https://streaming.assemblyai.com/v3/token"
    
    try:
        response = requests.get(
            f"{url}?{urlencode({'expires_in_seconds': 300})}",
            headers={"Authorization": clean_key}
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=f"AssemblyAI token error: {response.text}")
        
        data = response.json()
        return {"token": data.get("token")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/qa/evaluate")
def evaluate_call_transcript(data: EvaluationRequest):
    text = data.text.lower()
    
    guarantee_patterns = [
        r"\b\d+%\s*(return|profit|gain|guarantee)",
        r"guaranteed\s*(return|profit|gain|win)",
        r"risk[\s-]?free",
        r"100%\s*safe"
    ]
    
    high_pressure_patterns = [
        r"act\s*now",
        r"limited\s*time",
        r"don't\s*miss\s*out",
        r"secret\s*strategy"
    ]
    
    has_guarantee_violation = any(re.search(pat, text) for pat in guarantee_patterns)
    has_pressure_tactic = any(re.search(pat, text) for pat in high_pressure_patterns)
    
    if has_guarantee_violation:
        risk = 0.98
        category = "Regulatory Financial Guarantee Violation"
        whisper = "CRITICAL: Absolute or numeric financial guarantee detected. Immediate correction required!"
        sentiment = "High Risk / Non-Compliant"
    elif has_pressure_tactic:
        risk = 0.65
        category = "High-Pressure Sales Tactic"
        whisper = "WARNING: Urgency or manipulative sales phrase identified. Maintain neutral advisory tone."
        sentiment = "Cautionary"
    else:
        risk = 0.02
        category = "Fully Compliant"
        whisper = "Professional conversational flow. Continue execution."
        sentiment = "Compliant / Professional"

    return {
        "status": "success",
        "evaluation_result": {
            "call_id": data.call_id,
            "risk_score": risk,
            "detected_category": category,
            "compliance_violation": has_guarantee_violation,
            "supervisor_whisper": whisper,
            "sentiment_tone": sentiment
        }
    }