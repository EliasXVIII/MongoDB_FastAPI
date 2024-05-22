from pydantic import BaseModel
from typing import Optional


class User(BaseModel): ##El Base Model nos crea una entidad User
    id : Optional[str] = None #Con = None le estoy diciendo que probablemente no le llegue este valor y le digo que sera un String para que pueda utilizar ID de mayor magnitud
    username: str
    email: str

