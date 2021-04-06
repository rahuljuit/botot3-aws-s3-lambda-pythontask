from Final import IamRole
from Final import Lambda
from Final import s3Bucket
from Final import addFile
from myClass import obj1

s3_client = obj1.s3_client

role_name = 's3_lambda_access'
policy_name = 'S3ReadWriteAccess'
account_id = 581131017022
src_bucket = 'tech-input-bucket'
destination_bucket = 'tech-output-bucket'
region = 'ap-south-1'
function_name = 'my-s3-lambda-func'
file_name = 'test.txt'


res1 = s3Bucket.create_s3_bucket(src_bucket, region)
print(res1)
print("Source Bucket Created")

res2 = s3Bucket.create_s3_bucket(destination_bucket, region)
print(res2)
print("Destination Bucket Created")

res3 = IamRole.create_iam_role(src_bucket, destination_bucket, role_name, policy_name)
print(res3)
print("IAM Role Created!!")

waiter = s3_client.get_waiter('bucket_exists')
waiter.wait(Bucket=src_bucket)
s3Bucket.upload_zip_files(src_bucket)
print("Zip File Uploaded")


res4 = Lambda.create_lambda_function(src_bucket, function_name, account_id, role_name)
print(res4)
print("lambda Function Created")

# waiter = lambda_client.get_waiter('function_active')
# waiter.wait(FunctionName='my-s3-lambda-func')
res5 = Lambda.add_permission_to_lambda(function_name, account_id, src_bucket)
print(res5)
print("Lambda functions Permission Added")


res6 = Lambda.bucket_configuration(region, src_bucket, account_id, function_name)
print(res6)
print("Bucket Notification Configuration Added")


res7 = addFile.put_object_in_s3_bucket(file_name, src_bucket)
# print(res7)
print("Object added to the source bucket")
