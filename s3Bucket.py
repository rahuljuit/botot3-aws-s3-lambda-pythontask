import os
from classes import boto3_clients

obj3 = boto3_clients()
aws_console = obj3.aws_client()
s3_client = obj3.s3_client()



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


