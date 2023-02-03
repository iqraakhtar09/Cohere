from backend.cohere.classify_answer import classify_answer


def assess_answer(question_id, answer, api_key):
    return classify_answer(question_id, answer, api_key).classifications[0].prediction
