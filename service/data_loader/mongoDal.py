import pymongo

class MongoLoad:
    def __init__(self,db):
        self.mongodb = pymongo.MongoClient("mongodb://mongodb:27017")
        self.db = self.mongodb[db]

    def create(self,collection_name):
        col = self.db[collection_name]
        print("collection created")
        return col

    def build(self,collection,soldier):
        document = soldier.get_dict_person()
        collection.insert_one(document)
        print("document built")

    def get_info(self,collection):
        info = ''
        for doc in collection.find():
            info + str(doc)
        return info

    def update(self,collection,id,update_field,update_value):
        new_value = {'$set': {update_field:update_value}}
        collection.update_one({'id':id},new_value)

    def delete(self,collection,id):
        collection.delete_one({'id':id})
        return

