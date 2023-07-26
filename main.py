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

@app.get("/")
def home():
    return "MINHA API ESTÁ NO AR"


@app.post("/ml")
def Ml(inputs: Inputs) -> str:
   return inputs
 

   



    
    
    
