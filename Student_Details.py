from os import remove
import pymongo
from bson import ObjectId, decode
from pymongo.collection import ReturnDocument
#Connected Data Base
connection = pymongo.MongoClient('localhost',27017)
# Create Database
database = connection['StudentDetail']
# Create Collection
collection = database['StudentDetails']
print ("Database connected")

# insert data 
def inset_record(data):
    document = collection.insert_one(data)
    return document.inserted_id
data = {"name":"Yamuna Teja Kishore","id":"N1517888"}
id=inset_record(data)
print(id)
print("Sucessfully Inserted")

# retrive specific data usind Id 
def get_single_record(document_id):
    data = collection.find_one({'_id':ObjectId(document_id)})
    return data
document_id ='6110e88593475c5d7544bf71'
record = get_single_record(document_id)
print(record)
print("Sucessfully readed data")   

# update data
def update_create(document_id,data):
    document =  collection.update_one({'_id': ObjectId(document_id)},{"$set":data},upset=True)
    return document.acknowledged
def update_data(document_id,data):
    document = collection.update_one({'_id':ObjectId(document_id)},{"$set":data})
    return document.acknowledged
document_id="6110f2a86fa81ace0f60a9f2"
data = {'name':"Vemavarapu Yamuna Teja Kishore","id":"n1511"}
ack=update_data(document_id,data)
print(ack)
 
# retrive all record
def get_multiple_record():
    data = collection.find()
    return list(data)
record = get_multiple_record()
print(record)
print("Readed all the data")

# remove specific id
def remove_record(document_id):
    document=collection.delete_one({'_id':ObjectId(document_id)})
    return document.acknowledged
document_id="6110f2a86fa81ace0f60a9f2"
print(ack)




