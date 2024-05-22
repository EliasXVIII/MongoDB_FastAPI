

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client  # Importamos db_client desde el módulo client
from bson import ObjectId

router = APIRouter(prefix="/userdb", tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Selecciona la base de datos y la colección
database = db_client['Cluster10']
users_collection = database['users']

##Este lo conectaré con Mongo DB API
""" 
from fastapi import APIRouter, HTTPException, status
from db.models.user import User
import uvicorn
from db.schemas.user import user_schema, users_schema
from db.client import db_client ##En este paso vamos a importar de la carpeta "db"."client" la llamada db_client

##para formatear los json o los objetos a ObjectId de MongoDB utilizo lo siguiente
from bson import ObjectId

router = APIRouter(prefix="/userdb", tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

users_collection = db_client['mongodb+srv://elias:HicsPB8Il7jgEJ1q@cluster10.voo1tde.mongodb.net/?retryWrites=true&w=majority&appName=Cluster10']['users'] """


## con esta funcion busco en users todos los resultados.
@router.get("/", response_model=list[User])
async def users():
    return users_schema(users_collection.find())
    #return users_schema(db_client.users.find())

@router.get("/{id}")##Con el {id} hago que filtre por ID
async def user(id: str):
    return search_user("_id", ObjectId(id))

##Este ejemplo trabaja con query
@router.get("/")
async def user(id: str):
    return search_user("_id", ObjectId(id))






#        if type(search_user(user.id))==User:
#           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
#       Como Accedo a la base de datos??? 
# declaro una variable y lo convierto a un json o diccionario y le paso el valor de user
## En esta linea esta el db_client (que esta en db_client = MongoClient() en el archivo /FastAPI/db/client.py) luego "local" viene de la base de datos y en lamlista de "users" y uso la opcion insert_one para ingresar 1 user o defino en mi funcion user
## Voy a hacer un POST
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
    user_dict = dict(user) 
    del user_dict["id"]
    id = users_collection.insert_one(user_dict).inserted_id 
    #id = db_client.users.insert_one(user_dict).inserted_id 
    new_user = user_schema(users_collection.find_one({"_id": id}))  
    #new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)
    




    
#implemento un PUT para actualizar o modificar datos.
@router.put("/", response_model=User)
async def user(user: User):## si quiero actualizar el usuario completo tengo que pasarle los datos del usuario "user" ==> "User"
    user_dict = dict(user)
    del user_dict["id"]

    try:
        users_collection.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
        #db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)

    except:
        return {"error":"no se ha actualizado el usuario"}    

    return search_user("_id", ObjectId(user.id)) 
    

## Ahora voy a haer un DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = users_collection.find_one_and_delete({"_id": ObjectId(id)})
    #found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        return {"error": "No se elimina el usuario"}







##Funcion para buscar usuarios.
""" def search_user_by_email(email: str):
    
    try:
       user = db_client.local.users.find_one({"email": email})
       return User(**user_schema(user))
    except: 
        return {"error": "User not found this is empty"}
     """




def search_user(field:str, key):
    
    try:
       user = users_collection.find_one({field: key})
       #user = db_client.users.find_one({field: key})
       return User(**user_schema(user))
    except: 
        return {"error": "User not found this is empty"}


 
""" if __name__ == "__main__":
    uvicorn.run(router, host="127.0.0.1", port=8000) """