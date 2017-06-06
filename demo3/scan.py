import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('math')
    response = table.scan(
    FilterExpression=Attr('result').exists()
    )
    items = response['Items']
    return items
