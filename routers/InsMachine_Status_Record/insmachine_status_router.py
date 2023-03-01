from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.Machine_Status_Record_Module.machine_status_record_module import InsMachineStatusBase, InsMachineStatusDisplayBase

from routers.InsMachine_Status_Record import insmachine_status_controller

router = APIRouter(prefix="/insmachinestatuc", tags=["insmachinestatuc"])

@router.get("/mcid{mcid}:lodid{lotid}")
def get_status_match(mcid: str, lotid: str, db: Session = Depends(get_db)):
    return insmachine_status_controller.searchMatch(db, mcid, lotid)


@router.post("/")
def create_status(request: InsMachineStatusBase, db: Session = Depends(get_db)):
    return insmachine_status_controller.create(db, request)


@router.get("/", response_model=List[InsMachineStatusDisplayBase])
def get_all_status(db: Session = Depends(get_db)):
    return insmachine_status_controller.read_stockmaster(db)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return insmachine_status_controller.delete(db, id)


@router.put("/{id}")
def put_api(id: int, request:InsMachineStatusBase, db:Session=Depends(get_db)):
    return insmachine_status_controller.update(db, id, request)