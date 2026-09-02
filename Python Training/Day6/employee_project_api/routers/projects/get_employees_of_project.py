from db_connection import LocalSession
from models import Project
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

def get_employees_of_project(id: int):
    session = LocalSession()
    try:
        project = session.query(Project).options(selectinload(Project.employees)).filter(Project.project_id == id).first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        return project.employees
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
