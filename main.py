# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:30:33 2023

@author: Eduar
"""

from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector



app = FastAPI()

class Inputs(BaseModel):
  id : str   
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
    query = '''
        INSERT INTO sua_tabela (id, resource, user_id, topic, application_id, attempts, sent, received)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
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

 
db_config = {
    'user': 'root',
    'password': '3CdSQWBdD70V8AYhHa1D',
    'host': 'containers-us-west-165.railway.app',
    'database': 'railway'
}
def execute_query(query, args=None):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    if args:
        cursor.execute(query, args)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

   



    
    
    
