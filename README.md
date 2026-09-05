# VoicePulse AI 🎙️⚡

> Enterprise-grade real-time sales QA and compliance monitoring engine designed to safeguard customer interactions as they happen.

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-teal.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

VoicePulse AI is an advanced AI-powered speech and text analytics application built for sales and support environments. It listens to live microphone audio streams via secure WebSockets, transcribes speech using AssemblyAI's cutting-edge V3 Universal streaming model, and evaluates compliance risks in real time to instantly alert managers or agents of regulatory violations.

---

## 🏗️ System Architecture & Workflow

1. **Client Audio Capture:** The browser captures microphone input using the Web Audio API, downsampling raw PCM data to `16kHz` and converting it to `Int16` buffers.
2. **Secure Token Exchange:** The FastAPI backend securely communicates with AssemblyAI's V3 token endpoint (`/api/token`) to generate short-lived session tokens without exposing master API keys to the browser client.
3. **Real-Time WebSocket Stream:** Audio is streamed over secure WebSockets (`wss://`) to AssemblyAI's real-time transcription engine.
4. **Semantic Compliance Evaluation:** As transcripts update turn-by-turn, the backend evaluates text against compliance rules, calculating multi-factor risk scores and generating live "AI Supervisor Whispers."

---

## ✨ Key Features

* **Real-Time Speech-to-Text:** Ultra-low latency streaming transcription powered by AssemblyAI Universal V3.
* **Semantic Risk Scoring Engine:** Evaluates conversational text for high-pressure sales tactics, misleading claims, and regulatory financial guarantee violations.
* **Instant AI Supervisor Whispers:** Dynamically renders visual feedback, warning badges, and corrective coaching hints directly on the dashboard interface.
* **Secure Token Handshaking:** Hides API credentials behind a protected backend route with rigorous string sanitization to eliminate header authentication errors.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Pydantic, Uvicorn, Requests
* **Speech & AI:** AssemblyAI V3 Streaming WebSockets
* **Frontend:** HTML5, Modern CSS3, JavaScript (Web Audio API)
* **Environment Management:** `python-dotenv`

---

## 🚀 Installation & Quickstart

### 1. Clone the Repository
```bash
git clone [https://github.com/pervaiz123/VoicePulse_AI.git](https://github.com/pervaiz123/VoicePulse_AI.git)
cd VoicePulse_AI
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn requests python-dotenv pydantic
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory of your project:
```env
ASSEMBLYAI_API_KEY=your_actual_assemblyai_api_key_here
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```

Open your web browser and navigate to: **`http://127.0.0.1:8000/`**

---

## 📂 Project Directory Structure

```text
VoicePulse_AI/
│
├── main.py              # FastAPI application, token endpoint, and risk evaluation engine
├── index.html           # Frontend dashboard UI and Web Audio WebSocket handler
├── requirements.txt     # Python project dependencies
├── .env                 # Local environment configurations (git-ignored)
└── README.md            # Project documentation
```

---

## 🛡️ License

Distributed under the MIT License. See `LICENSE` for more information.
