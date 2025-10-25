import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    # --- Configuration ---
    BUCKET_NAME = 'ankit-s3-bucket-cleanup'
    DAYS_OLD = 30

    # --- Setup clients ---
    s3 = boto3.client('s3')

    # --- Calculate cutoff date ---
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=DAYS_OLD)

    print(f"Deleting files older than {DAYS_OLD} days (before {cutoff_date}) from bucket: {BUCKET_NAME}")

    # --- List all objects in the bucket ---
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in response:
        print("Bucket is empty.")
        return {"status": "empty"}

    deleted_files = []

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']

        # Compare object age
        if last_modified < cutoff_date:
            print(f"Deleting: {key} (LastModified: {last_modified})")
            s3.delete_object(Bucket=BUCKET_NAME, Key=key)
            deleted_files.append(key)
        else:
            print(f"Keeping: {key} (LastModified: {last_modified})")

    print(f"Deleted {len(deleted_files)} file(s): {deleted_files}")
    return {
        'statusCode': 200,
        'body': f"Deleted {len(deleted_files)} file(s): {deleted_files}"
    }
