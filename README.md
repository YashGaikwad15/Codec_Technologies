# AI-Powered Chatbot

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


# Automated Resume Parser

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


# Stock Market Dashboard

## Overview
The **Stock Market Dashboard** is a web application built with **Python, Flask, yFinance, and Chart.js**. It allows users to visualize **historical stock prices** for any public company in an interactive and responsive dashboard.

This project demonstrates **data visualization, web development, and API integration**, making it ideal for internships or portfolio projects.

---

## Features

- Search for any public stock using its **ticker symbol** (e.g., AAPL, TSLA).  
- View **historical stock prices** (Open, High, Low, Close).  
- Interactive **line chart** visualization using **Chart.js**.  
- Responsive, modern UI with smooth animations.  
- Modular code structure (Python backend + separate CSS/JS files).  

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Data Source | yFinance API |
| Data Handling | Pandas |
| Frontend | HTML, CSS (responsive), JavaScript |
| Charting | Chart.js |

---


# Secure Authentication System

A **Flask-based secure authentication system** with:

- Signup, login, and logout functionality  
- Password hashing using **Werkzeug**  
- Session management using **Flask-Login**  
- Flash messages for feedback  
- Client-side form validation and password toggle with **JavaScript**  
- Responsive, modern UI with **CSS gradients and animations**  
- SQLite database for storing user accounts  

---

## **Features**

1. **Signup**
   - Users can create an account with a **unique username and email**  
   - Passwords are securely **hashed** before storing  

2. **Login**
   - Authenticate users with **username and password**  
   - Session management keeps users logged in  

3. **Dashboard**
   - Secure page accessible **only to logged-in users**  
   - Logout button to safely end session  

4. **Client-Side Enhancements**
   - Show/Hide password toggle  
   - Required field validation before form submission  
   - Smooth animations for inputs and flash messages  

---

