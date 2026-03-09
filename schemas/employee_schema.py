from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr
    department: str


class EmployeeResponse(BaseModel):
    employee_id: int
    full_name: str
    email: str
    department: str
class Config:
        from_attributes = True # SQLAlchemy model ko Pydantic mein convert karne ke liye