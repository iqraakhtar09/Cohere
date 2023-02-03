from backend.utils import write_to_file
from backend.utils.get_printable_assessment import get_output


def save_answer_assessment(question, response):
    output = get_output(question, response)
    write_to_file.write_to_file("answers_1.txt", output)
