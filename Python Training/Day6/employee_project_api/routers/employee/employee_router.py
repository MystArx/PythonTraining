from fastapi import APIRouter
from schemas import EmployeeCreate, EmployeeResponse, EmployeeResponseWithProjects, EmployeeUpdate
from routers.employee.create_employee import create_employee
from routers.employee.get_all_employees import get_all_employees
from routers.employee.get_employee_by_id import get_employee_by_id
from routers.employee.get_employee_with_projects import get_employee_with_projects
from routers.employee.update_employee import updateEmployee
from routers.employee.delete_employee import deleteEmployee

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/get", response_model=list[EmployeeResponse])
def getEmployees():
    return get_all_employees()

@router.get("/get/{id}", response_model=EmployeeResponse)
def getEmployeeById(id: int):
    return get_employee_by_id(id)

@router.get("/get_with_projects/{id}", response_model=EmployeeResponseWithProjects)
def getEmployeeWithProjects(id: int):
    return get_employee_with_projects(id)

@router.post("/add", response_model=EmployeeResponse)
def addEmployee(employee: EmployeeCreate):
    return create_employee(employee)

@router.put("/update/{id}")
def update_employee(id: int, employee: EmployeeUpdate):
    return updateEmployee(id, employee)

@router.delete("/delete/{id}")
def delete_employee(id: int):
    return deleteEmployee(id)