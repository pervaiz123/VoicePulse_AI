# VoicePulse AI 🎙️⚡

> **Enterprise Real-Time Sales QA & Compliance Monitoring Engine**

[![Live Demo](https://img.shields.io/badge/Vercel-Live%20Demo-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://voice-pulse-1ehg7rieo-ahmed-a283.vercel.app/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![AssemblyAI V3](https://img.shields.io/badge/AssemblyAI-V3%20Streaming-blueviolet?style=for-the-badge)](https://www.assemblyai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

🌐 **Live Application Demo:** [https://voice-pulse-1ehg7rieo-ahmed-a283.vercel.app/](https://voice-pulse-1ehg7rieo-ahmed-a283.vercel.app/)

---

## 📌 Executive Overview

**VoicePulse AI** is a high-performance, real-time speech analytics and compliance enforcement platform designed for sales and support environments. Powered by **AssemblyAI’s V3 Streaming WebSocket API** and **FastAPI**, the system streams live microphone audio, generates low-latency transcriptions, and dynamically evaluates interactions against regulatory rules—such as identifying unauthorized financial guarantees or missing mandatory disclosures—to deliver instant **AI Supervisor Whispers** during live calls.

---

## ⚡ Core Features

* **Real-Time Speech-to-Text**: Direct WebSocket streaming with AssemblyAI V3 for sub-second transcript rendering.
* **Ephemeral Authentication Token Broker**: Backend token retrieval (`/api/token`) ensuring frontend clients stream securely without exposing root credentials.
* **Automated QA Compliance Engine**: Dynamic evaluation endpoint (`/api/qa/evaluate`) analyzing live transcript text for regulatory breaches and risk indicators.
* **Live Supervisor Whispers**: Instant real-time UI alerts when high-risk language or compliance violations are detected.
* **Serverless Cloud Ready**: Built on FastAPI with native support for local Uvicorn development and Vercel Serverless Function execution.

---

## 🏗️ System Architecture & Data Flow

```text
┌─────────────────┐       1. Request Temp Token      ┌────────────────────────┐
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
│  ([streaming.assemblyai.com/v3](https://streaming.assemblyai.com/v3))  │                 └────────────────────────┘
└─────────────────────────────────┘
