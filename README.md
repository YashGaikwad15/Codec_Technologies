1. AI-Powered Chatbot

A professional AI-powered chatbot built with Python, Flask, and NLP.  

## Features
- Contextual responses using sentence-transformers
- Logs chats to SQLite database
- Modern and responsive web interface
- Handles unknown queries gracefully

## Run Locally
1. Clone repo: `git clone <repo-url>`
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run app: `python app.py`
6. Open browser: `http://127.0.0.1:5000`


2. Automated Resume Parser

## Overview
The **Automated Resume Parser** is a web application built with **Python, Flask, spaCy, and PostgreSQL**. It extracts structured information such as **name, email, and skills** from uploaded resumes (PDF or DOCX) and stores the data in a database for easy retrieval and analysis.

This project demonstrates **NLP, web development, and database integration** — perfect for internship or portfolio presentations.

---

## Features

- Upload **PDF** or **DOCX** resumes.
- Automatically extract:
  - Candidate Name
  - Email Address
  - Skills (keyword-based extraction)
- Store parsed data in **PostgreSQL**.
- Display parsed results on a clean, professional web interface.
- Securely handles file uploads.
- Modern UI with animations and result cards.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| NLP | spaCy (`en_core_web_sm`) |
| Database | PostgreSQL |
| Frontend | HTML, CSS (modern UI), JavaScript |
| File Parsing | pdfplumber, python-docx |

---
