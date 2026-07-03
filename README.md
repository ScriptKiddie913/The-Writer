<div align="center">

# 🖋️ The Writer

### Your Local, Private AI Publishing House

**Turn a single idea into a fully written, beautifully typeset book, report, or collection — without your data ever leaving your machine.**

[![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)](#)
[![Made with FastAPI](https://img.shields.io/badge/backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](#)
[![Powered by Ollama](https://img.shields.io/badge/AI%20engine-Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)](#)
[![100% Local](https://img.shields.io/badge/privacy-100%25%20local-6a5acd?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](#)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)](#)

<br>

**No cloud APIs. No subscriptions. No data leaving your device.**
**Everything runs on your own hardware, powered by your own local AI models.**

</div>

---

## ✨ What is The Writer?

**The Writer** is a self-hosted, AI-assisted writing studio that plans, drafts, revises, and typesets long-form documents from a single prompt. Give it a title, a premise, and a few notes — it handles outlining, chapter-by-chapter drafting, continuity checking, and final PDF production, all inside a clean, live-updating dashboard.

Whether you're drafting a novel, assembling a poetry collection, or producing a polished executive report, The Writer turns a blank page into a finished, print-ready document.

> 🔒 **Privacy first.** Every generation runs against a local AI model on your own machine. Nothing is ever uploaded to a third-party service.

---

## 🎯 Highlights

| | |
|---|---|
| 📚 **Multi-Format Writing** | Novels, short story collections, poetry collections, and executive reports |
| 🧠 **Local AI, Your Choice** | Bring your own model — swap models freely, no vendor lock-in |
| 📎 **Knowledge Base Ingestion** | Feed in CSV, DOCX, PPTX, XLSX, Markdown, and PDF source material |
| 🎨 **Designer Themes** | Multiple built-in visual themes for print-ready PDF output |
| 📊 **Rich Report Blocks** | KPI cards, charts, timelines, risk matrices, IOC/CVE tables, and more |
| 🖥️ **Live Dashboard** | Watch chapters get written in real time with a clean, modern UI |
| 🗂️ **Multi-Project Workspace** | Manage and track several documents at once |
| 📄 **Print-Ready PDF Export** | Professional typography, custom fonts, and themed layouts out of the box |
| ⏸️ **Resume Anywhere** | Pause, close, and resume long-running projects without losing progress |
| 💻 **Runs Anywhere** | Native Python app or packaged desktop build — your call |

---

## 🧰 Tech Stack

The Writer is built entirely on open, well-established tooling:

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-2C3E50?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Engine-8A2BE2?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![JavaScript](https://img.shields.io/badge/Vanilla%20JS-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</div>

- **Backend Framework:** FastAPI + Uvicorn
- **AI Engine:** [Ollama](https://ollama.com) — fully local model inference, no external API calls
- **Data Layer:** SQLite (zero-config, file-based, portable)
- **PDF Engine:** ReportLab — custom typography, vector charts, and themed layouts
- **Document Ingestion:** python-docx, python-pptx, openpyxl, PyMuPDF, pypdf
- **Frontend:** Lightweight vanilla HTML/CSS/JS — no build step, no framework bloat
- **Packaging:** Available as a native Python app or a bundled desktop build

---

## 🤖 Models

The Writer is **model-agnostic** — it talks to whatever you have running in Ollama. Nothing is hardcoded to a single vendor.

- **Writing / Reasoning:** any chat-capable model pulled into Ollama (e.g. `llama3.1:8b` or your preferred local model)
- **Embeddings:** any Ollama embedding-capable model for knowledge base search
- **Vision / OCR:** any local vision model for scanned documents and images

Check what's installed and available at any time from inside the dashboard, or via:

```bash
ollama list
```

Pull a new model:

```bash
ollama pull llama3.1:8b
```

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com) installed and running locally
- At least one chat-capable model pulled into Ollama

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama

```bash
ollama serve
```

### 4. Launch The Writer

```bash
python3 book.py
```

### 5. Open the dashboard

Navigate to:

```
http://localhost:8000
```

That's it — create your first project, pick a mode and theme, and start writing.

---

## 📖 Supported Document Modes

| Mode | Description |
|---|---|
| 📕 **Novel** | Full-length fiction with chapter-by-chapter continuity |
| 📗 **Short Story Collection** | Multiple independent short works |
| 📘 **Poetry Collection** | Verse-focused layout with dedicated typography |
| 📊 **Executive Report** | Business, technical, academic, legal, and analytical report formats — including specialized profiles like threat intelligence reports, investment memos, and technical manuals |

Each mode automatically adapts formatting, structure, and available content blocks (tables, charts, callouts, timelines, and more) to match the type of document you're producing.

---

## 🎨 Themes

Choose from a set of curated visual themes that control both the on-screen dashboard accent and the final PDF's typography and color palette — from warm literary classics to sleek modern corporate layouts.

---

## 🗺️ Roadmap

- [ ] Additional document themes
- [ ] Expanded language support
- [ ] Collaborative multi-user projects
- [ ] Export to additional formats (EPUB, DOCX)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

### Built with ❤️ by **disavowed913**

<sub>The Writer — write privately, publish beautifully.</sub>

</div>
