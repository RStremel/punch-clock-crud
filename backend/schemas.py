from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional

class RecordsBase(BaseModel):
    employee_name: str
    employee_id: str
    workplace: str
    day_worked: date
    # shift_start: datetime.time = None
    # shift_end: datetime.time = None
    # lunch_time_start: datetime.time = None
    # lunch_time_end: datetime.time = None
    # overtime: bool = None
    # period_worked: datetime.time = None

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
    day_worked: Optional[date] = None
    workplace: Optional[str] = None
    # shift_start: Optional[datetime.time] = None
    # shift_end: Optional[datetime.time] = None
    # lunch_time_start: Optional[datetime.time] = None
    # lunch_time_end: Optional[datetime.time] = None
    # overtime: Optional[bool] = None
    # period_worked: Optional[datetime.time] = None

