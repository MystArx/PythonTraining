from fastapi import APIRouter
from schemas import (
    ProjectCreate, ProjectResponse, ProjectResponseWithEmployees, ProjectUpdate,
    EmployeeResponse, AllocationRequest
)
from routers.projects.create_project import create_project
from routers.projects.get_all_projects import get_all_projects
from routers.projects.get_all_projects_with_employees import get_all_projects_with_employees
from routers.projects.get_project_by_id import get_project_by_id
from routers.projects.get_projects_by_employee import get_projects_by_employee
from routers.projects.get_employees_of_project import get_employees_of_project
from routers.projects.assign_employee_to_project import assign_employee_to_project
from routers.projects.remove_employee_from_project import remove_employee_from_project
from routers.projects.update_project import updateProject
from routers.projects.delete_project import deleteProject

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/get", response_model=list[ProjectResponse])
def getProjects():
    return get_all_projects()

@router.get("/get_with_employees", response_model=list[ProjectResponseWithEmployees])
def getProjectsWithEmployees():
    """Get all projects along with all their assigned employees (Many-to-Many)."""
    return get_all_projects_with_employees()

@router.get("/get/{id}", response_model=ProjectResponseWithEmployees)
def getProjectById(id: int):
    return get_project_by_id(id)

@router.get("/employee/{employee_id}", response_model=list[ProjectResponse])
def getProjectsByEmployee(employee_id: int):
    """Get all projects of 1 employee."""
    return get_projects_by_employee(employee_id)

@router.get("/{id}/employees", response_model=list[EmployeeResponse])
def getEmployeesOfProject(id: int):
    """Get all employees working on 1 project."""
    return get_employees_of_project(id)

@router.post("/add", response_model=ProjectResponse)
def addProject(project: ProjectCreate):
    return create_project(project)

@router.post("/assign")
def assignEmployee(allocation: AllocationRequest):
    """Assign an employee to a project."""
    return assign_employee_to_project(allocation)

@router.delete("/remove")
def removeEmployee(allocation: AllocationRequest):
    """Remove an employee from a project."""
    return remove_employee_from_project(allocation)

@router.put("/update/{id}")
def update_project(id: int, project: ProjectUpdate):
    return updateProject(id, project)

@router.delete("/delete/{id}")
def delete_project(id: int):
    return deleteProject(id)
