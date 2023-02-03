from backend.database.connect import get_cursor


class Answer:
    def __init__(self, id, data, question_id, quality):
        self.id = id
        self.question_id = question_id
        self.data = data
        self.quality = quality


cursor = get_cursor()


def get_answers():
    select_answers = "select * from answers"

    cursor.execute(select_answers)

    answers_records = cursor.fetchall()

    answers = []

    for row in answers_records:
        answers.append(Answer(row[0], row[1], row[2], row[3]))

    return answers


def get_answers_by_question_id(id):
    select_answers = f"select * from answers where question_id = {id}"

    cursor.execute(select_answers)

    answers_records = cursor.fetchall()

    answers = []

    for row in answers_records:
        answers.append(Answer(row[0], row[1], row[2], row[3]))

    return answers