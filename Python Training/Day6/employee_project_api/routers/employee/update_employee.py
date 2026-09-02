from db_connection import LocalSession
from models import Employee
from sqlalchemy import update
from schemas import EmployeeUpdate
from fastapi import HTTPException

def updateEmployee(id: int, employee: EmployeeUpdate):
    session = LocalSession()
    try:
        employee_check = session.get(Employee, id)

        if employee_check is None:
            raise HTTPException(status_code=404, detail="Employee not found")

        update_data = employee.model_dump(exclude_unset=True)
        if update_data:
            query = update(Employee).where(Employee.employee_id == id).values(**update_data)
            session.execute(query)
            session.commit()

        return {
            "message": "Updated"
        }
    except HTTPException:
        session.rollback()
        raise
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()