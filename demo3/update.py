from boto3 import resource
dynamodb_resource = resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb_resource.Table("math")

    return table.update_item(
    Key={
        'id': 'c55dcc73-44dc-404d-b725-49118b71d389',
    },
    UpdateExpression='SET result = :val1',
    ExpressionAttributeValues={
        ':val1':29
    })
