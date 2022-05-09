from fastapi import File, UploadFile, HTTPException
from typing import List

def validate_file_size(files: List[UploadFile] = File(...)):
    limit=2_000_000
    file_size = 0
    for file in files:
        for chunk in file.file:
            file_size += len(chunk)
            if file_size > limit:
                print(f'\t>>> file {file.filename} is too big.')
                raise HTTPException(status_code=404, detail='file size too big.')
    
    return True