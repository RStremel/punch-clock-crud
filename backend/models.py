from sqlalchemy import Column, Integer, String, Date, Time, DateTime
from sqlalchemy.sql import func
from database import Base

class RecordsModel(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_id = Column(String)
    workplace = Column(String)
    day_worked = Column(Date)
    shift_start = Column(Time)
    shift_end = Column(Time)
    lunch_start = Column(Time)
    lunch_end = Column(Time)
    period_worked = Column(Time)
    created_at = Column(DateTime(timezone=True), default=func.now())