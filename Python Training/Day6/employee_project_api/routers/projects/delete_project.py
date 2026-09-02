from db_connection import LocalSession
from models import Project
from sqlalchemy import delete
from fastapi import HTTPException

def deleteProject(id: int):
    session = LocalSession()
    try:
        project_check = session.get(Project, id)

        if project_check is None:
            raise HTTPException(status_code=404, detail="Project not found")

        query = delete(Project).where(Project.project_id == id)
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
