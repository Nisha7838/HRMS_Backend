from sqlalchemy.orm import Session
from models.attendance_model import Attendance
from models.employee_model import Employee

class AttendanceRepository:
    @staticmethod
    def check_employee_exists(db: Session, emp_id: int):
        return db.query(Employee).filter(Employee.employee_id == emp_id).first()

    @staticmethod
    def get_attendance_by_date(db: Session, emp_id: int, attendance_date):
        return db.query(Attendance).filter(
            Attendance.employee_id == emp_id,
            Attendance.date == attendance_date
        ).first()

    @staticmethod
    def update_attendance_status(db: Session, attendance_obj, new_status: str):
        attendance_obj.status = new_status
        db.commit()
        db.refresh(attendance_obj)
        return attendance_obj    

    @staticmethod
    def create_attendance(db: Session, data):
        attendance = Attendance(
            employee_id=data.employee_id,
            date=data.date,
            status=data.status
        )
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance

    @staticmethod
    def get_by_employee_id(db: Session, emp_id: int, skip: int = 0, limit: int = 10):
        query = (
            db.query(Attendance, Employee.full_name)
            .join(Employee, Attendance.employee_id == Employee.employee_id)
            .filter(Attendance.employee_id == emp_id, Employee.is_active == True)  
        )

        total = query.count()
        data = query.offset(skip).limit(limit).all()
        result = [
            {
                "id": att.Attendance.id,
                "date": att.Attendance.date,
                "status": att.Attendance.status,
                "employee_full_name": att.full_name
            }
            for att in data
        ]
        
        return result, total