# 🚀 SkillSync AI

An AI-powered Resume Intelligence Platform that helps job seekers evaluate their resumes against job descriptions using a locally running Large Language Model (LLM).

SkillSync AI provides ATS analysis, resume parsing, skill-gap detection, personalized learning roadmaps, and professional resume insights without relying on paid cloud APIs.

---

## ✨ Features

- 📄 Resume Parsing (PDF & DOCX)
- 🎯 ATS Match Analysis
- 📊 Job Match Percentage
- 🧠 Skill Gap Detection
- 📚 Personalized Learning Roadmap
- 🤖 Local AI using Ollama + Llama 3.1
- ⚡ Modular Python Architecture
- 🧪 Automated Test Modules
- 💻 Streamlit Web Interface

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI
- Ollama
- Llama 3.1

### Resume Parsing
- pdfplumber
- python-docx

### Utilities
- JSON
- dotenv

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
SkillSync-AI/
│
├── ai/
├── parser/
├── services/
├── ui/
├── utils/
├── tests/
├── uploads/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Current Workflow

```text
Upload Resume
        ↓
Extract Resume Text
        ↓
Resume Parsing
        ↓
ATS Analysis
        ↓
Skill Gap Detection
        ↓
Learning Roadmap
```

---

## 📸 Application Preview

> Screenshots will be added after the final UI redesign.

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/aasthasinghh02/SkillSync-AI.git
cd SkillSync-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama from:

https://ollama.com

Pull Llama 3.1

```bash
ollama pull llama3.1
```

Run Ollama

```bash
ollama serve
```

Launch Application

```bash
streamlit run app.py
```

---

## 🧪 Testing

Run individual modules.

```bash
python -m tests.test_pdf
```

```bash
python -m tests.test_resume_parser
```

```bash
python -m tests.test_ats
```

```bash
python -m tests.test_skill_gap
```

```bash
python -m tests.test_roadmap
```

---

## 🎯 Future Improvements

- Professional Dashboard UI
- Cover Letter Generator
- Downloadable PDF Report
- Faster Modular Workflow
- Performance Optimization

---

## 👩‍💻 Author

**Aastha Singh**

GitHub:
https://github.com/aasthasinghh02

---

## ⭐ Project Status

Current Version

**Version 1.0 (In Active Development)**

The project is functional and continuously being improved with a focus on performance, UI/UX, and AI-powered career insights.