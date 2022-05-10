import os
from dotenv import load_dotenv
import boto3

class S3:
    def __init__(self):
        load_dotenv(override=True)
        self.aws_access_key = os.environ['AWS_ACCESS_KEY']
        self.aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        self.aws_bucket = os.environ['AWS_BUCKET']
        self.session = boto3.Session(
            self.aws_access_key,
            self.aws_secret_access_key
        )
        self.resource = self.session.resource('s3')
        self.client = self.session.client('s3')
        print('\t>>> S3 is up.')

s3 = S3()
