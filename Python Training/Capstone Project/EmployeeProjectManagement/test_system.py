# Simple Automated Test Script

import unittest
import os
from database import employees, projects, allocations
from models import Employee, Project, EmployeeProject
from employee_service import (
    add_employee, get_all_employees, search_employee, update_employee,
    delete_employee, filter_by_skill, filter_by_experience, sort_by_salary, sort_by_experience
)
from project_service import add_project, get_all_projects, update_project, delete_project
from allocation_service import allocate_employee, remove_allocation
from report_service import export_employee_data, read_exported_report
from exceptions import EmployeeNotFoundException, InvalidAllocationException

class TestStudentSystem(unittest.TestCase):

    def test_add_employee(self):
        emp = add_employee("Test Student", "test.student@example.com", 2.0, "Python", 50000.0)
        self.assertIsNotNone(emp)
        self.assertEqual(emp.employee_name, "Test Student")

    def test_search_employee(self):
        results = search_employee("Amit")
        self.assertTrue(len(results) > 0)

    def test_lambda_operations(self):
        py_emps = filter_by_skill("Python")
        self.assertTrue(len(py_emps) > 0)

        sorted_sal = sort_by_salary()
        self.assertTrue(sorted_sal[0].employee_salary >= sorted_sal[-1].employee_salary)

        sorted_exp = sort_by_experience()
        self.assertTrue(sorted_exp[0].employee_experience >= sorted_exp[-1].employee_experience)

    def test_export_data(self):
        export_employee_data()
        self.assertTrue(os.path.exists("reports/employee_report.txt"))

if __name__ == "__main__":
    unittest.main()
