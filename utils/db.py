from pymongo import MongoClient
from config.settings import MONGODB_URI, MONGODB_DB

__client = None


def get_client():
    global __client

    if not MONGODB_URI:
        return None

    if __client is None:
        __client = MongoClient(MONGODB_URI)


def get_db():
    client = get_client()
    if client is None:
        return None
    return client[MONGODB_DB]
