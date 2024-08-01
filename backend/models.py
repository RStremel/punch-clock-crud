from sqlalchemy import Column, Integer, String, Date, Time, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class RecordsModel(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_id = Column(String)
    day_worked = Column(Date, default=func.current_date())
    workplace = Column(String)
    shift_start = Column(Time)
    shift_end = Column(Time)
    lunch_time_start = Column(Time)
    lunch_time_end = Column(Time)
    overtime = Column(Boolean)
    period_worked = Column(Time)
    created_at = Column(DateTime(timezone=True), default=func.now())

# overtime (yes or no - calculo automatico acima de 8h)

# - Nome
# - Id
# - data (hoje)
# - horário entrada
# - horário saída
# - horário saída almoço
# - horário volta almoço
# - hora extra (acima de 8h)
# - tempo trabalhado (calculo)