from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta ## Para trabajar con calculos de fecha

##El algoritmo que voy a utilizar es HS256
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel): ##El Base Model nos crea una entidad User
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "elias":{
        "username": "elias",
        "full_name": "Elias Riquelme",
        "email": "elias@mail.com",
        "disabled": False,
        "password": "$2a$12$MTXhnddl46ZD1avjqGMU1OFIIgQrTFHJSGihZfAQ3KOmrTxKuY8Uu" ### antes era =>"123" generada con https://bcrypt-generator.com/

    },
    "irene":{
        "username": "irene",
        "full_name": "Irene Gallego",
        "email": "irene@mail.com",
        "disabled": False,
        "password": "$2a$12$iZezgKErJ47Y7VSxEcjRhek43DBAIR9yOsODdorvnFxYLsLLuaNUq" ## antes era "1234"
},
    "nicolas":{
        "username": "nicolas",
        "full_name": "Nicolas Pino",
        "email": "nicolas@mail.com",
        "disabled": False,
        "password": "$2a$12$nlwPO0WKzwdsg9nXR1ds1eXzshso.X9GwnPJ.PqSw9S1lsuZ3qX8S" ##"12345"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta"
        )
    


    return {"access_token": user.username, "token_type": "bearer"}