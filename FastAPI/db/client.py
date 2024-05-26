## desde aca vamos a encargarnos de conectar nuestra base datos con MongoDB Atlas
from pymongo import MongoClient

# URL de la conexión a MongoDB
mongodb_url = "mongodb+srv://elias:HicsPB8Il7jgEJ1q@cluster10.voo1tde.mongodb.net/?retryWrites=true&w=majority&appName=Cluster10"

# Crea el cliente MongoDB y accedo a db_client
db_client = MongoClient(mongodb_url) 


""" 
## importaciones
from pymongo import MongoClient


db_client = MongoClient('mongodb+srv://elias:HicsPB8Il7jgEJ1q@cluster10.voo1tde.mongodb.net/?retryWrites=true&w=majority&appName=Cluster10')
##db_client = MongoClient().local ##dentro de estos parentesis voy a colocar la URL de donde estaría la base de datos en caso de que este alojada en otro sitio pero en este caso sera local y no se coloca nada
 """