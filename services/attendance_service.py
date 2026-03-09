from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.attendance_repo import AttendanceRepository

def mark_attendance(db: Session, data):

    if not AttendanceRepository.check_employee_exists(db, data.employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    
    
    existing_attendance = AttendanceRepository.get_attendance_by_date(
        db, data.employee_id, data.date
    )
    
    if existing_attendance:
       
        updated_record = AttendanceRepository.update_attendance_status(
            db, existing_attendance, data.status
        )
        return {
            "status_code": 200,
            "message": "Attendance status updated successfully",
            "data": updated_record
        }
    
   
    new_attendance = AttendanceRepository.create_attendance(db, data)
    
    return {
        "status_code": 201,
        "message": "Attendance marked successfully",
        "data": new_attendance
    }    

def get_employee_attendance(db: Session, emp_id: int, page: int = 1, size: int = 10):
    skip = (page - 1) * size
    
    
    if not AttendanceRepository.check_employee_exists(db, emp_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    
   
    records, total = AttendanceRepository.get_by_employee_id(db, emp_id, skip, size)
    
    return {
        "status_code": 200,
        "message": "Attendance records fetched successfully",
        "total_count": total,
        "data": records
    }