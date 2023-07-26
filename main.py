# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:30:33 2023

@author: Eduar
"""

from fastapi import FastAPI
from pydantic import BaseModel
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

vendas = {
    
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}
@app.get("/")
def home():
    return "MINHA API ESTÁ NO AR"

@app.get("/venda/{id_venda}")
def venda_especifica(id_venda: int):
    return vendas[id_venda]

@app.post("/ml")
def Ml(inputs: Inputs) -> str:
    return str(inputs)
    
    
    
