import re

SECTION_HEADERS = {
    "education": ["education", "academic", "qualification"],
    "experience": ["experience", "employment", "work history"],
    "projects": ["projects", "project experience"],
    "skills": ["skills", "technical skills"],
    "achievements": ["achievements", "awards", "extra curricular", "activities"]
}

def extract_sections(text):
    text = text.lower()
    sections = {}
    current_section = None

    for line in text.split("\n"):
        for section, keywords in SECTION_HEADERS.items():
            if any(k in line for k in keywords):
                current_section = section
                sections[current_section] = []
                break

        if current_section:
            sections[current_section].append(line)

    return {
        k: " ".join(v).strip()
        for k, v in sections.items()
    }
