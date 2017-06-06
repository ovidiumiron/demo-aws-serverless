from boto3 import resource

def lambda_handler(event, context):
    dynamodb_resource = resource('dynamodb')

    table = dynamodb_resource.Table("math")
    id = "c55dcc73-44dc-404d-b725-49118b71d389"

    return table.put_item(
        Item={
        'id': id,
        'first':12,
        'second':4,
        "third": 55
    }
)
