import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('worst-house-records')
    http_method = event.get('httpMethod', 'GET')
    
    if http_method == 'GET':
        response = table.scan()
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(response['Items'])
        }
    
    elif http_method == 'DELETE':
        record_id = event.get('pathParameters', {}).get('recordId', '')
        table.delete_item(Key={'recordId': record_id})
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Deleted successfully'})
        }
    
    return {
        'statusCode': 400,
        'body': json.dumps({'message': 'Unsupported method'})
    }
