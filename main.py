from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

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

@app.post("/ml")
def Ml(inputs: Inputs) -> str:
    try:
        query = "INSERT INTO webhookMl2 (id, resource, user_id, topic, application_id, attempts, sent, received) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        args = (
            inputs.id,
            inputs.resource,
            inputs.user_id,
            inputs.topic,
            inputs.application_id,
            inputs.attempts,
            inputs.sent,
            inputs.received
        )
        execute_query(query, args)
        return "Dados inseridos com sucesso no banco de dados."
    except Exception as e:
        print("Erro:", e)
        return "Ocorreu um erro interno no servidor."




def execute_query(query, args=None):
    connection = mysql.connector.connect(host="containers-us-west-165.railway.app",user="root",password="3CdSQWBdD70V8AYhHa1D",database="railway",port=5656)
    cursor = connection.cursor()
    cursor.execute(query, args)
    connection.commit()  # Adicionando o commit para efetivar a inserção
    cursor.close()
    connection.close()




