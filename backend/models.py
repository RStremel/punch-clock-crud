from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class RecordsModel(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_id = Column(String)
    workplace = Column(String)
    day_worked = Column(String)
    shift_start = Column(String)
    shift_end = Column(String)
    shift_end = Column(String)
    lunch_start = Column(String)
    lunch_end = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())