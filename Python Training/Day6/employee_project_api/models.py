from db_connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

employee_projects = Table(
    "employee_projects",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.employee_id", ondelete="CASCADE"), primary_key=True),
    Column("project_id", Integer, ForeignKey("projects.project_id", ondelete="CASCADE"), primary_key=True)
)


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_name = Column(String(50), nullable=False)
    employee_email = Column(String(100), nullable=False, unique=True)
    employee_department = Column(String(50), nullable=False)
    employee_salary = Column(Integer, nullable=False)


    projects = relationship("Project", secondary=employee_projects, back_populates="employees")


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(50), nullable=False)
    project_description = Column(String(100), nullable=False)
    project_status = Column(String(50), nullable=False)

    employees = relationship("Employee", secondary=employee_projects, back_populates="projects")