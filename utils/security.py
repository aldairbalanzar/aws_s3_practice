from fastapi import File, UploadFile, HTTPException

def validate_file_size(file: UploadFile = File(...)):
    limit=2_000_000
    file_size = 0
    for chunk in file:
        file_size += len(chunk)
        if file_size > limit:
            print(f'\t>>> file {file.filename} is too big.')
            raise HTTPException(status_code=404, detail='file size too big.')

    return True

def validate_file_type(file: UploadFile = File(...)):
    print(f'type: {file.content_type}')
    if file.content_type == 'image/png' or file.content_type == 'image/jpeg':
        return True

    print(f'\t>>> file {file.filename} is of wrong type.')
    raise HTTPException(status_code=404, detail='file is of wrong type.')
