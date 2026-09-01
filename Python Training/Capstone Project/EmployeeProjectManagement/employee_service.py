# Employee Service Operations

from database import employees, get_next_employee_id
from models import Employee
from exceptions import EmployeeNotFoundException, InvalidAllocationException
from logger_config import logger

def add_employee(name, email, experience, skill, salary, status="Available"):
    if not name.strip():
        print("Error: Name cannot be empty.")
        return None
    for emp in employees:
        if emp.employee_email.lower() == email.strip().lower():
            print("Error: Email must be unique.")
            return None
    if experience < 0:
        print("Error: Experience cannot be negative.")
        return None
    if salary <= 0:
        print("Error: Salary must be positive.")
        return None
    if status not in ["Available", "Allocated"]:
        print("Error: Status must be Available or Allocated.")
        return None

    emp_id = get_next_employee_id()
    new_emp = Employee(emp_id, name.strip(), email.strip(), experience, skill.strip(), salary, status.strip())
    employees.append(new_emp)
    logger.info(f"Employee {emp_id} Created: {name}")
    return new_emp

def get_all_employees():
    return employees

def get_employee_by_id(emp_id):
    for emp in employees:
        if emp.employee_id == emp_id:
            return emp
    raise EmployeeNotFoundException(f"Employee ID {emp_id} not found.")

def search_employee(query):
    query_str = str(query).lower().strip()
    results = [e for e in employees if query_str in str(e.employee_id) or query_str in e.employee_name.lower() or query_str in e.employee_skill.lower()]
    return results

def update_employee(emp_id, skill=None, experience=None, salary=None, status=None):
    emp = get_employee_by_id(emp_id)
    if skill: emp.employee_skill = skill
    if experience is not None and experience >= 0: emp.employee_experience = float(experience)
    if salary is not None and salary > 0: emp.employee_salary = float(salary)
    if status in ["Available", "Allocated"]: emp.employee_status = status
    logger.info(f"Employee {emp_id} Updated")
    return emp

def delete_employee(emp_id, active_allocations=[]):
    emp = get_employee_by_id(emp_id)
    if emp_id in active_allocations:
        raise InvalidAllocationException(f"Cannot delete Employee {emp_id}: already allocated to an active project.")
    employees.remove(emp)
    logger.info(f"Employee {emp_id} Deleted")
    return emp

# Lambda Operations
def filter_by_skill(skill):
    return list(filter(lambda e: skill.lower() in e.employee_skill.lower(), employees))

def filter_by_experience(min_exp):
    return list(filter(lambda e: e.employee_experience >= min_exp, employees))

def filter_by_salary(min_sal):
    return list(filter(lambda e: e.employee_salary >= min_sal, employees))

def get_available_employees():
    return list(filter(lambda e: e.employee_status == "Available", employees))

def sort_by_salary(reverse=True):
    return sorted(employees, key=lambda e: e.employee_salary, reverse=reverse)

def sort_by_experience(reverse=True):
    return sorted(employees, key=lambda e: e.employee_experience, reverse=reverse)
