import json


def get_output(question, response):
    # TODO add question as top level of json structure, not separately
    output = json.dumps(question.__dict__, indent=4) + '\n'
    output += json.dumps(
        [response.classifications[i].__dict__ for i in range(len(response.classifications))],
        default=lambda o: '<not serializable>',
        indent=4
    )

    return output
