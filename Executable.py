import boto3
from Final import IamRole
from Final import Lambda
from Final import s3Bucket
from Final import addFile

aws_console = boto3.session.Session(profile_name="test-user")
s3_client = aws_console.client('s3')
lambda_client = aws_console.client('lambda')
iam_console = aws_console.client('iam')

# res1 = IamRole.iamrolecreate('S3LambdaFullAccess3', 581131017022)
# print(res1)
# print("IAM Role Created!!")
#
res2 = s3Bucket.sources3bucket('tech-input-bucket', 'ap-south-1')
print(res2)
print("Source Bucket Created")
# res3 = s3Bucket.destinationS3Bucket('tech-output-bucket', 'ap-south-1')
# print(res3)
# print("Destination Bucket Created")

waiter = s3_client.get_waiter('bucket_exists')
waiter.wait(Bucket='tech-input-bucket')
s3Bucket.uploadZipFiles('tech-input-bucket')
print("Zip File Uploaded")


res4 = Lambda.createLambdaFunction('tech-input-bucket', 'my-s3-lambda-func', 581131017022, 'S3LambdaFullAccess3')
print(res4)
print("lambda Function Created")

# waiter = lambda_client.get_waiter('function_active')
# waiter.wait(FunctionName='my-s3-lambda-func')
res5 = Lambda.addPermissionToLambda('my-s3-lambda-func', 581131017022, 'tech-input-bucket')
print(res5)
print("Lambda functions Permission Added")


res6 = Lambda.bucketConfiguration('ap-south-1', 'tech-input-bucket', 581131017022, 'my-s3-lambda-func')
print(res6)
print("Bucket Notification Configuration Added")



res7 = addFile.putObjectInS3Bucket('test.txt', 'tech-input-bucket')
print(res7)
print("Object added to the source bucket")