import cohere
from cohere.classify import Example
import json
import sys

from backend.handlers.answers_handler import assess_answer
from backend.handlers.questions_handler import get_random_question
from backend.utils import write_to_file
from backend.utils.get_printable_assessment import get_output
from backend.utils.save_answer_assessment import save_answer_assessment

co = cohere.Client(sys.argv[1])


def emotions_demo():
    examples = [
        Example("I am so happy right know!", "happiness"),
        Example("I can't believe we did it! Wow!", "happiness"),
        Example("Thank you all, you are the best", "happiness"),
        Example("Congratulations", "happiness"),
        Example("You've done it well, son", "happiness"),

        Example("I heard your dog just died, my condolences", "sadness"),
        Example("We didn't win this time, unfortunately", "sadness"),
        Example("She's so mad right now", "sadness"),
        Example("We just broke up...", "sadness"),
        Example("I have no friends and nobody loves me(", "sadness"),

        Example("He joined the club without me", "anger"),
        Example("Just wait for my revenge", "anger"),
        Example("Stop mocking me, you idiot", "anger"),
        Example("I'll make them pay back", "anger"),
        Example("Get this thing done by tomorrow morning or else you're getting a sack!", "anger"),

        Example("I saw something really scary behind that door", "fear"),
        Example("I won't climb up there, it is too high for me even now", "fear"),
        Example("Is it me or the walls are moving closer", "fear"),
        Example("Kill this enormous black creature in the sink!", "fear"),
        Example("Slow down, you're gonna hit something", "fear"),

        Example("For me, really?!", "surprise"),
        Example("You are kidding, right? I can't believe it!", "surprise"),
        Example("Wow, it is amazing!", "surprise"),
        Example("No way, he did what?", "surprise"),
        Example("This it outstanding result! Didn't know you're so good at it", "surprise"),

        Example("Not the broccoli again", "disgust"),
        Example("Blah! I'm about to vomit!", "disgust"),
        Example("Don't eat that, it's gross!", "disgust"),
        Example("That smell in toilet, I'll never forget it", "disgust"),
        Example("You stink, don't get close to me!", "disgust"),

        Example("It's OK, I guess", "neutral"),
        Example("Feel free to look around", "neutral"),
        Example("Sorry, nevermind", "neutral"),
        Example("Just forget what I said back then", "neutral"),
        Example("Take your sits and listen carefully", "neutral"),
    ]

    inputs = [
        "every time",
        "I could see beautiful picturesque views around me",
        "This is why I came here",
        "We'll get over it, bad times will pass",
        "Please don't tell me! It is impossible!",
        "Oh god... Not cleaning Bob's desk again! He's so filthy!",
    ]

    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )

    output = json.dumps(
        [response.classifications[i].__dict__ for i in range(len(response.classifications))],
        default=lambda o: '<not serializable>',
        indent=4
    )

    print(output)

    write_to_file.write_to_file("emotions_1.txt", output)


answered_questions = [2, 3]
random_question = get_random_question(answered_questions)
assert random_question.id not in answered_questions

answer_assessment = assess_answer(random_question.id, sys.argv[2], sys.argv[1])

print(f"Question: {random_question.data}, Answer: {sys.argv[2]}, Answer quality: {answer_assessment}")
# print(get_output(random_question, answer_assessment))
# save_answer_assessment(random_question, answer_assessment)
