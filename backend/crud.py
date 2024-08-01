from sqlalchemy.orm import Session
from schemas import RecordsCreate, RecordsUpdate
from models import RecordsModel

def get_all_records(db: Session):
    """
    Retrieves all sign in and sign out records from employees.
    """
    records = db.query(RecordsModel).all()

    if not records:
        return None
    return records

def get_record_by_id(db: Session, record_id: int):
    """
    Retrieves a record from a record ID.
    """
    return db.query(RecordsModel).filter(RecordsModel.id == record_id).first()

def create_record(db: Session, record: RecordsCreate):
    """
    Creates a sign in and sign out record and saves it in the database.
    """
    db_record = RecordsModel(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def delete_record(db: Session, record_id: int):
    """
    Deletes a record by selecting its ID.
    """
    db_record = db.query(RecordsModel).filter(RecordsModel.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
    return db_record

def update_record(db: Session, record_id: int, record: RecordsUpdate):
    """
    Updates a record by selecting its ID.
    """
    db_record = db.query(RecordsModel).filter(RecordsModel.id == record_id).first()

    if db_record is None:
        return None
    if record.employee_name is not None:
        db_record.employee_name = record.employee_name
    if record.employee_id is not None:
        db_record.employee_id = record.employee_id
    if record.workplace is not None:
        db_record.workplace = record.workplace
    if record.day_worked is not None:
        db_record.day_worked = record.day_worked
    if record.shift_start is not None:
        db_record.shift_start = record.shift_start
    if record.shift_end is not None:
        db_record.shift_end = record.shift_end
    if record.lunch_start is not None:
        db_record.lunch_start = record.lunch_start
    if record.lunch_end is not None:
        db_record.lunch_end = record.lunch_end
    if record.period_worked is not None:
        db_record.period_worked = record.period_worked

    db.commit()
    db.refresh(db_record)
    return db_record