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

conn = mysql.connector.connect(
    host='localhost',       # Endereço do servidor do MySQL (exemplo: 'localhost')
    user='root',     # Nome do usuário do MySQL
    password='Agro',   # Senha do usuário do MySQL
    database='dev'    # Nome do banco de dados que você deseja usar
)
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS WebhookML (
        id INT AUTO_INCREMENT PRIMARY KEY,
        resource VARCHAR(255),
        user_id INT,
        topic VARCHAR(255),
        application_id INT,
        attempts INT,
        sent VARCHAR(255),
        received VARCHAR(255)
    )
''')

@app.post("/ml")
def Ml(inputs: Inputs) -> str:
    cur = conn.cursor()
    sql = '''
        INSERT INTO vendas (resource, user_id, topic, application_id, attempts, sent, received)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
        inputs.resource,
        inputs.user_id,
        inputs.topic,
        inputs.application_id,
        inputs.attempts,
        inputs.sent,
        inputs.received
    )
    cur.execute(sql, values)
    conn.commit()
    return "Dados inseridos com sucesso no banco de dados."

   



    
    
    
