import json
import os


def dict_types(event, context):
    print(event)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1')
    print(os.getenv('param1'))
    print(os.getenv('param2'))
    john_scores = event["john"]
    scores = []
    for score in john_scores:
        print(score)
    return event   