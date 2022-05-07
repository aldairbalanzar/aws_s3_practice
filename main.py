import os
from dotenv import load_dotenv
from typing import Optional
from fastapi import FastAPI
import logging
import boto3
from botocore.exceptions import ClientError

# app = FastAPI()

load_dotenv(override=True)
aws_access_key = os.environ['AWS_ACCESS_KEY']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

session = boto3.Session(
aws_access_key,
aws_secret_access_key
)
s3 = session.resource('s3')
                     
for bucket in s3.buckets.all():
    print(f'name: {bucket.name}')

# @app.get("/")
# def read_root():
#     print('\t>>> getting "/" route...')
#     return {"Hello": "World"}

# print('\t>>> API is runnning...')

