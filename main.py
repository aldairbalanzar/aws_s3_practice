from typing import List
from fastapi import FastAPI, File, UploadFile
from utils.s3 import s3
from utils.security import validate_file_size

app = FastAPI()
print('\t>>> API is runnning...')

@app.get('/')
def read_root():
    print('\t>>> getting "/" route...')
    return {"greeting": "waddup"}

@app.post('/')
async def add_file(files: List[UploadFile] = File(...)):
    if validate_file_size(files):
        print('\t>>>adding file(s)...')
        for file in files:
            s3.resource.Bucket(s3.aws_bucket).put_object(Key=f'images/{file.filename}')

    return {'message': 'file(s) have been uploaded.'}