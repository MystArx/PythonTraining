from db_connection import LocalSession
from models import Project, Employee
from schemas import AllocationRequest
from fastapi import HTTPException

def remove_employee_from_project(allocation: AllocationRequest):
    session = LocalSession()
    try:
        project = session.get(Project, allocation.project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        employee = session.get(Employee, allocation.employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        if employee not in project.employees:
            raise HTTPException(status_code=400, detail="Employee is not assigned to this project")

        project.employees.remove(employee)
        session.commit()
        return {"message": f"Successfully removed Employee {employee.employee_name} from Project {project.project_name}"}
    except HTTPException:
        session.rollback()
        raise
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
