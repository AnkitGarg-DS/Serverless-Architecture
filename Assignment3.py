import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    buckets = s3.list_buckets()['Buckets']

    for bucket in buckets:
        bucket_name = bucket['Name']
        try:
            enc = s3.get_bucket_encryption(Bucket=bucket_name)
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
            print(f"{bucket_name} is encrypted with: {rules}")
        except s3.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"{bucket_name} is NOT encrypted")
                unencrypted_buckets.append(bucket_name)
            else:
                print(f"Error checking {bucket_name}: {e}")

    print(f"Unencrypted buckets: {unencrypted_buckets}")
    return {
        'statusCode': 200,
        'body': f"Unencrypted buckets: {unencrypted_buckets}"
    }