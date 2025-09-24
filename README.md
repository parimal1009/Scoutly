# Scoutly
A multi-agent based intelligent candidate searching and sourcing

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

## 🏗️ Architecture Overview -`

### Alternative Text-Based Representation:

```
                    Scoutly - Intelligent Talent Sourcing Platform
                                    
👤 User → 🎨 PRESENTATION LAYER → 🔐 APPLICATION SERVICES
          │                       │
          ├─ React SPA (5173)     ├─ Express.js Backend (5000)
          ├─ Auth Context         └─ FastAPI AI Service (8000)
          ├─ Real-time Updates            │
          └─ Drag & Drop                  ▼
                                  
          🤖 AI PROCESSING PIPELINE
          ┌─────────────────────────────────────────────────────────┐
          │ JD Processor → JD Parser → Prompt Gen → Search Agents   │
          │                                             │           │
          │ Profile Ranker ← Candidate Sourcer ←────────┘           │
          └─────────────────────────────────────────────────────────┘
                                    ▼
          🌐 EXTERNAL INTEGRATIONS
          ├─ AI Services (Groq, Tesseract, Poppler)
          ├─ Search APIs (Serper, LinkedIn, GitHub)
          ├─ Security & Analytics
          └─ Authentication & JWT
                                    ▼
          💾 DATA PERSISTENCE
          ├─ MongoDB (User Data, Jobs, Auth)
          ├─ Vector Database (Embeddings, ML)
          └─ Caching Layer (Performance)
```

### How to Use This Diagram:

1. **Copy the XML code** from above
2. **Go to [draw.io](https://app.diagrams.net/)**
3. **Create a new diagram**
4. **Go to File → Import from → Text**
5. **Paste the XML code**
6. **The diagram will be generated automatically**

You can then:
- **Export as PNG/SVG** for your README
- **Edit and customize** colors, shapes, and text
- **Add or remove components** as needed
- **Save and share** the diagram

### Adding to Your README:

Once you've generated and exported the diagram as an image, replace this section with:

```markdown
### Architecture Overview

<div align="center">

![Scoutly Architecture](./images/architecture-diagram.png)

*Comprehensive Multi-Agent AI Architecture for Intelligent Talent Sourcing*

</div>
