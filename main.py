from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import attendance_routes, employee_routes

app = FastAPI(title="HRMS Backend")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
app.include_router(employee_routes.router)    
app.include_router(attendance_routes.router)

