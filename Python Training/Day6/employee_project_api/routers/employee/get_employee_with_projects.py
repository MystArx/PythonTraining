from db_connection import LocalSession
from models import Employee
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

def get_employee_with_projects(id: int):
    session = LocalSession()
    try:
        employee = session.query(Employee).options(selectinload(Employee.projects)).filter(Employee.employee_id == id).first()
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    finally:
        session.close()
