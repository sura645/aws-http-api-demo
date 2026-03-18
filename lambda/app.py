import json

orders = {}

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method")

    if method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps(orders)
        }

    elif method == "POST":
        body = json.loads(event.get("body", "{}"))
        order_id = body.get("id")
        orders[order_id] = body

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Order created", "data": body})
        }

    elif method == "PUT":
        body = json.loads(event.get("body", "{}"))
        order_id = body.get("id")

        if order_id in orders:
            orders[order_id] = body
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Order updated"})
            }

    elif method == "DELETE":
        order_id = event.get("queryStringParameters", {}).get("id")

        if order_id in orders:
            del orders[order_id]
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Order deleted"})
            }

    return {
        "statusCode": 400,
        "body": json.dumps({"message": "Invalid request"})
    }
