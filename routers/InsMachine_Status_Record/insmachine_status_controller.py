from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func, text
from datetime import datetime, timedelta

from models.Machine_Status_Record_Module.machine_status_record_module import DbInsMachine, InsMachineStatusBase


def create(db: Session, request: InsMachineStatusBase):
    new_InsMahineStatusdata = DbInsMachine(
        MachineID=request.MachineID,
        MachineName=request.MachineName,
        MachineNo=request.MachineNo,
        Product=request.Product,
        Lot=request.Lot,
        LotCode=request.LotCode,
        Status=request.Status,
        Remark=request.Remark
    )
    db.add(new_InsMahineStatusdata)
    db.commit()
    db.refresh(new_InsMahineStatusdata)
    return new_InsMahineStatusdata


def delete(db: Session, id: int):
    status = db.query(DbInsMachine).filter(DbInsMachine.id == id).first()
    db.delete(status)
    db.commit()
    return JSONResponse(content={"detail": f"Machine Status id {id} deleted"})


def read_stockmaster(db: Session):
    return db.query(DbInsMachine).all()


def update(db: Session, id: int, request: InsMachineStatusBase):
    status = db.query(DbInsMachine).filter(DbInsMachine.id == id).first()
    status.MachineID = request.MachineID
    status.MachineName = request.MachineName
    status.MachineNo = request.MachineNo
    status.Product = request.Product
    status.Lot = request.Lot
    status.LotCode = request.LotCode
    status.Status = request.Status
    status.Remark = request.Remark
    
    db.commit()
    db.refresh(status)
    return status
    
    
def searchMatch(db: Session,  mcid:str, lotid:str):
    return db.query(
        (DbInsMachine.Status).label("Status")
    ).filter(
        DbInsMachine.MachineID==mcid
    ).filter(
        DbInsMachine.LotCode==lotid
    ).order_by(
        DbInsMachine.id.desc()
    ).first()