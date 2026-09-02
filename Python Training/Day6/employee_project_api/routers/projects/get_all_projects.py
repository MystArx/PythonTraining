from db_connection import LocalSession
from models import Project
from sqlalchemy import select
from fastapi import HTTPException

def get_all_projects():
    session = LocalSession()
    try:
        query = select(Project)
        projects = session.scalars(query).all()
        return projects
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
