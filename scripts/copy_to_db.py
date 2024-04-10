import pandas as pd 
from sqlalchemy import create_engine, types
import os
from dotenv import load_dotenv
import datetime
import logging

log = logging.getLogger()
logging.basicConfig()
log.setLevel(logging.INFO)

load_dotenv()
user = os.getenv('USER')
pw = os.getenv('PW')
host = os.getenv('HOST')
port = os.getenv('PORT')
db = os.getenv('DB')
engine = create_engine(f'postgresql://{user}:{pw}@{host}:{port}/{db}')

class CopyToDb:
    def __init__(self, csv_file: str, dtype_schema: dict, table_name: str):
        self.csv_file = csv_file
        self.dtype_schema = dtype_schema
        self.table_name = table_name
    
    def write_data(self):
        data = pd.read_csv(self.csv_file)
        data.to_sql(
            name=self.table_name,
            con=engine,
            if_exists='replace',
            dtype=self.dtype_schema
        )
        log.info(f'Data written to {self.table_name} successfully at {datetime.datetime.now()}')


if __name__=='__main__':
    # Test
    courses_dtype_schema = {
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "module_presentation_length": types.VARCHAR
    }
    copyInstance = CopyToDb(
        'scripts/data/courses.csv',
        courses_dtype_schema,
        table_name='courses_test'
        )
    copyInstance.write_data()