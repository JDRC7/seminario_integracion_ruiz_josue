from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str 

@router.get("/")
def read_root() -> dict[str,str]:
    return{"Mensaje": "Hola desde FastAPI + uv",
           "Autor": "Josue Ruiz",
           "Version": "0.1.0"}


@router.get("/Josue")
def endpoint_Josue() -> Mensaje:
    return Mensaje(texto="Hola", campo_interno="desde Josue Ruiz")

@router.get("/Ruiz", response_model=Mensaje)
def endpoint_Ruiz():
    return {"texto": "Hola Josue Ruiz", "prioridad": 5, "campo_interno": "no debería salir"}

