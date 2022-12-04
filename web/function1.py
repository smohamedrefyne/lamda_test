
import json

import os

def lambda_handler(event, context):
    print ("Hello World")

    return {
        'statusCode': 200,
        'body': json.dumps(list_of_dicts, default=str),
        'headers': {
            "Content-Type": "application/json"
        }
    }