from classes import boto3_clients

obj4 = boto3_clients()

aws_console = obj4.aws_client()
s3_client = obj4.s3_client()


def putObjectInS3Bucket(filename, bucket1):
    f = open(filename, "r")
    data = f.read()
    print(data)

    response3 = s3_client.put_object(
        ACL='private',
        Body=data,
        Bucket=bucket1,
        Key=filename,
    )
    return response3


# res7 = putObjectInS3Bucket('test.txt', 'tech-input-bucket')
# print(res7)
# print("Object added to the source bucket")