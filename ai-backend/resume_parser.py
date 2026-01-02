import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_education(text):
    doc = nlp(text)
    universities = []

    for ent in doc.ents:
        if ent.label_ in ["ORG"]:
            if any(word in ent.text.lower() for word in ["university", "college", "institute"]):
                universities.append(ent.text)

    return list(set(universities))


def extract_companies(text):
    doc = nlp(text)
    companies = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            companies.append(ent.text)

    companies = list(dict.fromkeys(companies))
    current_company = companies[0] if companies else None

    return {
        "companies": companies,
        "current_or_last_company": current_company
    }
