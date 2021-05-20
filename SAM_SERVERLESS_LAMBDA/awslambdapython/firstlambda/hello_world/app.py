import json


def first_lambda(event, context):

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "aws lambda is super cool...1"
        }),
    }
