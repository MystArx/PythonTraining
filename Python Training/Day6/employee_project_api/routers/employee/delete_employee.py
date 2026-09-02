from db_connection import LocalSession
from models import Employee
from sqlalchemy import delete
from fastapi import HTTPException

def deleteEmployee(id: int):
    session = LocalSession()
    try:
        employee_check = session.get(Employee, id)

        if employee_check is None:
            raise HTTPException(status_code=404, detail="Employee not found")

        query = delete(Employee).where(Employee.employee_id == id)
        session.execute(query)
        session.commit()
        return {
            "message": "deletion done"
        }
    except HTTPException:
        session.rollback()
        raise
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()