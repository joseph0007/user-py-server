import pymongo
from utils.util_funtions import (
  parse_json
)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythondb"]

def insertOne( collectionName: str, data: dict ):
  collection = mydb[collectionName]
  
  if data is None:
    return "No data is provided to insert"
  
  if type(data) is not dict:
    return "Please provide a dict to insert"
  
  return collection.insert_one(data)

  
def updateOne( collectionName: str, filter: dict, data: dict ):
  collection = mydb[collectionName]
  
  if data is None:
    return "No data is provided to insert"
  
  if filter is None:
    filter = dict()
  
  return collection.update_one(filter, { "$set": dict(data) })
  
  
def deleteOne( collectionName: str, filter: dict ):
  collection = mydb[collectionName]
  
  if filter is None:
    filter = dict()
  
  return collection.delete_one(filter)
  
def findOne( collectionName: str, filter: dict ):
  collection = mydb[collectionName]
  
  if filter is None:
    filter = dict()
  
  res = parse_json(collection.find_one(filter))
  
  if res is not None:
    res["_id"] = res["_id"]["$oid"]
    
  return res
  
def findAll( collectionName: str, filter: dict ):
  collection = mydb[collectionName]
  
  if filter is None:
    filter = dict()
  
  res = parse_json(collection.find(filter))
  
  if res is not None:
    for doc in res:
      doc["_id"] = doc["_id"]["$oid"]
  
  return res