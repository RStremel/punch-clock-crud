from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional

class RecordsBase(BaseModel):
    employee_name: str
    employee_id: str
    workplace: str
    day_worked: date
    shift_start: datetime.time = None
    shift_end: datetime.time = None
    lunch_start: datetime.time = None
    lunch_end: datetime.time = None
    period_worked: datetime.time = None

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
    day_worked: Optional[date] = None
    shift_start: Optional[datetime.time] = None
    shift_end: Optional[datetime.time] = None
    lunch_start: Optional[datetime.time] = None
    lunch_end: Optional[datetime.time] = None
    period_worked: Optional[datetime.time] = None

