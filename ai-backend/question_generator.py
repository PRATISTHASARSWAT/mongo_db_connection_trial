# question_generator.py

def generate_interview_questions(summary, skills, has_experience, has_projects):
    questions = []

    # 1️⃣ Experience-based question
    if has_experience:
        questions.append(
            "Can you walk me through your experience in your last organization and the key responsibilities you handled?"
        )
    else:
        questions.append(
            "As a fresher, how have you applied your academic knowledge through projects, internships, or self-learning?"
        )

    # 2️⃣ Project-based question
    if has_projects:
        questions.append(
            "Can you explain one of the projects you worked on, your role in it, and the challenges you faced?"
        )

    # 3️⃣ Skill-based technical question
    if skills:
        primary_skill = skills[0]
        questions.append(
            f"Can you explain your hands-on experience with {primary_skill} and how you have used it in real-world scenarios?"
        )

    # 4️⃣ Problem-solving question
    questions.append(
        "What was the most challenging technical problem you have faced so far, and how did you approach solving it?"
    )

    # Ensure max 4 relevant questions
    return questions[:4]
