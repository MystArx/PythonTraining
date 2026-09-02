from db_connection import LocalSession
from models import Employee
from sqlalchemy import select
from fastapi import HTTPException

def get_all_employees():
    session = LocalSession()
    try:
        query = select(Employee)
        employees = session.scalars(query).all()
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()