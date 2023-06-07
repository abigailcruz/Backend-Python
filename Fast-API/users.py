from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn users:app --reload

#Definiendo entidad user 
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Jhojaira",  surname="Marquez", url="https://moure.dev", age=35),
              User(name="Celia",  surname="Cruz", url="https://mouredev.com", age=45),
              User(name="Abigail",  surname="Marquez", url="https://moure.dev", age=24)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Jhojaira", "surname": "jhoja", "url":"https://moure.dev", "age": 35},
            {"name": "Fatima", "surname": "jhoja", "url":"https://moure.dev", "age": 35},
            {"name": "Abigail", "surname": "jhoja", "url":"https://moure.dev", "age": 35}]

@app.get("/users")
async def userclass():
    return users_list