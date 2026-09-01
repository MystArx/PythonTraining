from fastapi import FastAPI
from sqlalchemy import select, update, delete,func

from database import SessionLocal
from models import Employee, Project, ProjectAllocation
from create_tables import create_database_tables

from datetime import datetime,date


app = FastAPI()

create_database_tables()

@app.get("/status")
def status():

    return {
        "message": "API Up"
    }


@app.post("/insertemployee")
def insert_employee(
    emp_name: str,
    emp_age: int,
    emp_gender: str,
    emp_email: str,
    emp_salary: int
):

    session = SessionLocal()

    try:

        employee = Employee(
            emp_name=emp_name,
            emp_age=emp_age,
            emp_gender=emp_gender,
            emp_email=emp_email,
            emp_salary=emp_salary
        )

        session.add(employee)
        session.commit()
        session.refresh(employee)

        return {
            "message": "Employee added successfully",
            "emp_id": employee.emp_id
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to add employee",
            "error": str(e)
        }


@app.get("/employees")
def get_employees():

    session = SessionLocal()

    try:

        query = select(Employee).order_by(Employee.emp_id)

        employees = session.scalars(query).all()

        if not employees:
            return {
                "message": "No employees found"
            }

        return employees

    except Exception as e:

        return {
            "message": "Failed to retrieve employees",
            "error": str(e)
        }


@app.get("/employee")
def get_employee(emp_id: int):

    session = SessionLocal()

    try:

        employee = session.get(Employee, emp_id)

        if employee is None:
            return {
                "message": "Employee not found"
            }

        return employee

    except Exception as e:

        return {
            "message": "Failed to find employee",
            "error": str(e)
        }


@app.put("/updateemployee")
def update_employee(
    emp_id: int,
    emp_name: str,
    emp_age: int,
    emp_gender: str,
    emp_email: str,
    emp_salary: int
):

    session = SessionLocal()

    try:

        employee = session.get(Employee, emp_id)

        if employee is None:
            return {
                "message": "Employee not found"
            }

        query = (
            update(Employee)
            .where(Employee.emp_id == emp_id)
            .values(
                emp_name=emp_name,
                emp_age=emp_age,
                emp_gender=emp_gender,
                emp_email=emp_email,
                emp_salary=emp_salary
            )
        )

        session.execute(query)
        session.commit()

        return {
            "message": "Employee updated successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to update employee",
            "error": str(e)
        }

    finally:

        session.close()



@app.delete("/deleteemployee")
def delete_employee(emp_id: int):

    session = SessionLocal()

    try:

        employee = session.get(Employee, emp_id)

        if employee is None:
            return {
                "message": "Employee not found"
            }

        session.delete(employee)
        session.commit()

        return {
            "message": "Employee deleted successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to delete employee",
            "error": str(e)
        }

    finally:

        session.close()


@app.post("/insertproject")
def insert_project(
    name: str,
    duration: int,
    customer_name: str,
    technology: str,
    status: str
):

    session = SessionLocal()

    try:

        project = Project(
            name=name,
            duration=duration,
            customer_name=customer_name,
            technology=technology,
            status=status
        )

        session.add(project)
        session.commit()
        session.refresh(project)

        return {
            "message": "Project added successfully",
            "project_id": project.project_id
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to add project",
            "error": str(e)
        }

    finally:

        session.close()


@app.get("/projects")
def get_projects():

    session = SessionLocal()

    try:

        query = select(Project).order_by(Project.project_id)

        projects = session.scalars(query).all()

        if not projects:
            return {
                "message": "No projects found"
            }

        return projects

    except Exception as e:

        return {
            "message": "Failed to retrieve projects",
            "error": str(e)
        }

    finally:

        session.close()


@app.get("/project")
def get_project(project_id: int):

    session = SessionLocal()

    try:

        project = session.get(Project, project_id)

        if project is None:
            return {
                "message": "Project not found"
            }

        return project

    except Exception as e:

        return {
            "message": "Failed to find project",
            "error": str(e)
        }

    finally:

        session.close()


@app.put("/updateproject")
def update_project(
    project_id: int,
    name: str,
    duration: int,
    customer_name: str,
    technology: str,
    status: str
):

    session = SessionLocal()

    try:

        project = session.get(Project, project_id)

        if project is None:
            return {
                "message": "Project not found"
            }

        query = (
            update(Project)
            .where(Project.project_id == project_id)
            .values(
                name=name,
                duration=duration,
                customer_name=customer_name,
                technology=technology,
                status=status
            )
        )

        session.execute(query)
        session.commit()

        return {
            "message": "Project updated successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to update project",
            "error": str(e)
        }

    finally:

        session.close()


@app.delete("/deleteproject")
def delete_project(project_id: int):

    session = SessionLocal()

    try:

        project = session.get(Project, project_id)

        if project is None:
            return {
                "message": "Project not found"
            }

        session.delete(project)
        session.commit()

        return {
            "message": "Project deleted successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to delete project",
            "error": str(e)
        }

    finally:

        session.close()


@app.post("/insertallocation")
def insert_allocation(projectId,emp_id,endDate):
    today=datetime.now()
    session=SessionLocal()
    
    try:

        project_alloc = ProjectAllocation(
            empid=emp_id,
            project_id=projectId,
            allocation_start_date=today,
            end_date=endDate
        )

        session.add(project_alloc)
        session.commit()
        session.refresh(project_alloc)

        return {
            "message": "Project added successfully",
            "project_id": project_alloc.project_alloc_id
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to add project",
            "error": str(e)
        }

    finally:

        session.close()


@app.get("/allocations")
def get_allocations():

    session = SessionLocal()

    try:

        query = (
            select(ProjectAllocation)
            .order_by(ProjectAllocation.proj_alloc_id)
        )

        allocations = session.scalars(query).all()

        if not allocations:
            return {
                "message": "No project allocations found"
            }

        return allocations

    except Exception as e:

        return {
            "message": "Failed to retrieve allocations",
            "error": str(e)
        }

    finally:

        session.close()



@app.get("/allocation")
def get_allocation(id: int):

    session = SessionLocal()

    try:

        allocation = session.get(ProjectAllocation, id)

        if allocation is None:
            return {
                "message": "Project allocation not found"
            }

        return allocation

    except Exception as e:

        return {
            "message": "Failed to find allocation",
            "error": str(e)
        }

    finally:

        session.close()


@app.put("/updateallocation")
def update_allocation(
    allocation_id: int,
    projectId: int,
    emp_id: int,
    endDate: date
):

    session = SessionLocal()

    try:
        allocation = session.get(
            ProjectAllocation,
            allocation_id
        )

        if allocation is None:
            return {
                "message": "Project allocation not found"
            }

        employee = session.get(Employee, emp_id)

        if employee is None:
            return {
                "message": "Employee not found"
            }

        project = session.get(Project, projectId)

        if project is None:
            return {
                "message": "Project not found"
            }

        today = date.today()

        query = (
            select(func.count(ProjectAllocation.proj_alloc_id))
            .where(
                ProjectAllocation.empid == emp_id,
                ProjectAllocation.end_date >= today,
                ProjectAllocation.proj_alloc_id != allocation_id
            )
        )

        active_allocations = session.scalar(query)

        if (active_allocations!=None) and  (active_allocations>= 5):
            return {
                "message": "Employee already has maximum 5 active project allocations"
            }

        query = (
            update(ProjectAllocation)
            .where(
                ProjectAllocation.proj_alloc_id == allocation_id
            )
            .values(
                empid=emp_id,
                project_id=projectId,
                end_date=endDate
            )
        )

        session.execute(query)
        session.commit()

        return {
            "message": "Project allocation updated successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to update allocation",
            "error": str(e)
        }

    finally:

        session.close()


@app.delete("/deleteallocation")
def delete_allocation(id: int):

    session = SessionLocal()

    try:

        allocation = session.get(
            ProjectAllocation,
            id
        )

        if allocation is None:
            return {
                "message": "Project allocation not found"
            }

        session.delete(allocation)
        session.commit()

        return {
            "message": "Project allocation deleted successfully"
        }

    except Exception as e:

        session.rollback()

        return {
            "message": "Failed to delete allocation",
            "error": str(e)
        }

    finally:

        session.close()


@app.get("/viewallocations")
def view_allocations():

    session = SessionLocal()

    try:

        query = (
            select(
                ProjectAllocation.proj_alloc_id.label("allocation_id"),

                Employee.emp_id,
                Employee.emp_name,

                Project.project_id,
                Project.name.label("project_name"),
                Project.technology,
                Project.status,

                ProjectAllocation.allocation_start_date,
                ProjectAllocation.end_date
            )
            .join(
                Employee,
                ProjectAllocation.empid == Employee.emp_id
            )
            .join(
                Project,
                ProjectAllocation.project_id == Project.project_id
            )
            .order_by(ProjectAllocation.proj_alloc_id)
        )

        result = session.execute(query).mappings().all()

        if not result:
            return {
                "message": "No project allocations found"
            }

        return result

    except Exception as e:

        return {
            "message": "Failed to retrieve allocation details",
            "error": str(e)
        }

    finally:

        session.close()



@app.get("/employee/allocations")
def employee_allocations(emp_id: int):

    session = SessionLocal()

    try:

        employee = session.get(Employee, emp_id)

        if employee is None:
            return {
                "message": "Employee not found"
            }

        query = (
            select(
                ProjectAllocation.proj_alloc_id.label("allocation_id"),
                Employee.emp_name,
                Project.name.label("project_name"),
                Project.technology,
                Project.status,
                ProjectAllocation.allocation_start_date,
                ProjectAllocation.end_date
            )
            .join(
                Employee,
                ProjectAllocation.empid == Employee.emp_id
            )
            .join(
                Project,
                ProjectAllocation.project_id == Project.project_id
            )
            .where(ProjectAllocation.empid == emp_id)
            .order_by(ProjectAllocation.proj_alloc_id)
        )

        result = session.execute(query).mappings().all()

        return result

    except Exception as e:

        return {
            "message": "Failed to retrieve employee allocations",
            "error": str(e)
        }

    finally:

        session.close()