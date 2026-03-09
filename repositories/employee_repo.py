from sqlalchemy.orm import Session
from models.employee_model import Employee
from fastapi import HTTPException

class EmployeeRepository:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10):
        query = db.query(Employee)
        total = query.count()
        data = query.offset(skip).limit(limit).all()
        return data, total

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(Employee).filter(Employee.email == email).first()

    @staticmethod
    def create(db: Session, data):
        employee = Employee(
            full_name=data.full_name,
            email=data.email,
            department=data.department
        )
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    @staticmethod
    def delete(db: Session, emp_id: int):
        employee = db.query(Employee).filter(Employee.employee_id == emp_id).first()
        if employee:
            db.delete(employee)
            db.commit()
            return True
        return False