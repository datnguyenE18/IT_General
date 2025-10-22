import json

def lambda_handler(event, context):

    # In 'event' ra CloudWatch Logs để debug
    print("Event received:", event)

    name = "World"

    # 1. Lấy 'name' từ query string của API Gateway
    if 'queryStringParameters' in event and event['queryStringParameters'] and 'name' in event['queryStringParameters']:
        name = event['queryStringParameters']['name']

    # 2. Nếu không có thì thử lấy 'name' từ JSON body (dùng cho Test Event)
    elif 'name' in event:
        name = event['name']

    # Xây dựng nội dung trả về
    response_body = {
        "message": f"Hello {name} from Lambda!"
    }

    # Trả về response theo format mà API Gateway yêu cầu
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }
