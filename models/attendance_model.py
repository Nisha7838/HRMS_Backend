from sqlalchemy import Column, Integer, Date, String, ForeignKey ,Boolean
from database.connection import Base

class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    date = Column(Date)
    status = Column(Boolean, default=False)