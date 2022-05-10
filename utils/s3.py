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
<<<<<<< HEAD
        print('\t>>> S3 is up.')
=======
        print('\t>>> S3 is running...')
>>>>>>> ff1a6a5e5fa48ba738798a7db42f7673576b67ce

s3 = S3()