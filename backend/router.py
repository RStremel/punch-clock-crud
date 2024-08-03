from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import RecordsCreate, RecordsRead, RecordsUpdate
from typing import List
from crud import delete_record, get_all_records, get_record_by_id, create_record, update_record

router = APIRouter()

@router.post("/records/", response_model=RecordsRead)
def create_records_route(record: RecordsCreate, db: Session = Depends(get_db)):
    return create_record(db=db, record=record)

@router.get("/records/", response_model=List[RecordsRead])
def read_all_records_route(db: Session = Depends(get_db)):
    records = get_all_records(db)
    return records

@router.get("/records/{record_id}", response_model=RecordsRead)
def read_record_by_id_route(record_id: int, db: Session = Depends(get_db)):
    db_records = get_record_by_id(db, record_id=record_id)
    if db_records is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_records

@router.delete("/records/{record_id}", response_model=RecordsRead)
def detele_record_route(record_id: int, db: Session = Depends(get_db)):
    db_records = delete_record(db, record_id=record_id)
    if db_records is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_records

@router.put("/records/{record_id}", response_model=RecordsRead)
def update_record_route(record_id: int, record: RecordsUpdate, db: Session = Depends(get_db)):
    db_records = update_record(db, record_id=record_id, record=record)
    if db_records is None:
        raise HTTPException(status_code=404, detail="Record nt found.")
    return db_records