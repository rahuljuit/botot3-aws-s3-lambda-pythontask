import boto3


class Boto3Clients:

    def __init__(self):
        self.sessionn = boto3.session.Session(profile_name='test-user')
        self.lambda_client = self.sessionn.client('lambda')
        self.s3_client = self.sessionn.client('s3')
        self.iam_client = self.sessionn.client('iam')


obj1 = Boto3Clients()
