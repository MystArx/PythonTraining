# Simple In-Memory Database Store

from models import Employee, Project, EmployeeProject

# Global lists holding data
employees = [
    Employee(101, "Amit Sharma", "amit@example.com", 3.5, "Python", 65000.0, "Allocated"),
    Employee(102, "Priya Verma", "priya@example.com", 5.0, "Java", 85000.0, "Allocated"),
    Employee(103, "Rohan Gupta", "rohan@example.com", 2.0, "Python", 48000.0, "Available"),
    Employee(104, "Sneha Reddy", "sneha@example.com", 4.0, "React", 72000.0, "Allocated"),
    Employee(105, "Ravi Kumar", "ravi@example.com", 6.0, "Python", 95000.0, "Available")
]

projects = [
    Project("P101", "Banking Automation", "ABC Bank", "Python", 12, "Active"),
    Project("P102", "E-Commerce Suite", "Global Retails", "Java", 8, "Active"),
    Project("P103", "Healthcare Portal", "HealthCare Inc", "React", 6, "Active"),
    Project("P104", "Legacy Migration", "FinanceCorp", "Java", 4, "Completed")
]

allocations = [
    EmployeeProject(1001, 101, "P101", "Developer", 100, "2026-01-15"),
    EmployeeProject(1002, 102, "P102", "Lead", 100, "2026-02-01"),
    EmployeeProject(1003, 104, "P103", "Developer", 75, "2026-03-10")
]

next_emp_id = 106
next_alloc_id = 1004

def get_next_employee_id():
    global next_emp_id
    eid = next_emp_id
    next_emp_id += 1
    return eid

def get_next_allocation_id():
    global next_alloc_id
    aid = next_alloc_id
    next_alloc_id += 1
    return aid
