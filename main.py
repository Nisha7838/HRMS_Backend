from fastapi import FastAPI
from routes import attendance_routes, employee_routes

app = FastAPI(title="HRMS Backend")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
app.include_router(employee_routes.router)    
app.include_router(attendance_routes.router)

