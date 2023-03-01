from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT, VARCHAR
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbInsMachine(Base):
    __tablename__ = "Machine_Status_Record"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    MachineID =  Column(Integer, unique=False)
    MachineName =  Column(String, unique=False)
    MachineNo =  Column(String, unique=False)
    Product =  Column(String, unique=False)
    Lot =  Column(String, unique=False)
    LotCode =  Column(String, unique=False)
    Status =  Column(String, unique=False)
    Remark =  Column(String, unique=False)

class InsMachineStatusBase(BaseModel):
    MachineID : int
    MachineName : str
    MachineNo : str
    Product : str
    Lot : str
    LotCode : str
    Status : str
    Remark : str


class InsMachineStatusDisplayBase(BaseModel):
    id: int
    datetime : datetime
    MachineID : int
    MachineName : str
    MachineNo : str
    Product : str
    Lot : str
    LotCode : str
    Status : str
    Remark : str

    class Config:
        orm_mode = True

