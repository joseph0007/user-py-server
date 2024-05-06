from fastapi import FastAPI
from routers import users_routes

app = FastAPI()

app.include_router(users_routes.router)

@app.get("/")
async def root():
  return {
    "message": "Hello World"
  }

@app.get("*")
async def root():
  return {
    "status": True,
    "message": "You seem to be lost.",
  }
  
  