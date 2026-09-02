from fastapi import HTTPException
from db_connection import LocalSession
from models import Project, Employee
from schemas import ProjectCreate

def create_project(project: ProjectCreate):
    session = LocalSession()
    try:
        new_project = Project(
            project_name=project.project_name,
            project_description=project.project_description or "",
            project_status=project.project_status
        )
        if project.employee_ids:
            employees = session.query(Employee).filter(Employee.employee_id.in_(project.employee_ids)).all()
            new_project.employees.extend(employees)

        session.add(new_project)
        session.commit()
        session.refresh(new_project)
        return new_project
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
