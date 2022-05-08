import os
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv
from typing import IO
from fastapi import FastAPI, File, UploadFile, HTTPException
import boto3

app = FastAPI()

load_dotenv(override=True)
aws_access_key = os.environ['AWS_ACCESS_KEY']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
aws_bucket = os.environ['AWS_BUCKET']

session = boto3.Session(
aws_access_key,
aws_secret_access_key
)
resource = session.resource('s3')
client = session.client('s3')

print('\t>>> API is runnning...')

@app.get('/')
def read_root():
    print('\t>>> getting "/" route...')
    return {"Hello": "World"}

@app.post('/')
async def add_file(file: UploadFile = File(...)):
    limit=2_000_000
    file_size = 0
    temp: IO = NamedTemporaryFile(delete=False)
    for chunk in file.file:
        file_size += len(chunk)
        if file_size > limit:
            raise HTTPException(status_code=404, detail='file size too big')

    print('\t>>>adding file...')
    resource.Bucket(aws_bucket).put_object(Key=file.filename)
    return {'added_file': file.filename}