from pymongo.database import Database

from config import USER, PASSWORD
import pymongo


class MongoConnect:
    def __init__(self):
        self.user = USER
        self.password = PASSWORD

    def get_db(self, db_name: str):
        url = f'mongodb+srv://{self.user}:{self.password}' \
              f'@cluster1.ss7fmb4.mongodb.net/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(url)
        db = client[db_name]
        return db

    def create_collection(self, db: Database, coll_name: str):
        return db[coll_name]

    def insert_one(self, coll, data: dict):
        return coll.insert_one(data).inserted_id

    def delete_one(self, coll, query: dict):
        return coll.delete_one(query)

    def find_one(self, found, data: dict):
        return found.find_one(data)

    def drop_coll(self, coll):
        return coll.drop()


class Storage(MongoConnect):
    pass
