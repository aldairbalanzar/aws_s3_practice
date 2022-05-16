from ast import Name
from tempfile import NamedTemporaryFile
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
from utils.s3 import s3
from utils.security import validate_file_size, validate_file_type
from content_size_limit_asgi import ContentSizeLimitMiddleware
from database.db_config import engine
from database.models import User, Todo

User.Base.metadata.create_all(bind=engine)
Todo.Base.metadata.create_all(bind=engine)

app = FastAPI()
print('\t>>> API is runnning...')

@app.get('/')
def read_root():
    print('\t>>> getting "/" route...')
    return {"greeting": "waddup"}

@app.post('/add_photo')
def add_file(file: UploadFile):
    path = f'images/{file.filename}'
    bucket = s3.resource.Bucket(s3.aws_bucket)
    bucket.upload_fileobj(file.file, path, ExtraArgs={'ContentType': file.content_type})
    img_url = f'https://{s3.aws_bucket}.s3.amazonaws.com/images/{file.filename}'

    return {'message': 'file successfuly uploaded',
            'image_url': img_url}

@app.post('/add_multiple_photos')
async def add_files(files: List[UploadFile]):
    img_url_list = []
    for file in files:
        validate_file_type(file)
        
        path = f'images/{file.filename}'
        bucket = s3.resource.Bucket(s3.aws_bucket)
        bucket.upload_fileobj(file.file, path, ExtraArgs={'ContentType': file.content_type})

        img_url_list.append(f'https://{s3.aws_bucket}.s3.amazonaws.com/images/{file.filename}')

    return {'message': 'file(s) successfuly uploaded',
            'image_url': img_url_list}

app.add_middleware(ContentSizeLimitMiddleware, max_content_size=2_000_000)