import boto3
import json
from config.settings import S3_BUCKET_NAME, S3_INPUT_PREFIX
from utils.logger import logger

s3 = boto3.client('s3')

def read_json_from_s3():
    objects = s3.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=S3_INPUT_PREFIX).get('Contents', [])
    data = []
    for obj in objects:
        key = obj['Key']
        if key.endswith('.json'):
            try:
                content = s3.get_object(Bucket=S3_BUCKET_NAME, Key=key)['Body'].read()
                data.append(json.loads(content))
            except Exception as e:
                logger.error(f"Failed to read from S3: {e}")
    return data
