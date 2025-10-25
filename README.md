# Serverless-Architecture

### Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
- #### Step 1: Setup EC2 Instances & Tags
    - ##### Go to EC2 Console → Instances → Launch instances.
    ![alt text](image.png)
    ![alt text](image-1.png)
    ![alt text](image-2.png)

    - #### After they’re running, select each one → Tags → Manage tags:
    ![alt text](image-3.png)
    ![alt text](image-4.png)
    ![alt text](image-5.png)
    ![alt text](image-6.png)

- #### Step 2: Create the Lambda Function
    - ##### Go to AWS Lambda Console → Create function
        - ###### Choose:
            - 1.	Author from scratch
            - 2.	Function name: EC2AutoManager
            - 3.	Runtime: Python 3.9+
            - 4.	Execution role: “Create a new role with basic Lambda permissions”
    ![alt text](image-7.png)
    ![alt text](image-8.png)

- #### Step 3: Add IAM Permissions to the Role
    - ##### Go to IAM Console → Roles → Find your Lambda’s role
        - Attach the following managed policy: AmazonEC2FullAccess
    ![alt text](image-9.png)
    ![alt text](image-10.png)

- #### Step 4: Write the Lambda Function Code
    - Refer Assignment1.py for the Lambda code.

- #### Step 5: Test the Lambda Function
            - 1.	In the Lambda console → Test tab.
            - 2.	Configure a test event (any JSON; the event isn’t used, e.g. {}).
            - 3.	Click Test.

            - Expected behavior:
                •	The EC2 instance tagged Auto-Stop=True stops.
                •	The EC2 instance tagged Auto-Start=True starts.
    
    ![alt text](image-11.png)
    ![alt text](image-12.png)
    ![alt text](image-13.png)
    ![alt text](image-14.png)
    ![alt text](image-15.png)

### Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
- #### Step 1: Create the S3 Bucket and Upload Files
    - ##### Go to the S3 Console
    - ##### Click Create bucket
    ![alt text](image-16.png)
    ![alt text](image-17.png)
    ![alt text](image-18.png)
    - ##### Upload some files
        - A few recent files (today’s date)
        - A few older files
    ![alt text](image-19.png)
    ![alt text](image-20.png)
    ![alt text](image-29.png)

- #### Step 2: Create IAM Role for Lambda
    - 1 Go to IAM → Roles → Create role
    ![alt text](image-21.png)
    - 2 Choose:
        - Trusted entity type: AWS service
        - Use case: Lambda
    ![alt text](image-22.png)
    - 3 Attach the managed policy:
        - AmazonS3FullAccess
    ![alt text](image-23.png)
    - 4 Name the role: S3CleanupLambdaRole
    - 5 Click Create role
    ![alt text](image-24.png)

- #### Step 3: Create the Lambda Function
    - 1 Go to AWS Lambda Console → Create function
    - 2 Choose:
        - Author from scratch
        - Function name: S3CleanupFunction
    - 3 Runtime: Python 3.9+
    - 4 Execution role: Use existing role → select S3CleanupLambdaRole
    - 5 Click Create function
    ![alt text](image-26.png)

- #### Step 4: Write the Lambda Code
    - Refer Assignment2.py for the Lambda code

- #### Step 5: Test the Lambda Function
    - 1 Click Deploy
    - 2 Go to the Test tab
    - 3 Create a test event (just {} — no input needed)
    - 4 Click Test
    ![alt text](image-27.png)

    - ##### Expected Behavior:
        - 1 Lambda logs show files being deleted if they’re older than 30 days.
        - 2 Files newer than 30 days remain.
        - 3 We can verify in the S3 console — refresh the bucket to see the result.
        ![alt text](image-28.png)

    ### Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
    - #### Step 1: S3 Bucket Setup
        - Go to S3 Dashboard > Create Bucket.
        - Create 3 buckets:
            - Enable default encryption on some.
            - Leave encryption disabled on others.
        ![alt text](image-30.png)
    
    - #### Step 2: IAM Role for Lambda
        - Go to IAM > Roles > Create Role.
        - Choose Lambda as the trusted entity.
        - Attach the following policies:
            - AmazonS3ReadOnlyAccess (to list buckets and get encryption settings)
            - AWSLambdaBasicExecutionRole (for CloudWatch logging)
        - Name the role something like LambdaS3EncryptionMonitor.
        ![alt text](image-31.png)

    - #### Step 3: Lambda Function Setup
        - Go to Lambda > Create Function.
        - Runtime: Python 3.12
        - Execution role: Use LambdaS3EncryptionMonitor
        - Name it UnencryptedBucketDetector
        ![alt text](image-32.png)

    - #### Step 4: Lambda Function Code (Python + Boto3)
        - Refer Assignment3.py

    - #### Step 5: Manual Invocation & Verification
        - In the Lambda console, click Test.
        - Create a test event (default JSON is fine).
        - Click Test again to invoke.
        - Go to CloudWatch Logs:
            - Look for /aws/lambda/UnencryptedBucketDetector
        - Check the log stream
        ![alt text](image-33.png)

    ### Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3
    - #### Step 1: EBS Volume Setup
        - Go to EC2 Dashboard > Elastic Block Store > Volumes.
        - Either:
            - Use an existing volume, or
            - Create a new one and attach it to an EC2 instance.
        - Note down the Volume ID (vol-0787bd263dd1e5a05).
        ![alt text](image-34.png)

    - #### Step 2: IAM Role for Lambda
        - Go to IAM > Roles > Create Role.
        - Choose Lambda as the trusted entity.
        - Attach the following policies:
            - AmazonEC2FullAccess
            - AWSLambdaBasicExecutionRole
        - Name the role something like LambdaEBSSnapshotManager.
        ![alt text](image-35.png)

    - ### Step 3: Lambda Function Setup
        - Go to Lambda > Create Function.
        - Runtime: Python 3.12
        - Execution role: Use LambdaEBSSnapshotManager
        - Name it EBSBackupCleanup
        ![alt text](image-36.png)

    - ### Step 4: Lambda Function Code (Python + Boto3)
        - Refer Assignment4.py
    
    - ### Step 5: Manual Invocation & Verification
        - In Lambda console, click Test.
        - Create a test event.
        - Click Test again to invoke.
        - Go to EC2 > Snapshots:
            - Confirm a new snapshot was created.
        ![alt text](image-37.png)
        ![alt text](image-38.png)







