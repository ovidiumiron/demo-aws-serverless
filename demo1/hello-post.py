# curl -X POST -d '{"name": "Ovidiu"}' https://3z66q4oft1.execute-api.eu-west-1.amazonaws.com/dev
def lambda_handler(event, context):
    return 'Hello from Lambda {0}'.format(event["name"])
