import pymongo



class MongoLoad:
    def __init__(self,db):
        self.mongodb = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.mongodb[db]

    def create(self,collection_name):
        col = self.db[collection_name]
        print("creat good")
        return col

    def build(self,collection,soldier):
        document = soldier.get_dic_person()
        collection.insert_one(document)
        print("build good")

    def get_info(self,collection):
        return str(collection.find())

    def update(self,collection,id,update_field,update_value):
        new_value = {'$set': {update_field:update_value}}
        collection.update_one({'id':id},new_value)

    def delete(self,collection,id):
        collection.delete_one({'id':id})
        return

# a = MongoLoad("aaaa")
# c = a.create("aaaa")
# s= service.data_loader.soldier.Soldier("A" , "A" , "s" ,"D" )
#
# print(a.build(c , s))
