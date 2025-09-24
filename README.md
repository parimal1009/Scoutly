# 🎯 Scoutly - Intelligent Talent Sourcing Platform

<div align="center">

![Scoutly Logo](https://img.shields.io/badge/Scoutly-AI%20Powered%20Talent%20Sourcing-blue?style=for-the-badge&logo=rocket)

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-16+-green?style=flat-square&logo=node.js)](https://nodejs.org)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react)](https://reactjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0+-47A248?style=flat-square&logo=mongodb)](https://mongodb.com)

**A multi-agent based intelligent candidate searching and sourcing platform that revolutionizes talent acquisition through AI-powered job description processing and automated candidate discovery.**

</div>

## 🌟 Overview

Scoutly is an advanced talent sourcing platform that leverages artificial intelligence to streamline the recruitment process. It automatically processes job descriptions, generates optimized search prompts, and sources candidates from multiple platforms including LinkedIn and GitHub.

### 🏗️ Architecture Overview

```mermaid
graph TB
    subgraph "Frontend Layer"
        UI[React Frontend<br/>Port 5173]
        UI --> |User Authentication| AUTH[Auth Context]
        UI --> |Job Processing| DASH[Dashboard]
    end
    
    subgraph "Backend Services"
        API[Express.js Backend<br/>Port 5000]
        AI[FastAPI AI Service<br/>Port 8000]
    end
    
    subgraph "AI Processing Pipeline"
        JDP[JD Processor]
        JDParser[JD Parser<br/>PDF/Image/Text]
        PG[Prompt Generator<br/>LLM Powered]
        SOURCER[Candidate Sourcer]
    end
    
    subgraph "Data Sources"
        LINKEDIN[LinkedIn API]
        GITHUB[GitHub API]
        WEB[Web Search<br/>Serper API]
    end
    
    subgraph "Storage Layer"
        MONGO[(MongoDB<br/>User Data & Jobs)]
        VECTOR[(Vector DB<br/>Candidate Profiles)]
    end
    
    subgraph "External Tools"
        OCR[Tesseract OCR]
        PDF[Poppler PDF]
        LLM[Groq LLM API]
    end
    
    %% Frontend connections
    UI --> |Auth Requests| API
    UI --> |JD Processing| AI
    
    %% Backend connections
    API --> |User Data| MONGO
    AI --> |Job Data| MONGO
    
    %% AI Pipeline
    AI --> JDP
    JDP --> JDParser
    JDParser --> |OCR/PDF Processing| OCR
    JDParser --> |PDF Processing| PDF
    JDParser --> PG
    PG --> |LLM Processing| LLM
    PG --> SOURCER
    
    %% Data sourcing
    SOURCER --> |Search Candidates| LINKEDIN
    SOURCER --> |Search Developers| GITHUB
    SOURCER --> |Web Search| WEB
    SOURCER --> |Store Profiles| VECTOR
    
    %% Styling
    classDef frontend fill:#e1f5fe
    classDef backend fill:#f3e5f5
    classDef ai fill:#e8f5e8
    classDef storage fill:#fff3e0
    classDef external fill:#fce4ec
    
    class UI,AUTH,DASH frontend
    class API,AI backend
    class JDP,JDParser,PG,SOURCER ai
    class MONGO,VECTOR storage
    class OCR,PDF,LLM,LINKEDIN,GITHUB,WEB external
