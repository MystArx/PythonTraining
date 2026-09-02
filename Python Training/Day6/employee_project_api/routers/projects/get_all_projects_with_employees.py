from db_connection import LocalSession
from models import Project
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

def get_all_projects_with_employees():
    session = LocalSession()
    try:
        projects = session.query(Project).options(selectinload(Project.employees)).all()
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
