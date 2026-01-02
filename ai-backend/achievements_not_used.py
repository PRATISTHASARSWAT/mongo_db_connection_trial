import re

def extract_achievements(text: str):
    if not text:
        return []

    bullets = re.split(r"[-•]", text)
    return [b.strip() for b in bullets if len(b.split()) > 4]
