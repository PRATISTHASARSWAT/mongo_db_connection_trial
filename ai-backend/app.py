from fastapi import FastAPI, UploadFile, File
from utils import extract_text
from parser import parse_resume, extract_experience_and_projects
from summarizer import generate_summary
from question_generator import generate_interview_questions

app = FastAPI()

@app.post("/parse-resume/")
async def parse_resume_api(file: UploadFile = File(...)):
    text = extract_text(file.file, file.filename)

    parsed_data = parse_resume(text)
    summary = generate_summary(text)

    has_experience, has_projects = extract_experience_and_projects(text)

    questions = generate_interview_questions(
        summary=summary,
        skills=parsed_data.get("skills", []),
        has_experience=has_experience,
        has_projects=has_projects
    )

    # Return full structured data
    return {
        "summary": summary,
        "parsed_data": {
            "skills": parsed_data.get("skills", []),
            "text": text
        },
        "interview_questions": questions
    }
