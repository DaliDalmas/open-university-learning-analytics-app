from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('USER')
pw = os.getenv('PW')
host = os.getenv('HOST')
port = os.getenv('PORT')
db = os.getenv('DB')
engine = create_engine(f'postgresql://{user}:{pw}@{host}:{port}/{db}')

sessionLocal1 = sessionmaker(autocommit=True, autoflush=True, bind=engine)

Base = declarative_base()