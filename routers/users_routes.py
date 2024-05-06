from fastapi import APIRouter, Response, status
from utils.schemas import User
from models.users_model import (
  userCreate,
  fetchUser,
  fetchAllUser,
  deleteUser,
  updateUser,
)

router = APIRouter(
  prefix="/api/users",
  tags=["users"],
  responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=200)
async def root(user: User, response: Response):
  
  try:
    userDict = userCreate(user)
  except Exception as error:
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {
      "status": False,
      "message": error.__str__(),
      "data": dict()
    }

  response.status_code = status.HTTP_201_CREATED
  return {
    "status": True,
    "message": "user created successfully",
    "data": userDict
  }

@router.get("/{userId}")
async def root(userId: str):
  userData = fetchUser(userId)
  
  if userData is None:
    return {
      "status": False,
      "message": "User not found",
      "data": dict()
    }
  
  return {
    "status": True,
    "message": "User found",
    "data": userData
  } 
  
@router.get("/")
async def root():
  userData = fetchAllUser()
  
  if userData is None:
    return {
      "status": False,
      "message": "User not found",
      "data": dict()
    }
    
  return {
    "status": True,
    "message": "All user data retrieved",
    "data": userData
  } 
  
@router.delete("/{userId}")
async def root(userId: str):
  userDeleteData = deleteUser(userId)
  
  if userDeleteData is False:
    return {
      "status": False,
      "message": "User not found",
      "data": dict()
    }
    
  return {
    "status": True,
    "message": "User delete successfully"
  } 

@router.patch("/{userId}")
async def root(userId: str, user: User):
  userData = updateUser(userId, user)
  
  if userData is None:
    return {
      "status": False,
      "message": "User not found",
      "data": dict()
    }
    
  return {
    "status": True,
    "message": "User updated successfully",
    "data": userData
  }
