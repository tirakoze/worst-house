import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['bucket']
    key = event['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    return {
        'statusCode': 200,
        'bucket': bucket,
        'key': key,
        'contentType': response['ContentType']
    }
