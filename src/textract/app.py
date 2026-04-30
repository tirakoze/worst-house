import json
import boto3

textract = boto3.client('textract')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['bucket']
    key = event['key']
    
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        }
    )
    
    text_blocks = []
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            text_blocks.append(block['Text'])
    
    return {
        'statusCode': 200,
        'bucket': bucket,
        'key': key,
        'extracted_text': ' '.join(text_blocks)
    }
