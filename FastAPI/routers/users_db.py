

from fastapi import APIRouter, HTTPException, status ##API Router lo utilizo para crear un enrutador modular || HTTP HTTPException para manejar errores HTTP ya que las consultas seran a traves de HTTP y status para acceder a los códigos de estado HTTP.
from db.models.user import User ## Este en concreto lo importo de la carpeta db /models user.py
from db.schemas.user import user_schema, users_schema ##User es el modelo de datos de un usuario Y user_schema y users_schema son funciones para serializar y deserializar usuarios que he creado en MongoDB_FastAPI/FastAPI/db/schemas/user.py

from db.client import db_client  # db_client es el cliente de MongoDB que traigo de FastAPI/db/client.py
from bson import ObjectId #ObjectId es necesario para trabajar con IDs de MongoDB.

router = APIRouter(prefix="/userdb", tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})
# APIRouter es para crea un enrutador con el prefijo /userdb "tags" es para documentar el grupo de rutas bajo el nombre "userdb" y Responses es para personalizar un error en caso de que no encuentre algo que le pida





# Selecciona la base de datos y la colección
database = db_client['Cluster10']
users_collection = database['users']


##para formatear los json o los objetos a ObjectId de MongoDB utilizo lo siguiente
from bson import ObjectId

router = APIRouter(prefix="/userdb", tags=["userdb"], responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

"""
users_collection = db_client['mongodb+srv://elias:HicsPB8Il7jgEJ1q@cluster10.voo1tde.mongodb.net/?retryWrites=true&w=majority&appName=Cluster10']['users'] """


## con esta funcion busco en users todos los resultados.
@router.get("/", response_model=list[User]) ##Especifica que la respuesta será una lista de objeto
async def users():
    return users_schema(users_collection.find()) ##  Recupera todos los documentos en la colección y los convierte al esquema que le asignamos a users_schema
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
    if type(search_user("email", user.email)) == User: ## Esto es para que (field:str, key): ##criterio de busqueda (field) y la clave sean los valores por los que vana a buscar el user (field email y key el email del usuario)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe en nuestra base de datos! ")
    user_dict = dict(user) 
    del user_dict["id"]
    id = users_collection.insert_one(user_dict).inserted_id 
    #id = db_client.users.insert_one(user_dict).inserted_id 
    new_user = user_schema(users_collection.find_one({"_id": id}))  
    #new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user) ##que devuelva todos los campos de new_user en User
    



    
#implemento un PUT para actualizar o modificar datos.
@router.put("/", response_model=User)
async def user(user: User):## si quiero actualizar el usuario completo tengo que pasarle los datos del usuario "user" ==> "User"
    user_dict = dict(user)
    del user_dict["id"]

    try:
        users_collection.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)#En esta parte paso el Id y los cambios y pasa a ser un nuevo, user_dict como un ternario.
        #db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)

    except:
        return {"error":"no se ha actualizado el usuario"}    

    return search_user("_id", ObjectId(user.id)) ##le pasamos la instancia de user.id 
    

## Ahora voy a haer un DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = users_collection.find_one_and_delete({"_id": ObjectId(id)}) ## con esta linea busca en nuestra coleccion y busca 1 y lo elimina a traves del Objecto id
    #found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}







##Funcion para buscar usuarios.
""" def search_user_by_email(email: str):
    
    try:
       user = db_client.local.users.find_one({"email": email})
       return User(**user_schema(user))
    except: 
        return {"error": "User not found this is empty"}
     """



def search_user(field:str, key): ##criterio de busqueda (field) y la clave por la cual quiero buscar.
                        ## Como se ve key no esta definido su criterio de busqueda como str ya que puede ser un id o un ObjectId de MongoDB el que se coloque para su busqueda
    try:
       user = users_collection.find_one({field: key})
       #user = db_client.users.find_one({field: key})
       return User(**user_schema(user)) ## ** eso significa todos los campos
    except: 
        return {"error": "User not found this is empty"}
