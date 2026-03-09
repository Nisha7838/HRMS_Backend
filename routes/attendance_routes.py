from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.attendance_schema import AttendanceCreate
from services.attendance_service import *

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/")
def add_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    return mark_attendance(db, data)


@router.get("/{emp_id}")
def employee_attendance(emp_id: int, db: Session = Depends(get_db)):
    return get_employee_attendance(db, emp_id)