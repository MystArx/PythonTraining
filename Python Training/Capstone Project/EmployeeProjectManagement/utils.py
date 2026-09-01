# Helper utilities for formatting and input validation

def print_header(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_employee(emp):
    print(f"ID: {emp.employee_id} | Name: {emp.employee_name} | Email: {emp.employee_email} | Skill: {emp.employee_skill} | Exp: {emp.employee_experience}yrs | Salary: ₹{emp.employee_salary} | Status: {emp.employee_status}")

def print_project(proj):
    print(f"ID: {proj.project_id} | Name: {proj.project_name} | Client: {proj.client_name} | Tech: {proj.technology} | Duration: {proj.project_duration}m | Status: {proj.project_status}")
