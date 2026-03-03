import pdfplumber
import docx
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages])
        return text
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text
    else:
        return ""

def parse_resume(file_path):
    text = extract_text(file_path)
    doc = nlp(text)

    # Extract basic info
    name = ""
    skills = []
    education = []

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text
        if ent.label_ == "ORG":
            education.append(ent.text)

    # Extract skills by keyword matching
    skill_keywords = ["Python","Java","C++","SQL","Machine Learning","Data Analysis","Excel","AWS","Flask","Django"]
    for skill in skill_keywords:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "name": name,
        "skills": skills,
        "education": education
    }