import pymongo
import os
from dotenv import find_dotenv, load_dotenv
import sys

class DatabaseManager:
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASS = os.getenv("MONGO_PASS")
    MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
    
    try:
        client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}.b3optnw.mongodb.net/?retryWrites=true&w=majority")
    except pymongo.errors.ConfigurationError:
        print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
        sys.exit(1)
    
    db = client.myDatabase