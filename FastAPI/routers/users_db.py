##Este lo conectaré con Mongo DB API

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
import uvicorn
from db.schemas.user import user_schema
from db.client import db_client ##En este paso vamos a importar de la carpeta "db"."client" la llamada db_client

router = APIRouter(prefix="/userdb", tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


users_list = []



## con esta funcion busco en users todos los resultados.
@router.get("/")
async def users():
    return users_list

@router.get("/{id}")##Con el {id} hago que filtre por ID
async def user(id: int):
    return search_user(id)

##Este ejemplo trabaja con query
@router.get("/")
async def user(id: int):
    return search_user(id)






#        if type(search_user(user.id))==User:
#           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
#       Como Accedo a la base de datos??? 
# declaro una variable y lo convierto a un json o diccionario y le paso el valor de user
## En esta linea esta el db_client (que esta en db_client = MongoClient() en el archivo /FastAPI/db/client.py) luego "local" viene de la base de datos y en lamlista de "users" y uso la opcion insert_one para ingresar 1 user o defino en mi funcion user
## Voy a hacer un POST
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    user_dict = dict(user) 
    del user_dict["id"]
    id = db_client.local.users.insert_one(user_dict).inserted_id   
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))
    return User(**new_user)
    




    
#implemento un PUT para actualizar o modificar datos.
@router.put("/")
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
@router.delete("/{id}")
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