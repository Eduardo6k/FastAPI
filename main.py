from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import traceback


app = FastAPI()

class Inputs(BaseModel):
    id: str
    resource: str
    user_id: int
    topic: str
    application_id: int
    attempts: int
    sent: str
    received: str

@app.get("/")
def home():
    return "MINHA API ESTÁ NO AR"
    
lista = []
@app.post("/ml")
def Ml(inputs: Inputs) -> str:
    # Verificar se o campo _id está presente
    if inputs._id is None:
        return "O campo _id é obrigatório."
    
    lista.clear()
    lista.append(str(inputs))
    return str(inputs)

@app.get("/get")
def get():
    return str(lista)
    
    
   






