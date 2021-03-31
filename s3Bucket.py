import boto3
import os

aws_console = boto3.session.Session(profile_name="test-user")
s3_client = aws_console.client('s3')
lambda_client = aws_console.client('lambda')
iam_console = aws_console.client('iam')


def sources3bucket(bucket1, loc):

    response = s3_client.create_bucket(
        ACL='private',
        Bucket=bucket1,
        CreateBucketConfiguration={
             'LocationConstraint': loc
        }
    )

    return response


# creating destination bucket
def destinationS3Bucket(bucket2,loc):
    response = s3_client.create_bucket(
        ACL='private',
        Bucket=bucket2,
        CreateBucketConfiguration={
            'LocationConstraint': loc
        }
    )
    return response


def uploadZipFiles(bucket1):
    for file in os.listdir():
        if '.zip' in file:
            upload_to_bucket = bucket1
            upload_to_bucket_dir = str(file)
            s3_client.upload_file(file, upload_to_bucket, upload_to_bucket_dir)


# res2 = sources3bucket('tech-input-bucket', 'ap-south-1')
# print(res2)
# print("Source Bucket Created")
# res3 = destinationS3Bucket('tech-output-bucket', 'ap-south-1')
# print(res3)
# print("Destination Bucket Created")