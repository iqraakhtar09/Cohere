from backend.database.connect import get_cursor


class Question:
    def __init__(self, id, data):
        self.id = id
        self.data = data


cursor = get_cursor()


def get_questions():
    select_questions = "select * from questions"

    cursor.execute(select_questions)

    questions_records = cursor.fetchall()

    questions = []

    for row in questions_records:
        questions.append(Question(row[0], row[1]))

    return questions


def get_question_by_id(id):
    select_questions = f"select * from questions where id={id}"

    cursor.execute(select_questions)

    questions_records = cursor.fetchall()

    for row in questions_records:
        return Question(row[0], row[1])
