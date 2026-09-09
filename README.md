VoicePulse AI 🎙️⚡Enterprise Real-Time Sales QA & Compliance Monitoring EngineVoicePulse AI is a high-performance, real-time speech analytics and compliance engine designed for sales call monitoring. Powered by AssemblyAI's V3 Streaming WebSocket API and FastAPI, the platform ingests audio streams, generates real-time transcriptions, and dynamically evaluates agent interactions against compliance and regulatory rules (e.g., detecting unauthorized financial guarantees or missing disclosures).🌟 Key FeaturesReal-Time Speech-to-Text: Streamlined WebSocket integration with AssemblyAI V3 for ultra-low latency transcription.Automated Compliance & QA Scoring: Real-time evaluation endpoint (/api/qa/evaluate) analyzing live transcripts for regulatory breaches, risk indicators, and supervisor whisper prompts.Ephemeral Token Security: Secure /api/token architecture ensuring client-side WebSocket connections consume temporary short-lived authentication tokens without exposing backend API credentials.Serverless & Local Ready: Built on FastAPI with full support for local Uvicorn development as well as native serverless execution on Vercel.🏗️ Architecture & Data Flow┌─────────────────┐       1. Fetch Temp Token       ┌────────────────────────┐
│                 │ ──────────────────────────────> │  FastAPI Backend       │
│  Browser Client │                                 │  (main.py / Vercel)    │
│  (index.html)   │ <────────────────────────────── │                        │
│                 │       2. Ephemeral Token        └───────────┬────────────┘
└────────┬────────┘                                             │
         │                                                      │ 3. Exchange Key
         │ 4. Direct Audio Stream & WebSocket                   │    via HTTP GET
         ▼                                                      ▼
┌─────────────────────────────────┐                 ┌────────────────────────┐
│  AssemblyAI V3 Streaming API    │                 │ AssemblyAI Auth Server │
│  (streaming.assemblyai.com/v3)  │                 └────────────────────────┘
└─────────────────────────────────┘
Token Provisioning: The frontend requests a temporary token from /api/token. The backend contacts AssemblyAI's token service using the server-side ASSEMBLYAI_API_KEY and returns a temporary token valid for 3600 seconds.WebSocket Streaming: The client opens a secure direct WebSocket stream to wss://[streaming.assemblyai.com/v3/ws](https://streaming.assemblyai.com/v3/ws) using the temporary token.Compliance Evaluation: As transcript fragments stream in, live text payloads are dispatched to /api/qa/evaluate for real-time risk checks and supervisor whispers.🛠️ Tech StackComponentTechnologyDescriptionBackend FrameworkFastAPIHigh-performance Python async web frameworkSpeech-to-TextAssemblyAI V3Streaming WebSocket Real-Time Transcription APIServer EngineUvicornLightning-fast ASGI web serverTestingPytestUnit testing suiteDeploymentVercelNative FastAPI Serverless Functions Hosting📂 Repository StructurePlaintextVoicePulse_AI/
├── api/
│   └── index.py            # Vercel entrypoint bridge (imports app from main)
├── main.py                 # Core FastAPI application, routes, and QA logic
├── index.html              # Frontend UI dashboard with audio capture & WebSocket stream
├── test_main.py            # Automated test suite for endpoints and token retrieval
├── requirements.txt        # Production dependencies
├── pyproject.toml          # Project metadata & Vercel builder settings
└── README.md               # Repository documentation
🚀 Quickstart — Local SetupPrerequisitesPython 3.10 or higherAssemblyAI API Key (Get one from the AssemblyAI Dashboard)InstallationClone the Repository:DOSgit clone <https://github.com/pervaiz123/VoicePulse_AI.git>
cd VoicePulse_AI
Set Up Virtual Environment:DOSpython -m venv venv

# On Windows

venv\Scripts\activate

# On macOS/Linux

source venv/bin/activate
Install Dependencies:DOSpip install -r requirements.txt
Set Environment Variable:DOS# Windows (CMD)
set ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here

# Windows (PowerShell)

$env:ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"

# macOS/Linux

export ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
Run Development Server:DOSuvicorn main:app --reload --port 8000
Access the dashboard at [http://127.0.0.1:8000](http://127.0.0.1:8000).Running TestsExecute the automated test suite with pytest:DOSpytest
🌐 Deploying to VercelVoicePulse AI is optimized for Vercel's native FastAPI serverless preset.Push Repository: Ensure all local code is pushed to your GitHub repository:DOSgit add .
git commit -m "Prepare production deployment"
git push origin main
Import Project into Vercel:Navigate to the Vercel Dashboard and click Add New > Project.Select your VoicePulse_AI repository.Under Framework Preset, select FastAPI.Configure Environment Variables:Expand the Environment Variables section.Add the following entry:Key: ASSEMBLYAI_API_KEYValue: Your AssemblyAI API KeyTarget Environments: Check Production, Preview, and Development.Deploy:Click Deploy.Once complete, open your assigned .vercel.app URL and click Start Live Call Monitoring.📡 API EndpointsGET /Serves the primary enterprise monitoring dashboard (index.html).GET /api/tokenRetrieves a temporary authentication token from AssemblyAI V3.Headers Required: Server-side ASSEMBLYAI_API_KEYResponse:JSON{
  "token": "e301a2..."
}
POST /api/qa/evaluateEvaluates a transcript snippet for sales compliance risks.Payload:JSON{
  "transcript": "This payment has a guaranteed return of investment."
}
Response:JSON{
  "status": "Regulatory Financial Guarantee Violation",
  "whisper": "CRITICAL: Absolute or numeric financial guarantee detected. Immediate correction required!"
}
📄 LicenseThis project is open-source and available under the MIT License.
