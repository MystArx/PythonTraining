# Report Service & File Handling

import os
from database import employees, projects, allocations
from employee_service import (
    get_all_employees, get_available_employees, filter_by_skill,
    sort_by_salary, sort_by_experience
)
from allocation_service import get_employees_of_project, get_projects_of_employee
from utils import print_header, print_employee
from logger_config import logger

os.makedirs("reports", exist_ok=True)
REPORT_FILE = "reports/employee_report.txt"

def report_all_employees():
    print_header("1. Complete Employee Report")
    for e in get_all_employees():
        print_employee(e)

def report_available_employees():
    print_header("2. Available Employees Report")
    for e in get_available_employees():
        print_employee(e)

def report_project_wise(project_id):
    print_header(f"3. Project-wise Employee Report ({project_id})")
    records = get_employees_of_project(project_id)
    if not records:
        print("No employees assigned to this project.")
    for emp, alloc in records:
        print(f"Emp ID: {emp.employee_id} | Name: {emp.employee_name} | Role: {alloc.role} | Alloc: {alloc.allocation_percentage}%")

def report_employee_wise(emp_id):
    print_header(f"4. Employee-wise Project Report (ID: {emp_id})")
    records = get_projects_of_employee(emp_id)
    if not records:
        print("No projects assigned to this employee.")
    for proj, alloc in records:
        print(f"Proj ID: {proj.project_id} | Name: {proj.project_name} | Role: {alloc.role} | Alloc: {alloc.allocation_percentage}%")

def report_skill_wise(skill):
    print_header(f"5. Skill-wise Employee Report ({skill})")
    for e in filter_by_skill(skill):
        print_employee(e)

def report_sorted_salary():
    print_header("6. Employees Sorted by Salary")
    for e in sort_by_salary():
        print_employee(e)

def report_sorted_experience():
    print_header("7. Employees Sorted by Experience")
    for e in sort_by_experience():
        print_employee(e)

def export_employee_data():
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("==================================================\n")
        f.write("       EMPLOYEE PROJECT ALLOCATION REPORT        \n")
        f.write("==================================================\n\n")
        for emp in employees:
            f.write(f"Employee ID: {emp.employee_id}\n")
            f.write(f"Employee Name: {emp.employee_name}\n")
            f.write(f"Skill: {emp.employee_skill}\n")
            f.write(f"Experience: {emp.employee_experience} Years\n")
            
            emp_allocs = [a for a in allocations if a.employee_id == emp.employee_id]
            if emp_allocs:
                for a in emp_allocs:
                    proj = next((p for p in projects if p.project_id == a.project_id), None)
                    proj_name = proj.project_name if proj else "N/A"
                    client = proj.client_name if proj else "N/A"
                    f.write(f"Project: {proj_name}\n")
                    f.write(f"Client: {client}\n")
                    f.write(f"Role: {a.role}\n")
                    f.write(f"Allocation: {a.allocation_percentage}%\n")
            else:
                f.write("Allocated Projects: None\n")
            f.write("==================================================\n\n")
    logger.info("Report Exported")
    print(f"Report exported to {REPORT_FILE}")

def read_exported_report():
    try:
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            print("\n--- REPORT FILE CONTENT ---")
            print(f.read())
    except FileNotFoundError:
        print("Error: Exported report file not found. Please export first.")
