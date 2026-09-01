from db_connection import LocalSession
from models import Employee
from sqlalchemy import select

def get_all_employees():
    session=LocalSession()
    try:
        query=select(Employee)
        employees=session.scalars(query).all()
        return employees
    except Exception as e:
        return {
            "error : ",e
        }