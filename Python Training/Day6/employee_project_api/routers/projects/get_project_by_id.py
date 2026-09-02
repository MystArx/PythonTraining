from db_connection import LocalSession
from models import Project
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

def get_project_by_id(id: int):
    session = LocalSession()
    try:
        project = session.query(Project).options(selectinload(Project.employees)).filter(Project.project_id == id).first()
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
    finally:
        session.close()
