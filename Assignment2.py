import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    bucket_name = 'ankit-s3-bucket-cleanup'
    s3 = boto3.client('s3')
    deleted_files = []

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)
    print(f"Cutoff date: {cutoff_date}")

    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']
            age = (datetime.now(timezone.utc) - last_modified).days
            print(f"{key} last modified: {last_modified} ({age} days old)")

            if last_modified < cutoff_date:
                s3.delete_object(Bucket=bucket_name, Key=key)
                deleted_files.append(key)

    print(f"Deleted files: {deleted_files}")
    return {
        'statusCode': 200,
        'body': f"Deleted files: {deleted_files}"
    }