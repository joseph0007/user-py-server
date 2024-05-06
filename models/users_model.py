from bson import ObjectId
from utils.schemas import User
from databases.mongo import (
  insertOne,
  findOne,
  findAll,
  deleteOne,
  updateOne
)

collectionName = "users_py"

def userCreate(user: User):
  checkData = findOne(collectionName, { "email": user.email })
  
  if checkData is not None:
    raise Exception("User already exists with same email")
  
  dictUserData = dict(user)
  res = insertOne(collectionName, dictUserData)
  userData = findOne(collectionName, { "_id": ObjectId(res.inserted_id) })
  
  return userData

def fetchUser(userId: str):
  userData = findOne(collectionName, { "_id": ObjectId(userId) })
  return userData
  
def fetchAllUser():
  userData = findAll(collectionName, {})
  return userData
  
def deleteUser(userId: str):
  deleteOne(collectionName, { "_id": ObjectId(userId) })
  return True

def updateUser(userId: str, user: User):
  updateOne(collectionName, { "_id": ObjectId(userId) }, user)
  userData = findOne(collectionName, { "_id": ObjectId(userId) })
  return userData