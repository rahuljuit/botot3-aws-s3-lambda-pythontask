import boto3
import os
import json
from botocore.exceptions import ClientError

aws_console = boto3.session.Session(profile_name="test-user")
s3_client = aws_console.client('s3')
lambda_client = aws_console.client('lambda')
iam_console = aws_console.client('iam')

trust_relationship_policy_another_aws_service = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

def iamrolecreate(role_name, account_id):
    try:
        create_role_res = iam_console.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_relationship_policy_another_aws_service),
            Description='This is a test role',
            Tags=[
                {
                    'Key': 'Rahul',
                    'Value': 'CreateRole'
                }
            ]
        )
    except ClientError as error:
        if error.response['Error']['Code'] == 'EntityAlreadyExists':
            return 'Role already exists... hence exiting from here'
        else:
            return 'Unexpected error occurred... Role could not be created', error

    policy_json = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": "*"
        },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "*"
            }]
    }

    policy_name = role_name + '_policy'
    policy_arn = ''

    try:
        policy_res = iam_console.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_json)
        )
        policy_arn = policy_res['Policy']['Arn']
    except ClientError as error:

        if error.response['Error']['Code'] == 'EntityAlreadyExists':

            print('Policy already exists... hence using the same policy')
            policy_arn = 'arn:aws:iam::' + str(account_id) + ':policy/' + policy_name
        else:

            print('Unexpected error occurred... hence cleaning up', error)
            iam_console.delete_role(
                RoleName=role_name
            )
            return 'Role could not be created...', error

    try:
        policy_attach_res = iam_console.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
    except ClientError as error:
        print('Unexpected error occurred... hence cleaning up')
        iam_console.delete_role(
            RoleName=role_name
        )
        return 'Role could not be created...', error

    return 'Role {0} successfully got created'.format(role_name)



# res1 = iamrolecreate('S3LambdaFullAccess3', 581131017022)
# print(res1)
# print("IAM Role Created!!")