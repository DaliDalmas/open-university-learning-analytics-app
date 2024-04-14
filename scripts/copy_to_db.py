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

'''
explanation of this code by chatgpt
------------------------------------
This code is about importing CSV data into a PostgreSQL database using pandas and SQLAlchemy. Here's what it does:

It imports necessary libraries: pandas for handling data, SQLAlchemy for working with databases,
os for handling file paths and environment variables, dotenv for loading environment variables from a .env file,
datetime for handling date and time, and logging for logging messages.

It sets up logging to provide information about the process.

It loads environment variables from a .env file, which typically contains sensitive information like database 
credentials and connection details.

It creates an engine using SQLAlchemy, which represents the interface to the database. 
This engine is created with the PostgreSQL database URL constructed from the environment variables.

It defines a class called CopyToDb. This class is designed to handle the copying of data 
from a CSV file into a database table.

The __init__ method initializes instances of CopyToDb with parameters including the path to the CSV file (csv_file), 
a dictionary defining the data types of each column (dtype_schema), and the name of the database table (table_name) where the data will be inserted.

The write_data method reads the data from the CSV file using pandas, then writes it to the specified database 
table using the to_sql method. It specifies the table name, the database connection (engine), the action to take 
if the table already exists (if_exists='replace'), and the data types of the columns.

After writing the data, it logs a message confirming the successful writing of data to the database table, 
including the table name and the current date and time.

Overall, this code provides a flexible and efficient way to import data from CSV files into a PostgreSQL database 
table with appropriate data types and logging for monitoring the process.
'''

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
        log.info(
            f'Data written to {self.table_name} successfully at {datetime.datetime.now()}'
            )


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