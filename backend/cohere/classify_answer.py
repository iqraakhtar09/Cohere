import cohere

from backend.cohere.train_question import train_question


def classify_answer(question_id, answer, api_key):
    co = cohere.Client(api_key)
    examples = train_question(question_id)

    inputs = [
        answer,
    ]

    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )

    return response
