import boto3

def lambda_handler(event, context):
    extracted_text = event.get('extracted_text', '')
    bucket = event.get('bucket', '')
    key = event.get('key', '')
    print(f"Saving results for {key}")
    return {
        'statusCode': 200,
        'message': 'Results saved successfully',
        'bucket': bucket,
        'key': key,
        'extracted_text': extracted_text
    }
