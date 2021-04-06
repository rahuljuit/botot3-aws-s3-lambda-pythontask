from myClass import obj1

s3_client = obj1.s3_client
lambda_client = obj1.lambda_client


def create_lambda_function(bucket1, func_name, account_id, role_name):

    response = lambda_client.create_function(
        FunctionName=func_name,
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

def add_permission_to_lambda(func_name, account_id, bucket1):
    response = lambda_client.add_permission(
        Action='lambda:InvokeFunction',
        FunctionName=func_name,
        Principal='s3.amazonaws.com',
        SourceAccount=str(account_id),
        SourceArn='arn:aws:s3:::' + bucket1,
        StatementId='s3',
    )
    return response

# res5 = addPermissionToLambda('my-s3-lambda-func', 581131017022, 'tech-input-bucket')
# print(res5)
# print("Lambda functions Permission Added")


def bucket_configuration(loc, bucket1, account_id, func_name):
    response1 = s3_client.put_bucket_notification_configuration(
        Bucket=bucket1,
        NotificationConfiguration={
            'LambdaFunctionConfigurations': [
                {
                    'LambdaFunctionArn': 'arn:aws:lambda:' + loc + ':' + str(account_id) + ':function:' + func_name,
                    'Events': [
                        's3:ObjectCreated:Put'
                    ],
                },
            ]
        },
    )
    return response1
