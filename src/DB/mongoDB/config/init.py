import os


def check_mongo_is_running():
    url_mongo = os.environ.get("MONGODB_PROCESO")
    print(url_mongo)
