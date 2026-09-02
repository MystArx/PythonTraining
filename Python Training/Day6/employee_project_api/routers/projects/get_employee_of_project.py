from db_connection import LocalSession
from models import Project
from sqlalchemy.orm import joinedload
from fastapi import HTTPException

def get_employee_of_project(id: int):
    session = LocalSession()
    try:
        project = session.query(Project).options(joinedload(Project.employee)).filter(Project.project_id == id).first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        if project.employee is None:
            raise HTTPException(status_code=404, detail="No employee assigned to this project")
        return project.employee
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
