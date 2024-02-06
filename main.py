from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

# Fetch database connection details from environment variables
db_path = os.getenv('SQLITE_DB_PATH')

engine = create_engine(f'sqlite:///{db_path}')

def run_query(sql_text):
    output = ""
    with engine.connect() as connection:
        try:
            result = connection.execute(text(sql_text))
        except Exception as e:
            result = "An exception occurred: " + str(e)
    for row in result:
        output += str(row)
    return output
