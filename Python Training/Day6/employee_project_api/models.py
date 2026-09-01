from db_connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Employee(Base):
    __tablename__="employees"

    employee_id=Column(Integer,primary_key=True,autoincrement=True)

    employee_name=Column(String(50),nullable=False)      

    employee_email=Column(String(100),nullable=False,unique=True)      

    employee_department=Column(String(50),nullable=False)

    employee_salary=Column(Integer,nullable=False) 


class Project(Base):
    __tablename__="projects"

    project_id=Column(Integer,primary_key=True,autoincrement=True)

    project_name=Column(String(50),nullable=False)      

    project_description=Column(String(100),nullable=False)      

    project_status=Column(String(50),nullable=False)

    employee_id=Column(Integer,ForeignKey("employees.employee_id"),nullable=False)