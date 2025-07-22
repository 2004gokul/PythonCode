import json
import boto3
from config.settings import S3_BUCKET_NAME, S3_OUTPUT_PREFIX
from utils.logger import logger

s3 = boto3.client('s3')

def write_json_to_s3(data, file_name):
    try:
        key = f"{S3_OUTPUT_PREFIX}{file_name}_transformed.json"
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=key, Body=json.dumps(data, indent=2))
        logger.info(f"Written to S3: {key}")
    except Exception as e:
        logger.error(f"Error writing to S3: {e}")
