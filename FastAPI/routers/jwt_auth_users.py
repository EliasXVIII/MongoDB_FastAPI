from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta ## Para trabajar con calculos de fecha(timeedelta)

##El algoritmo que voy a utilizar es HS256
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

## para generar una palabra secreta tenemos el siguiente código que se ejecuta en consola $ openssl rand -hex 32
SECRET = "1c85b246abedd2998d7031d11da7a33fe7221830d81ec783ec3e98bd81e7e5ef"

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
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

## Intentar definir un nuevo criterio y encontrar el usuario autenticadoo
async def auth_user(token: str = Depends(oauth2)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de auth invalidas", headers={"WWW-Authenticate":"Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
    except JWTError:
        raise exception
    
    return search_user(username)


## Aca coloco el Current User
async def current_user(user : User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta"
        )
    access_token = {"sub":user.username, "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"} ##access_token



##Tengo la operacion para traer mis datos

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user