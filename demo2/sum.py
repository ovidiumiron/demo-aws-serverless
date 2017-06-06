# curl -X POST -d '{"num1": 1, "num2":2}' https://3z66q4oft1.execute-api.eu-west-1.amazonaws.com/dev
def lambda_handler(event, context):
    return event["num1"] + event["num2"]
