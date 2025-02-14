from fastapi import FastAPI ##Importamos FastAPI
import uvicorn 
##from faker import Faker

## importacion de router para enrutar apis
from routers import products, users, basic_auth_user, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI() ##instanciar FastAPI
##fake = Faker()

""" for _ in range(2000):
    print(fake.name()) """
## aplico el router
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_user.router)
app.include_router(users_db.router)


app.mount("/static", StaticFiles(directory="frontend"), name="static")
# Para iniciar el front voy a esta dirección
##http://127.0.0.1:8000/static/index.html

@app.get("/") ## con GET obtengo en / a través del protocolo HTTP 
async def root(): ## uso async para que la aplicación no se detenga.
    return {"Hola": "Esto se encuentra en '/' de la aplicación"}

## En FastAPI puedo utilizar UVICORN para levantar el servidor.
## para esto ejecuto en la terminal $ uvicorn main:app --reload

@app.get("/url")
async def root():
    return {"Ahora esto": "esta en '/url' de la aplicación"}

#Documentacion con Swagger /docs
#Documentacion con Redocly /redoc


if __name__ == "__main__": ## con esto hago que se ejecute el servidor desde main 
    uvicorn.run(app, host="127.0.0.1", port=8000)
## También si ejecuto $ uvicorn main:app --reload por consola levanto el servidor
