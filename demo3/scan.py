import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('math')
    response = table.scan(
    FilterExpression=Attr('result').non_exists()
    )
    # see
    # http://boto3.readthedocs.io/en/latest/_modules/boto3/dynamodb/conditions.html
    items = response['Items']
    return items
