from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import traceback


app = FastAPI()

class Inputs(BaseModel):
    id: int
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

@app.post("/ml")
def Ml(inputs: Inputs) -> str:
    return str(inputs)
   






