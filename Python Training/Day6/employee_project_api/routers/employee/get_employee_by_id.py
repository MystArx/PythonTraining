from db_connection import LocalSession
from models import Employee
from fastapi import HTTPException

def get_employee_by_id(id: int):
    session = LocalSession()
    try:
        employee = session.get(Employee, id)
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    finally:
        session.close()
