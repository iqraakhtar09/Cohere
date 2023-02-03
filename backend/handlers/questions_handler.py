from backend.database.questions import get_questions
import secrets


def get_random_question(answered_questions):
    candidate_questions = []
    questions = get_questions()
    for question in questions:
        if question.id not in answered_questions:
            candidate_questions.append(question)

    return secrets.choice(candidate_questions)
