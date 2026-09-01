# Allocation Service Operations

from database import allocations, get_next_allocation_id
from models import EmployeeProject
from employee_service import get_employee_by_id
from project_service import get_project_by_id
from exceptions import EmployeeAlreadyAllocatedException, InvalidAllocationException
from logger_config import logger

def get_employee_total_allocation(emp_id):
    total = 0
    for a in allocations:
        if a.employee_id == emp_id:
            try:
                p = get_project_by_id(a.project_id)
                if p.project_status == "Active":
                    total += a.allocation_percentage
            except Exception:
                pass
    return total

def sync_employee_status(emp_id):
    emp = get_employee_by_id(emp_id)
    total = get_employee_total_allocation(emp_id)
    emp.employee_status = "Allocated" if total >= 100 else "Available"

def allocate_employee(emp_id, project_id, role, percentage):
    emp = get_employee_by_id(emp_id)
    proj = get_project_by_id(project_id)

    if proj.project_status != "Active":
        raise InvalidAllocationException(f"Cannot allocate: Project '{proj.project_id}' is not Active.")

    if percentage not in [25, 50, 75, 100]:
        raise InvalidAllocationException("Percentage must be 25, 50, 75, or 100.")

    for a in allocations:
        if a.employee_id == emp_id and a.project_id == proj.project_id:
            raise EmployeeAlreadyAllocatedException(f"Employee {emp_id} already allocated to Project '{proj.project_id}'.")

    current_total = get_employee_total_allocation(emp_id)
    if current_total + percentage > 100:
        raise InvalidAllocationException(f"Cannot allocate {percentage}%. Current allocation is {current_total}%. Total cannot exceed 100%.")

    alloc_id = get_next_allocation_id()
    new_alloc = EmployeeProject(alloc_id, emp_id, proj.project_id, role, percentage)
    allocations.append(new_alloc)

    sync_employee_status(emp_id)
    logger.info(f"Employee {emp_id} Assigned to Project '{proj.project_id}'")
    return new_alloc

def remove_allocation(emp_id, project_id):
    pid = str(project_id).upper().strip()
    target = None
    for a in allocations:
        if a.employee_id == emp_id and a.project_id == pid:
            target = a
            break
    if not target:
        raise InvalidAllocationException(f"No allocation found for Employee {emp_id} on Project '{pid}'.")

    allocations.remove(target)
    sync_employee_status(emp_id)
    logger.info(f"Removed Allocation for Employee {emp_id} on Project '{pid}'")
    return target

def get_employees_of_project(project_id):
    pid = str(project_id).upper().strip()
    proj = get_project_by_id(pid)
    result = []
    for a in allocations:
        if a.project_id == pid:
            emp = get_employee_by_id(a.employee_id)
            result.append((emp, a))
    return result

def get_projects_of_employee(emp_id):
    emp = get_employee_by_id(emp_id)
    result = []
    for a in allocations:
        if a.employee_id == emp_id:
            proj = get_project_by_id(a.project_id)
            result.append((proj, a))
    return result
