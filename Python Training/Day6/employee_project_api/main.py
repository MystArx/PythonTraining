from create_tables import create_tables
from fastapi import FastAPI
from routers.employee.employee_router import router as employee_router
from routers.projects.project_router import router as project_router

create_tables()

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "UP"
    }

app.include_router(employee_router)
app.include_router(project_router)