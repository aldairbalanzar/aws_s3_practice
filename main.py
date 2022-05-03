from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print('\t>>> getting "/" route...')
    return {"Hello": "World"}

print('\t>>> API is runnning...')