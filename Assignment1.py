import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Stop instances with tag Auto-Stop=True
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Auto-Stop', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    stop_ids = [i['InstanceId'] for r in stop_response['Reservations'] for i in r['Instances']]
    if stop_ids:
        print(f"Stopping instances: {stop_ids}")
        ec2.stop_instances(InstanceIds=stop_ids)
    else:
        print("No instances found to stop.")

    # Start instances with tag Auto-Start=True
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Auto-Start', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )
    start_ids = [i['InstanceId'] for r in start_response['Reservations'] for i in r['Instances']]
    if start_ids:
        print(f"Starting instances: {start_ids}")
        ec2.start_instances(InstanceIds=start_ids)
    else:
        print("No instances found to start.")

    return {
        'statusCode': 200,
        'body': f"Stopped: {stop_ids}, Started: {start_ids}"
    }