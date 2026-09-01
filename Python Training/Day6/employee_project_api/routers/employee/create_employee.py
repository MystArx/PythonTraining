from fastapi import HTTPException
from db_connection import LocalSession
from models import Employee
from schemas import EmployeeCreate

def create_employee(employee : EmployeeCreate):
    session=LocalSession()
    try:
        new_employee=Employee(
            employee_name=employee.employee_name,
            employee_email=employee.employee_email,
            employee_department=employee.employee_department,
            employee_salary=employee.employee_salary
        )
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
        return new_employee

    except Exception as e:
        session.rollback()
        raise  HTTPException(status_code=500)