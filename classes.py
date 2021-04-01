import boto3

class boto3_clients:

    def aws_client(self):
        return boto3.session.Session(profile_name='test-user')

    def lambda_client(self):
        return boto3.session.Session(profile_name='test-user').client('lambda')

    def s3_client(self):
        return boto3.session.Session(profile_name='test-user').client('s3')

    def iam_client(self):
        return boto3.session.Session(profile_name='test-user').client('iam')