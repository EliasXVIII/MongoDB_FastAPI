from fastapi import FastAPI ##Importamos FastAPI
import uvicorn 

app = FastAPI() ##instanciar FastAPI

@app.get("/") ## con GET obtengo en / a través del protocolo HTTP 
async def root(): ## uso async para que la aplicación no se detenga.
    return {"Hello": "World"}

## En FastAPI puedo utilizar UVICORN para levantar el servidor.
## para esto ejecuto en la terminal $ uvicorn main:app --reload

@app.get("/url")
async def root():
    return {"Hello": "prueba"}

#Documentacion con Swagger /docs
#Documentacion con Redocly /redoc

if __name__ == "__main__": ## con esto hago que se ejecute el servidor desde main 
    uvicorn.run(app, host="127.0.0.1", port=8000)
## También si ejecuto $ uvicorn main:app --reload por consola levanto el servidor
