from fastapi import APIRouter, HTTPException
import uvicorn
from pydantic import BaseModel

router = APIRouter()

##voy a definir una entidad USER
class User(BaseModel): ##El Base Model nos crea una entidad User
    id : int
    name: str
    surname: str
    age: int

users_list = [User(id=1 ,name="Elias",surname="Riquelme", age=36),
              User(id=2 ,name="Irene", surname="Gallego", age=29),
              User(id=3 ,name="Nicolas", surname="Pino", age=33)]

""" @app.get("/usersjson")
async def users():
    return [{"name": "Elias","surname":"Riquelme","age":36},{"name":"Irene","surname":"Gallego","age":29}] """

## con esta funcion busco en users todos los resultados.
@router.get("/users/")
async def users():
    return users_list

@router.get("/user/{id}")##Con el {id} hago que filtre por ID
async def user(id: int):
    return search_user(id)

##Este ejemplo trabaja con query
@router.get("/user/")
async def user(id: int):
    return search_user(id)



## Voy a hacer un POST
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id))==User:
        raise HTTPException(status_code=204, detail="User already exists")
        """ return {"error": "User already exists"} """ ## ya no me sirve por que aplico HTTPException
    else:
        users_list.append(user)
        return user
    
#implemento un PUT para actualizar o modificar datos.
@router.put("/user/")
async def user(user: User):## si quiero actualizar el usuario completo tengo que pasarle los datos del usuario "user" ==> "User"
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se actualiza el usuario"}
    else:
        return user
    

## Ahora voy a haer un DELETE
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error": "No se elimina el usuario"}
    else:
        return {"message": "Usuario eliminado"}







##Funcion para buscar usuarios.
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except: 
        return {"error": "User not found this is empty"}

 
if __name__ == "__main__":
    uvicorn.run(router, host="127.0.0.1", port=8000)