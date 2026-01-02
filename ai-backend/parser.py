import spacy
import re

nlp = spacy.load("en_core_web_sm")

# -------------------------
# Main Resume Parser
# -------------------------
def parse_resume(text):
    doc = nlp(text)

    # Email extraction
    email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

    # Phone extraction (India-friendly)
    phone = re.findall(r"\+?\d[\d -]{8,12}\d", text)

    # Skill extraction
    skill_keywords = [
        "python", "java", "sql", "machine learning", "deep learning",
        "excel", "power bi", "tableau", "fastapi", "django",
        "html", "css", "javascript", "nlp", "llm"
    ]

    skills = set()
    for token in doc:
        if token.text.lower() in skill_keywords:
            skills.add(token.text.capitalize())

    return {
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
        "skills": list(skills)
    }


# -------------------------
# Experience & Project Detection
# -------------------------
def extract_experience_and_projects(text):
    text_lower = text.lower()

    experience_keywords = [
        "experience", "worked at", "company", "organization",
        "intern", "employment", "role", "responsibilities"
    ]

    project_keywords = [
        "project", "developed", "built", "implemented",
        "designed", "created", "application", "system"
    ]

    has_experience = any(word in text_lower for word in experience_keywords)
    has_projects = any(word in text_lower for word in project_keywords)

    return has_experience, has_projects
