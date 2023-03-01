from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from models.database import engine
from oracle_connection import machineCount, lotCode, machine_name, machinelist
from fastapi.middleware.cors import CORSMiddleware
from typing import List


from models.Machine_Status_Record_Module import machine_status_record_module
from routers.InsMachine_Status_Record import insmachine_status_router

app = FastAPI()

origins = [
    "*",
    "http://localhost:8005",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(insmachine_status_router.router)

@app.get("/")
def hello():
    return {"hello":"FastAPI"}


@app.get('/mccount')
def get_mcCount():
    result = machineCount()
    return {'mc_count': result}
    
    
@app.get('/getlot{code}')
def get_mcCount(code:str):
    product = lotCode(code)[1]
    lot = lotCode(code)[0]
    return {'lot': lot, 'product':product}
    
    
@app.get('/getmc{mcid}')
def get_mcdata(mcid:int):
    machineName = machine_name(mcid)[0]
    machineNo = machine_name(mcid)[1]
    return {'Machine_Name': machineName, 'Machine_No':machineNo}
    
    

@app.get('/getInsMachineList')
def get_mcInsList():
    machineList = machinelist()
    return {'MachineList': machineList}
    
    
    
machine_status_record_module.Base.metadata.create_all(engine)