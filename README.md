# ✍️ The Writer
### Local Multi-Agent Autonomous Writing System powered by Ollama

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-black?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)
![Offline](https://img.shields.io/badge/100%25-Offline-success?style=for-the-badge)
![MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

## 📖 Overview

**The Writer** is a fully local multi-agent autonomous writing platform that orchestrates multiple Ollama models to collaboratively generate long-form documents.

Unlike traditional AI writing applications that rely on a single model and repeated prompting, The Writer coordinates specialized AI agents responsible for planning, drafting, reviewing, continuity management, editing, and quality assurance.

Everything runs locally.

No cloud APIs.

No subscriptions.

No external AI services.

Simply configure your project once, press **Start**, and the system autonomously produces professional-quality documents from beginning to end.

---

# ✨ Features

- 🧠 Multi-Agent Writing Pipeline
- 📚 Long-form Novel Generation
- 📖 Short Story Collections
- ✒ Poetry Collections
- 📊 Executive Reports
- 🗂 Project-specific Knowledge Bases
- 🔍 Local OCR for PDFs & Images
- 📑 Retrieval-Augmented Generation (RAG)
- 📚 Story Bible Generation
- 🧾 Professional PDF Export
- 🔄 Crash Recovery & Resume
- 🖥 Browser Dashboard
- ⚡ Multiple Ollama Models
- 🔒 Completely Offline
- 📦 Single Python File

---

# 🧩 Writing Modes

| Mode | Description |
|-------|-------------|
| 📚 Novel | Multi-chapter long-form fiction with persistent continuity |
| 📖 Short Stories | Autonomous anthology generation |
| ✍ Poetry | Poetry collections with thematic consistency |
| 📊 Executive Report | Professional reports with structured layouts and tables |

---

# 🏗 Multi-Agent Architecture

Each project can contain any number of specialized agents.

Example workflow:

```text
Architect
      │
      ▼
Outline Planner
      │
      ▼
Section Planner
      │
      ▼
Primary Writer
      │
      ▼
Continuity Validator
      │
      ▼
Reviewer
      │
      ▼
Editor
      │
      ▼
Final Formatter
```

Each agent can run on a completely different Ollama model.

---

# 🧠 Knowledge Base

Every project owns its own isolated knowledge base.

Supported sources include:

- PDFs
- Scanned PDFs
- Images
- Screenshots
- Research Papers
- Notes
- Plain Text
- Documentation

Uploaded content is automatically

```
OCR
↓

Chunked

↓

Embedded

↓

Indexed

↓

Retrieved

↓

Injected into Agent Context
```

Knowledge is never shared between projects.

---

# 📚 Persistent Memory

The system continuously maintains:

- Story Bible
- Character Registry
- World Building
- Timeline
- Relationships
- Locations
- Objects
- Previous Chapters
- Plot Threads
- Editorial Decisions

allowing books to extend well beyond typical context limitations.

---

# 📑 Retrieval-Augmented Generation

The Writer includes a fully local RAG pipeline.

Features include

- Semantic Retrieval
- Embeddings
- Context Injection
- Long-term Memory
- Knowledge Search
- Chapter Recall
- Project Isolation

---

# 🔍 OCR Pipeline

Knowledge extraction is performed locally.

Supported inputs

- PDFs
- Scanned Books
- Images
- Screenshots
- Photos
- Documents

OCR Workflow

```
PDF

↓

Extract Text

↓

No Text Layer?

↓

Rasterize Pages

↓

Vision OCR

↓

Knowledge Chunks

↓

Embeddings

↓

Project Memory
```

---

# 🎨 Themes

Projects support customizable themes for generated PDFs.

Theme controls

- Typography
- Fonts
- Color Palette
- Headings
- Cover Pages
- Section Styling
- Layout

Executive Reports additionally support

- Professional Tables
- Section Banners
- Report Styling

---

# 📄 Export Formats

Supported outputs

- PDF
- DOCX *(planned)*
- PPTX *(planned)*
- Markdown *(planned)*

---

# 💻 Technology Stack

## Backend

- Python
- FastAPI
- SQLite

## AI

- Ollama
- Local LLMs
- Local Vision Models
- Local Embedding Models

## Retrieval

- Vector Embeddings
- Semantic Search
- RAG Pipeline

## OCR

- glm-ocr
- PyMuPDF
- PyPDF

## Document Generation

- ReportLab
- python-docx
- python-pptx
- openpyxl

## Frontend

- HTML
- CSS
- JavaScript

No React.

No Electron.

No external frontend frameworks.

---

# 📂 Project Workflow

```
Create Project
        │
        ▼
Select Writing Mode
        │
        ▼
Configure Agents
        │
        ▼
Attach Knowledge Base
        │
        ▼
OCR & Embeddings
        │
        ▼
Project Memory
        │
        ▼
Architecture Planning
        │
        ▼
Chapter Planning
        │
        ▼
Writing
        │
        ▼
Review
        │
        ▼
Continuity Validation
        │
        ▼
Formatting
        │
        ▼
Professional PDF
```

---

# 🤖 Recommended Ollama Models

| Purpose | Suggested Models |
|----------|-----------------|
| Planning | qwen3, deepseek-r1 |
| Writing | llama3.1, qwen3 |
| Editing | gemma3, mistral |
| OCR | glm-ocr |
| Embeddings | nomic-embed-text |

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/the-writer.git

cd the-writer

pip install -r requirements.txt

ollama serve

python writer.py
```

Open

```
http://localhost:8000
```

---

# 🔒 Privacy

✔ Fully Offline

✔ No External APIs

✔ No Cloud AI

✔ Local Knowledge Storage

✔ Local OCR

✔ Local LLMs

✔ Project Isolation

---

# 📜 License

MIT License

Copyright © 2026 Sagnik Saha

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork it

🐞 Report issues

💡 Suggest new features

---

<p align="center">

### Built with ❤️ by **Sagnik Saha**

**The Writer — Bringing autonomous long-form writing entirely offline.**

</p>
