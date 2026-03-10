from sqlalchemy import Column, Integer, String , Boolean
from database.connection import Base

class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    department = Column(String(100))
    is_active = Column(Boolean, default=True)