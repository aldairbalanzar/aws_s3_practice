from sqlite3 import connect
from venv import create
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv(override=True)
db_user = os.environ['DB_USER']
db_pw = os.environ['DB_PW']
db_name = os.environ['DB_NAME']

engine = create_engine(
    f'postgresql+psycopg2://{db_user}:{db_pw}@localhost/{db_name}',
    connect_args={},
    future=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()