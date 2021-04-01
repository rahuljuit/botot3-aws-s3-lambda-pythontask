
from classes import boto3_clients

obj2 = boto3_clients()
aws_console = obj2.aws_client()
s3_client = obj2.s3_client()
lambda_client = obj2.lambda_client()



def createLambdaFunction(bucket1, funcName, account_id, role_name):

    response = lambda_client.create_function(
        FunctionName=funcName,
        Runtime='python3.7',
        Role='arn:aws:iam::' + str(account_id) + ':role/' + role_name,
        Handler='lambda_function.lambda_handler',
        Code={
            'S3Bucket': bucket1,
            'S3Key': 'function.zip',

        }
    )
    return response


# res4 = createLambdaFunction('tech-input-bucket', 'my-s3-lambda-func', 581131017022, 'S3LambdaFullAccess3')
# print(res4)
# print("lambda Function Created")

def addPermissionToLambda( funcName, account_id, bucket1):
    response = lambda_client.add_permission(
        Action='lambda:InvokeFunction',
        FunctionName=funcName,
        Principal='s3.amazonaws.com',
        SourceAccount=str(account_id),
        SourceArn='arn:aws:s3:::' + bucket1,
        StatementId='s3',
    )
    return response

# res5 = addPermissionToLambda('my-s3-lambda-func', 581131017022, 'tech-input-bucket')
# print(res5)
# print("Lambda functions Permission Added")


def bucketConfiguration(loc, bucket1, account_id, funcName):
    response1 = s3_client.put_bucket_notification_configuration(
        Bucket=bucket1,
        NotificationConfiguration={
            'LambdaFunctionConfigurations': [
                {
                    'LambdaFunctionArn': 'arn:aws:lambda:' + loc + ':' + str(account_id) + ':function:' + funcName,
                    'Events': [
                        's3:ObjectCreated:Put'
                    ],
                },
            ]
        },
    )
    return response1


# res6 = bucketConfiguration('ap-south-1','tech-input-bucket' , 581131017022, 'my-s3-lambda-func')
# print(res6)
# print("Bucket Notification Configuration Added"