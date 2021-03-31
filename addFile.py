import boto3

aws_console = boto3.session.Session(profile_name="test-user")
s3_client = aws_console.client('s3')
lambda_client = aws_console.client('lambda')
iam_console = aws_console.client('iam')

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