from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.employee_schema import EmployeeCreate
from services.employee_service import *

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
def add_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, data)


@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)


@router.delete("/{emp_id}")
def remove_employee(emp_id: int, db: Session = Depends(get_db)):
    return delete_employee(db, emp_id)