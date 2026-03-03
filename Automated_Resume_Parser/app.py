from flask import Flask, render_template, request
import os
import pdfplumber
import docx
import spacy
import psycopg2

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# PostgreSQL connection (UPDATED)
conn = psycopg2.connect(
    host="localhost",
    database="resume_parser",
    user="postgres",
    password="yash@15"   # 🔴 PUT YOUR PASSWORD HERE
)
cursor = conn.cursor()

# Create table if not exists (UPDATED)
cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    skills TEXT
)
""")
conn.commit()


def extract_text(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text


def parse_resume(text):
    doc = nlp(text)

    name = "Not Found"
    email = "Not Found"
    skills_found = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    for token in doc:
        if token.like_email:
            email = token.text
            break

    SKILLS = [
        "python", "java", "sql", "flask", "django",
        "machine learning", "deep learning",
        "nlp", "html", "css", "javascript"
    ]

    text_lower = text.lower()
    for skill in SKILLS:
        if skill in text_lower:
            skills_found.append(skill)

    return name, email, ", ".join(skills_found)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["resume"]
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        text = extract_text(file_path)
        name, email, skills = parse_resume(text)

        cursor.execute(
            "INSERT INTO resumes (name, email, skills) VALUES (%s, %s, %s)",
            (name, email, skills)
        )
        conn.commit()

        result = {
            "name": name,
            "email": email,
            "skills": skills
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
