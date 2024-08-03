from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class RecordsBase(BaseModel):
    employee_name: str
    employee_id: str
    workplace: str
    day_worked: str
    shift_start: str
    shift_end: str
    lunch_start: str
    lunch_end: str

class RecordsCreate(RecordsBase):
    pass

class RecordsRead(RecordsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class RecordsUpdate(RecordsBase):
    employee_name: Optional[str] = None
    employee_id: Optional[str] = None
    workplace: Optional[str] = None
    day_worked: Optional[str] = None
    shift_start: Optional[str] = None
    shift_end: Optional[str] = None
    lunch_start: Optional[str] = None
    lunch_end: Optional[str] = None