from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class EmployeeResponse(BaseModel):
    employee_id: int
    employee_name: str
    employee_email: str
    employee_department: str
    employee_salary: float

    model_config = ConfigDict(from_attributes=True)


class ProjectResponse(BaseModel):
    project_id: int
    project_name: str
    project_description: Optional[str] = None
    project_status: str

    model_config = ConfigDict(from_attributes=True)


class ProjectResponseWithEmployees(BaseModel):
    project_id: int
    project_name: str
    project_description: Optional[str] = None
    project_status: str

    employees: list[EmployeeResponse] = []
    model_config = ConfigDict(from_attributes=True)


class EmployeeResponseWithProjects(BaseModel):
    employee_id: int
    employee_name: str
    employee_email: EmailStr
    employee_department: str
    employee_salary: float

    projects: list[ProjectResponse] = []
    model_config = ConfigDict(from_attributes=True)

EmployeeResponseWithProject = EmployeeResponseWithProjects


class ProjectCreate(BaseModel):
    project_name: str
    project_description: Optional[str] = None
    project_status: str
    employee_ids: Optional[list[int]] = []


class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    project_status: Optional[str] = None
    employee_ids: Optional[list[int]] = None


class EmployeeCreate(BaseModel):
    employee_name: str
    employee_email: EmailStr
    employee_department: str
    employee_salary: float


class EmployeeUpdate(BaseModel):
    employee_name: Optional[str] = None
    employee_email: Optional[EmailStr] = None
    employee_department: Optional[str] = None
    employee_salary: Optional[float] = None


class AllocationRequest(BaseModel):
    employee_id: int
    project_id: int
