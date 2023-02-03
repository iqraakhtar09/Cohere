from backend.database import answers, questions
from cohere.classify import Example


def train_question(question_id):
    answer_list = answers.get_answers_by_question_id(question_id)

    examples = []

    for i in range(len(answer_list)):
        examples.append(Example(answer_list[i].data, answer_list[i].quality))

    return examples
