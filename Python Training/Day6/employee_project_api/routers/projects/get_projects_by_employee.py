from db_connection import LocalSession
from models import Employee
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

def get_projects_by_employee(employee_id: int):
    session = LocalSession()
    try:
        employee = session.query(Employee).options(selectinload(Employee.projects)).filter(Employee.employee_id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee.projects
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
