import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volume_id = 'vol-0787bd263dd1e5a05'
    retention_days = 30
    deleted_snapshots = []

    # Step 1: Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=f"Automated backup of {volume_id} on {datetime.now().isoformat()}"
    )
    snapshot_id = snapshot['SnapshotId']
    print(f"Created snapshot: {snapshot_id}")

    # Step 2: List and delete old snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=retention_days)

    for snap in snapshots:
        if snap['VolumeId'] == volume_id and snap['StartTime'] < cutoff_date:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            deleted_snapshots.append(snap['SnapshotId'])

    print(f"Deleted snapshots: {deleted_snapshots}")
    return {
        'statusCode': 200,
        'body': {
            'created_snapshot': snapshot_id,
            'deleted_snapshots': deleted_snapshots
        }
    }