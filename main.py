from tempfile import NamedTemporaryFile
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from utils.s3 import s3
from utils.security import validate_file_size, validate_file_type
from PIL import Image
from io import BytesIO

app = FastAPI()
print('\t>>> API is runnning...')

@app.get('/')
def read_root():
    print('\t>>> getting "/" route...')
    return {"greeting": "waddup"}

@app.post('/')
async def add_files(files: List[UploadFile] = File(...)):
    for file in files:
        data = await file.read()
        file_copy = NamedTemporaryFile(delete=False)

        file_copy.write(data)
        file_copy.seek(0)
        validate_file_type(file)
        validate_file_size(file_copy)

    print('\t>>> adding file(s)...')
    for file in files:
        data = await file.read()
        file_copy = NamedTemporaryFile(delete=False)

        file_copy.write(data)
        file_copy.seek(0)
        
        s3.resource.Bucket(s3.aws_bucket).put_object(Body=data, Key=f'images/{file.filename}',  ContentType=file.content_type)
        # s3.resource.Bucket(s3.aws_bucket).upload_file(file.filename, f'images/{file.filename}', ExtraArgs={'ContentType': file.content_type})


    return {'message': 'successfuly added files!'}
