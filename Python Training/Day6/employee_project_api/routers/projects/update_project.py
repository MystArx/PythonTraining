from db_connection import LocalSession
from models import Project, Employee
from schemas import ProjectUpdate
from fastapi import HTTPException

def updateProject(id: int, project: ProjectUpdate):
    session = LocalSession()
    try:
        project_obj = session.get(Project, id)
        if project_obj is None:
            raise HTTPException(status_code=404, detail="Project not found")

        if project.project_name is not None:
            project_obj.project_name = project.project_name
        if project.project_description is not None:
            project_obj.project_description = project.project_description
        if project.project_status is not None:
            project_obj.project_status = project.project_status
        if project.employee_ids is not None:
            employees = session.query(Employee).filter(Employee.employee_id.in_(project.employee_ids)).all()
            project_obj.employees = employees

        session.commit()
        return {"message": "Updated"}
    except HTTPException:
        session.rollback()
        raise
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
