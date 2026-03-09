from repositories.employee_repo import EmployeeRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException
def create_employee(db: Session, data):
    
    if EmployeeRepository.get_by_email(db, data.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    new_emp = EmployeeRepository.create(db, data)
    return {
        "status_code": 201,
        "message": "Employee created successfully"
    }

def get_all_employees(db: Session, page: int = 1, size: int = 10):
    skip = (page - 1) * size
    employees, total = EmployeeRepository.get_all(db, skip=skip, limit=size)
    
    return {
        "status_code": 200,
        "message": "Data fetched successfully",
        "total_count": total,
        "data": employees
    }

def delete_employee(db: Session, emp_id: int):
    success = EmployeeRepository.delete(db, emp_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {
        "status_code": 200,
        "message": "Employee deleted successfully"
    }