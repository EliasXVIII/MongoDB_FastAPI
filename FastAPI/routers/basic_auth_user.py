from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

##Crear instancia de nuestro sistrema de auntenticación-
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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
        "password": "123"

    },
    "irene":{
        "username": "irene",
        "full_name": "Irene Gallego",
        "email": "irene@mail.com",
        "disabled": False,
        "password": "1234"
},
    "nicolas":{
        "username": "nicolas",
        "full_name": "Nicolas Pino",
        "email": "nicolas@mail.com",
        "disabled": False,
        "password": "12345"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
## Voy a crear un criterio de depencendia.
async def current_user(token : str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de auth invalidas", headers={"WWW-Authenticate":"Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user



@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta"
        )
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user