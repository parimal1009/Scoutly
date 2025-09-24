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

## 🏗️ Architecture Overview - Draw.io Diagram

### Instructions to Generate the Architecture Diagram:
1. Go to [draw.io](https://app.diagrams.net/) (formerly draw.io)
2. Create a new blank diagram
3. Go to File > Import from > Text
4. Copy and paste the XML code below
5. The diagram will be automatically generated

### Draw.io XML Code:

```xml
<mxfile host="app.diagrams.net" modified="2024-01-01T00:00:00.000Z" agent="5.0" etag="xxx" version="22.1.16">
  <diagram name="Scoutly Architecture" id="scoutly-arch">
    <mxGraphModel dx="1422" dy="754" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Title -->
        <mxCell id="title" value="Scoutly - Intelligent Talent Sourcing Platform" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1;fontColor=#2E86C1;" vertex="1" parent="1">
          <mxGeometry x="300" y="20" width="600" height="40" as="geometry" />
        </mxCell>

        <!-- User Layer -->
        <mxCell id="user" value="👤 User" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="100" width="120" height="60" as="geometry" />
        </mxCell>

        <!-- Presentation Layer -->
        <mxCell id="presentation-layer" value="🎨 PRESENTATION LAYER" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=16;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="200" y="80" width="280" height="180" as="geometry" />
        </mxCell>
        
        <mxCell id="react-spa" value="React SPA&#xa;Port 5173&#xa;• Modern UI&#xa;• Tailwind CSS&#xa;• Dashboard&#xa;• File Upload" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="220" y="110" width="120" height="80" as="geometry" />
        </mxCell>
        
        <mxCell id="auth-context" value="Auth Context&#xa;• JWT Management&#xa;• Session Handling&#xa;• Protected Routes" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="350" y="110" width="120" height="80" as="geometry" />
        </mxCell>

        <mxCell id="real-time" value="Real-time Updates&#xa;• Status Monitoring&#xa;• Job Progress&#xa;• Error Handling" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="220" y="200" width="120" height="50" as="geometry" />
        </mxCell>

        <mxCell id="drag-drop" value="Drag & Drop&#xa;• Multi-format&#xa;• PDF/Image/Text" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="350" y="200" width="120" height="50" as="geometry" />
        </mxCell>

        <!-- Application Services -->
        <mxCell id="app-services" value="🔐 APPLICATION SERVICES" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=16;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="520" y="80" width="280" height="180" as="geometry" />
        </mxCell>

        <mxCell id="express-backend" value="Express.js Backend&#xa;Port 5000&#xa;• Authentication&#xa;• API Gateway&#xa;• JWT Tokens&#xa;• CORS Config" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="540" y="110" width="120" height="80" as="geometry" />
        </mxCell>

        <mxCell id="fastapi-service" value="FastAPI AI Service&#xa;Port 8000&#xa;• AI Orchestration&#xa;• Processing Pipeline&#xa;• Async Jobs&#xa;• API Docs" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="670" y="110" width="120" height="80" as="geometry" />
        </mxCell>

        <mxCell id="middleware" value="Middleware Layer&#xa;• Rate Limiting&#xa;• Error Handling&#xa;• Request Validation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="540" y="200" width="250" height="50" as="geometry" />
        </mxCell>

        <!-- AI Processing Pipeline -->
        <mxCell id="ai-pipeline" value="🤖 AI PROCESSING PIPELINE" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=16;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="200" y="300" width="600" height="120" as="geometry" />
        </mxCell>

        <!-- AI Agents Flow -->
        <mxCell id="jd-processor" value="JD Processor&#xa;• Multi-format&#xa;• OCR Integration" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="220" y="330" width="80" height="60" as="geometry" />
        </mxCell>

        <mxCell id="jd-parser" value="JD Parser&#xa;• Text Extract&#xa;• Requirements" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="310" y="330" width="80" height="60" as="geometry" />
        </mxCell>

        <mxCell id="prompt-gen" value="Prompt Gen&#xa;• LLM Powered&#xa;• Query Optimization" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="400" y="330" width="80" height="60" as="geometry" />
        </mxCell>

        <mxCell id="search-agents" value="Search Agents&#xa;• Multi-platform&#xa;• Real-time" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="490" y="330" width="80" height="60" as="geometry" />
        </mxCell>

        <mxCell id="candidate-sourcer" value="Candidate&#xa;Sourcer&#xa;• LinkedIn&#xa;• GitHub" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="580" y="330" width="80" height="60" as="geometry" />
        </mxCell>

        <mxCell id="profile-ranker" value="Profile Ranker&#xa;• AI Scoring&#xa;• ML Models" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="670" y="330" width="80" height="60" as="geometry" />
        </mxCell>

        <!-- External Integrations -->
        <mxCell id="external-integrations" value="🌐 EXTERNAL INTEGRATIONS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=16;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="200" y="460" width="600" height="120" as="geometry" />
        </mxCell>

        <mxCell id="ai-services" value="AI Services&#xa;• Groq LLM&#xa;• Tesseract OCR&#xa;• Poppler PDF" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="220" y="490" width="110" height="70" as="geometry" />
        </mxCell>

        <mxCell id="search-apis" value="Search APIs&#xa;• Serper API&#xa;• LinkedIn API&#xa;• GitHub API" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="350" y="490" width="110" height="70" as="geometry" />
        </mxCell>

        <mxCell id="security-analytics" value="Security & Analytics&#xa;• Rate Limiting&#xa;• Monitoring&#xa;• Performance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="480" y="490" width="110" height="70" as="geometry" />
        </mxCell>

        <mxCell id="auth-security" value="Authentication&#xa;• JWT Tokens&#xa;• bcrypt Hash&#xa;• Session Mgmt" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="610" y="490" width="110" height="70" as="geometry" />
        </mxCell>

        <!-- Data Persistence -->
        <mxCell id="data-persistence" value="💾 DATA PERSISTENCE" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=16;fontStyle=1;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="200" y="620" width="600" height="120" as="geometry" />
        </mxCell>

        <mxCell id="mongodb" value="MongoDB&#xa;• User Data&#xa;• Job Records&#xa;• Authentication&#xa;• Analytics" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#148F77;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="250" y="650" width="150" height="70" as="geometry" />
        </mxCell>

        <mxCell id="vector-db" value="Vector Database&#xa;• Candidate Embeddings&#xa;• Similarity Search&#xa;• ML Models&#xa;• Efficient Retrieval" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="450" y="650" width="150" height="70" as="geometry" />
        </mxCell>

        <mxCell id="caching" value="Caching Layer&#xa;• Processed JDs&#xa;• Search Results&#xa;• Performance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="620" y="650" width="150" height="70" as="geometry" />
        </mxCell>

        <!-- Performance Metrics Box -->
        <mxCell id="performance-box" value="⚡ PERFORMANCE METRICS&#xa;• Async Processing&#xa;• Real-time Updates&#xa;• Error Recovery&#xa;• Rate Limiting&#xa;• Health Monitoring" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFCE9F;strokeColor=#D79B00;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="850" y="300" width="200" height="120" as="geometry" />
        </mxCell>

        <mxCell id="tech-stack" value="🛠️ TECHNOLOGY STACK&#xa;Frontend: React 18, Tailwind&#xa;Backend: Express.js, MongoDB&#xa;AI: FastAPI, Groq, Tesseract&#xa;APIs: Serper, LinkedIn, GitHub&#xa;Security: JWT, bcrypt, CORS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFCE9F;strokeColor=#D79B00;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="850" y="450" width="200" height="140" as="geometry" />
        </mxCell>

        <!-- Arrows for flow -->
        <mxCell id="user-to-react" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#dae8fc;strokeColor=#6c8ebf;" edge="1" parent="1" source="user" target="react-spa">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="react-to-express" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#f8cecc;strokeColor=#b85450;" edge="1" parent="1" source="react-spa" target="express-backend">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="express-to-fastapi" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#fff2cc;strokeColor=#d6b656;" edge="1" parent="1" source="express-backend" target="fastapi-service">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="flow-arrow1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#e1d5e7;strokeColor=#9673a6;" edge="1" parent="1" source="jd-processor" target="jd-parser">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="flow-arrow2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#e1d5e7;strokeColor=#9673a6;" edge="1" parent="1" source="jd-parser" target="prompt-gen">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="flow-arrow3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#e1d5e7;strokeColor=#9673a6;" edge="1" parent="1" source="prompt-gen" target="search-agents">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="flow-arrow4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#e1d5e7;strokeColor=#9673a6;" edge="1" parent="1" source="search-agents" target="candidate-sourcer">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="flow-arrow5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;fillColor=#e1d5e7;strokeColor=#9673a6;" edge="1" parent="1" source="candidate-sourcer" target="profile-ranker">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Connections to external services -->
        <mxCell id="ai-to-external" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;" edge="1" parent="1" source="fastapi-service" target="ai-services">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="730" y="200" as="sourcePoint" />
            <mxPoint x="275" y="490" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <mxCell id="search-to-apis" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;fillColor=#d5e8d4;strokeColor=#82b366;dashed=1;" edge="1" parent="1" source="search-agents" target="search-apis">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Connections to database -->
        <mxCell id="backend-to-mongo" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;fillColor=#f8cecc;strokeColor=#b85450;dashed=1;" edge="1" parent="1" source="express-backend" target="mongodb">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="600" y="260" as="sourcePoint" />
            <mxPoint x="325" y="650" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <mxCell id="ranker-to-vector" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;" edge="1" parent="1" source="profile-ranker" target="vector-db">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

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
