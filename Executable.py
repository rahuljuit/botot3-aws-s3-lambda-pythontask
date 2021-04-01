
from Final import IamRole
from Final import Lambda
from Final import s3Bucket
from Final import addFile
from classes import boto3_clients

obj5 = boto3_clients()
s3_client = obj5.s3_client()

role_name = 'S3LambdaFullAccess5'
account_id = 581131017022
src_bucket = 'tech-input-bucket'
dest_bucket = 'tech-output-bucket'
region = 'ap-south-1'
function_name = 'my-s3-lambda-func'
file_name = 'test.txt'


res1 = IamRole.iamrolecreate(role_name, account_id)
print(res1)
print("IAM Role Created!!")

res2 = s3Bucket.sources3bucket(src_bucket, region)
print(res2)
print("Source Bucket Created")
res3 = s3Bucket.destinationS3Bucket(dest_bucket, region)
print(res3)
print("Destination Bucket Created")

waiter = s3_client.get_waiter('bucket_exists')
waiter.wait(Bucket=src_bucket)
s3Bucket.uploadZipFiles(src_bucket)
print("Zip File Uploaded")


res4 = Lambda.createLambdaFunction(src_bucket, function_name, account_id, role_name)
print(res4)
print("lambda Function Created")

# waiter = lambda_client.get_waiter('function_active')
# waiter.wait(FunctionName='my-s3-lambda-func')
res5 = Lambda.addPermissionToLambda(function_name, account_id, src_bucket)
print(res5)
print("Lambda functions Permission Added")


res6 = Lambda.bucketConfiguration(region, src_bucket, account_id, function_name)
print(res6)
print("Bucket Notification Configuration Added")


res7 = addFile.putObjectInS3Bucket(file_name, src_bucket)
# print(res7)
print("Object added to the source bucket")