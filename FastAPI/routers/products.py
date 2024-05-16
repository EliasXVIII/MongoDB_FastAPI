from fastapi import APIRouter
import uvicorn

router = APIRouter(prefix="/products",
                tags=["products"],##Se utiliza tags para la documentación
                responses={404:{"message":"no encontrado"}})

products_list = ["producto1", "producto2", "producto3", "producto4", "producto5", "producto6"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]

if __name__ == "__main__": ## con esto hago que se ejecute el servidor desde main 
    uvicorn.run(router, host="127.0.0.1", port=8000)