import psycopg2
from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASS = os.getenv("POSTGRES_PASS")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

conn = None
cur = None

try:
    conn = psycopg2.connect(
        database = POSTGRES_DB,
        host = POSTGRES_HOST,
        user = POSTGRES_USER,
        password = POSTGRES_PASS,
        port = POSTGRES_PORT)
    
    cur = conn.cursor()
    
    # create_script = ''' CREATE TABLE pokemon (
    #                         id          int PRIMARY KEY
    # )
    # '''
    
except Exception as error:
    print(error)
finally:
    if cur is not None: cur.close()
    if conn is not None: conn.close()