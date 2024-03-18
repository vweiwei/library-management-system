import pymongo
from Utils.configGetter import settings

class MongoConnection:

    def __init__(self, database=None, collection=None):
        self.client = pymongo.MongoClient(settings.mongo_uri)
        self.db = self.client[settings.mongodb_name]
        # if database is not None:
        #     db = self.client[database]
        # else:
        #     db = self.client[settings.mongodb_name]
        # if collection is not None:
        #     self.collect = db[collection]
        # else:
        #     self.collect = db[settings.collection]

    # def __init__(self):
    #     # self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    #     self.client = pymongo.MongoClient('mongodb://root:123456@localhost:27017')
    #     self.db = self.client["ClassroomManager"]
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(MongoConnection, "_instance"):
    #         with MongoConnection._instance_lock:
    #             if not hasattr(MongoConnection, "_instance"):
    #                 MongoConnection._instance = object.__new__(cls)
    #     return MongoConnection._instance





