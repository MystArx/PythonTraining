# OOP Data Models

class Employee:
    def __init__(self, employee_id, employee_name, employee_email, employee_experience, employee_skill, employee_salary, employee_status="Available"):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_email = employee_email
        self.employee_experience = float(employee_experience)
        self.employee_skill = employee_skill
        self.employee_salary = float(employee_salary)
        self.employee_status = employee_status

    def __repr__(self):
        return f"Employee({self.employee_id}, {self.employee_name}, {self.employee_email}, {self.employee_experience}yrs, {self.employee_skill}, ₹{self.employee_salary}, {self.employee_status})"


class Project:
    def __init__(self, project_id, project_name, client_name, technology, project_duration, project_status="Active"):
        self.project_id = str(project_id)
        self.project_name = project_name
        self.client_name = client_name
        self.technology = technology
        self.project_duration = int(project_duration)
        self.project_status = project_status

    def __repr__(self):
        return f"Project('{self.project_id}', '{self.project_name}', '{self.client_name}', '{self.technology}', {self.project_duration}m, '{self.project_status}')"


class EmployeeProject:
    def __init__(self, allocation_id, employee_id, project_id, role, allocation_percentage, allocation_date="2026-08-31"):
        self.allocation_id = allocation_id
        self.employee_id = employee_id
        self.project_id = str(project_id)
        self.role = role
        self.allocation_percentage = int(allocation_percentage)
        self.allocation_date = allocation_date

    def __repr__(self):
        return f"EmployeeProject({self.allocation_id}, Emp:{self.employee_id}, Proj:'{self.project_id}', Role:'{self.role}', {self.allocation_percentage}%)"
