import pymongo
import Soldier

class MongoLoad:
    def __init__(self,db):
        self.mongodb = pymongo.MongoClient("mongodb://mongodb:27017")
        self.db = self.mongodb[db]

    def create(self,collection_name):
        col = self.db[collection_name]
        return col

    def build(self,collection,id,first_name,last_name,rank,phone_number):
        soldier = Soldier(id,first_name,last_name,rank,phone_number)
        document = soldier.get_dic_person()
        collection.insert_one(document)


    def get_info(self,collection):
        return str(collection.find())

    def update(self,collection,id,update_field,update_value):
        new_value = {'$set': {update_field:update_value}}
        collection.update_one({'id':id},new_value)

    def delete(self,collection,id):
        collection.delete_one({'id':id})