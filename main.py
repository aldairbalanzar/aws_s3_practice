from ast import Name
from tempfile import NamedTemporaryFile
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from utils.s3 import s3
from utils.security import validate_file_size, validate_file_type
from PIL import Image
from io import BytesIO
import os
import boto3

app = FastAPI()
print('\t>>> API is runnning...')

@app.get('/')
def read_root():
    print('\t>>> getting "/" route...')
    return {"greeting": "waddup"}

@app.post('/photo')
def add_file(file: UploadFile):
    s3.resource.Bucket(s3.aws_bucket).upload_fileobj(file.file,
                                                    f'images/{file.filename}',
                                                    ExtraArgs={'ContentType': file.content_type})
    img_url = f'https://{s3.aws_bucket}.s3.amazonaws.com/images/{file.filename}'

    return {
            'message': 'file successfuly uploaded',
            'image_url': img_url
            }

# @app.post('/')
# async def add_files(files: List[UploadFile] = File(...)):

    # for file in files:
        # data = await file.read()
        # file_copy = BytesIO()
        # with file_copy as f:
        #     f.write(data)
        #     f.seek(0)
        #     validate_file_type(file)
        #     validate_file_size(f)
        #     print(f'bytes: {f.getbuffer().nbytes}')
        #     f.seek(0)
        #     print('\t>>> adding file(s)...')
        # s3.resource.Bucket(s3.aws_bucket).put_object(Body=f, Key=f'images/{file.filename}', ContentType=file.content_type)

        # data = await file.read()
        # file_copy = BytesIO()

        # with file_copy as f:
        #     f.write(data)
        #     f.seek(0)
        #     validate_file_type(file)
        #     validate_file_size(f)
        #     print(f'bytes: {f.getbuffer().nbytes}')
        #     f.seek(0)
        #     print('\t>>> adding file(s)...')
        #     s3.client.put_object(Body=f, Bucket=s3.aws_bucket, Key=f'images/{file.filename}', ContentType=file.content_type)


    # for file in files:
        #method 1
        # data = await file.read()
        # temp_file = BytesIO()
        # temp_file.write(data)
        # temp_file.seek(0)
        # s3.client.upload_fileobj(temp_file, s3.aws_bucket, f'images/{file.filename}', ExtraArgs={'ContentType': file.content_type})
        # temp_file.close()
        
        #method 2
        # data = await file.read()
        # temp_file = NamedTemporaryFile(delete=False)
        # try:
        #     temp_file.write(data)
        #     temp_file.seek(0)
        #     s3.client.upload_fileobj(temp_file, s3.aws_bucket, f'images/{file.filename}', ExtraArgs={'ContentType': file.content_type})
        
        # finally:
        #     temp_file.close()
        #     os.unlink(temp_file.name)

        #method 3
        # data = await file.read()
        # temp_file = NamedTemporaryFile('wb', delete=False)
        # f = None
        # try:
        #     with temp_file as f:
        #         f.write(data)

        #     f = open(temp_file.name, 'rb')
        #     s3.client.upload_fileobj(f, s3.aws_bucket, f'images/{file.filename}', ExtraArgs={'ContentType': file.content_type})

        # finally:
        #     if f is not None:
        #         f.close()
        #     os.unlink(temp_file.name)

        #method 4
        # data = await file.read()
        # temp_file = BytesIO()
        # temp_file.write(data)
        # temp_file.seek(0)
        # s3.client.put_object(Bucket=s3.aws_bucket, Body=data, Key=f'images/{file.filename}', ContentType=file.content_type)

    # return {'message': 'successfuly added files!'}
