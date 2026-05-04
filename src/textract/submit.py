import boto3
import json
import uuid

sf = boto3.client('stepfunctions')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    job_id = str(uuid.uuid4())
    bucket = event.get('bucket', '')
    key = event.get('key', '')
    
    table = dynamodb.Table('worst-house-jobs')
    table.put_item(Item={
        'jobId': job_id,
        'status': 'RUNNING',
        'bucket': bucket,
        'key': key
    })
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'jobId': job_id})
    }
