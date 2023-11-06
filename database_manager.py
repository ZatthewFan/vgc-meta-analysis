import pymongo
import os
from dotenv import find_dotenv, load_dotenv
import sys


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
CONNECTION_STRING = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}.b3optnw.mongodb.net/?retryWrites=true&w=majority"

def get_database():
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client["vgc_teams"]

if __name__ == "__main__":
    db = get_database()