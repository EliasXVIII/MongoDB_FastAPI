from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

##voy a definir una entidad USER
class User(BaseModel): ##El Base Model nos crea una entidad User
    id : int
    name: str
    surname: str
    age: int

users_list = [User(id=1 ,name="Elias",surname="Riquelme", age=36),
              User(id=2 ,name="Irene", surname="Gallego", age=29),
              User(id=2 ,name="Nicolas", surname="Pino", age=33)]

""" @app.get("/usersjson")
async def users():
    return [{"name": "Elias","surname":"Riquelme","age":36},{"name":"Irene","surname":"Gallego","age":29}] """

""" @app.get("/users")
async def users():
    return users_list """

@app.get("/user/{id}")##Con el {id} hago que filtre por ID
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except: 
        return {"error": "User not found this is empty"}







if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)