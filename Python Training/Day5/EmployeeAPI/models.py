from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date

Base = declarative_base()


class Employee(Base):

    __tablename__ = "employees"

    emp_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    emp_name = Column(String(50))
    emp_age = Column(Integer)
    emp_gender = Column(String(10))
    emp_email = Column(String(50))
    emp_salary = Column(Integer)

    allocations = relationship(
        "ProjectAllocation",
        back_populates="employee"
    )


class Project(Base):

    __tablename__ = "projects"

    project_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name = Column(String(50))
    duration = Column(Integer)
    customer_name = Column(String(50))
    technology = Column(String(50))
    status = Column(String(20))

    allocations = relationship(
        "ProjectAllocation",
        back_populates="project"
    )


class ProjectAllocation(Base):

    __tablename__ = "project_allocation"

    proj_alloc_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    empid = Column(
        Integer,
        ForeignKey("employees.emp_id"),
        nullable=False
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.project_id"),
        nullable=False
    )

    allocation_start_date = Column(Date)
    end_date = Column(Date)

    employee = relationship(
        "Employee",
        back_populates="allocations"
    )

    project = relationship(
        "Project",
        back_populates="allocations"
    )