import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    job_id = event.get('pathParameters', {}).get('jobId', '')
    table = dynamodb.Table('worst-house-jobs')
    
    response = table.get_item(Key={'jobId': job_id})
    item = response.get('Item', {})
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(item)
    }
