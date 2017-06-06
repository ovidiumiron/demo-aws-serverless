from __future__ import print_function

import json
from boto3 import resource


# The boto3 dynamoDB resource

def lambda_handler(event, context):
    dynamodb_resource = resource('dynamodb')
    id = "c55dcc73-44dc-404d-b725-49118b71d389"
    table = dynamodb_resource.Table("math")
    response = table.get_item(Key={'id': id})

    if "Item" in respose:
        return response["Item"]["result"]

    return None


