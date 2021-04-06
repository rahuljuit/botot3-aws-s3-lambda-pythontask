import json
from botocore.exceptions import ClientError
from myClass import obj1

s3_client = obj1.s3_client
iam_client = obj1.iam_client


trust_relationship_policy = {
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


def create_iam_role(bucket1, bucket2, role_name, policy_name):
    policy_json = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": ["s3:ListBucket"],
            "Resource": ["arn:aws:s3:::" + bucket1]
        }, {
            "Sid": "ReadFromBucket",
            "Effect": "Allow",
            "Action": "s3:Get*",
            "Resource": ["arn:aws:s3:::" + bucket1 + "/*"]
        }, {
            "Sid": "AllObjectActions",
            "Effect": "Allow",
            "Action": "s3:*Object",
            "Resource": ["arn:aws:s3:::" + bucket2 + "/*"]
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
    try:
        iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_relationship_policy),
            Description='Role for s3-lambda'
        )

        policy_res = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_json)
        )
        policy_arn = policy_res['Policy']['Arn']

        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
    except ClientError as error:
        if error.response['Error']['Code'] == 'EntityAlreadyExists':
            return 'Role already exists...  hence exiting from here'
        else:
            return 'Unexpected error occurred... Role could not be created ', error

    return 'Role {0} successfully got created with managed Policy {1}'.format(role_name, policy_name)


result = create_iam_role('tech-input-bucket', 'tech-output-bucket', 's3_lambda_access', 'S3LambdaReadWriteAccess')
print(result)
