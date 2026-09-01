# EMPLOYEE PROJECT MANAGEMENT SYSTEM - MAIN APPLICATION

from employee_service import (
    add_employee, get_all_employees, search_employee, update_employee, delete_employee,
    filter_by_skill, filter_by_experience, get_available_employees, sort_by_salary, sort_by_experience
)
from project_service import add_project, get_all_projects, update_project, delete_project, search_projects
from allocation_service import allocate_employee, remove_allocation, allocations
from report_service import (
    report_all_employees, report_available_employees, report_project_wise,
    report_employee_wise, report_skill_wise, report_sorted_salary, report_sorted_experience,
    export_employee_data, read_exported_report
)
from utils import print_employee, print_project
from exceptions import EmployeeNotFoundException, ProjectNotFoundException, InvalidAllocationException, EmployeeAlreadyAllocatedException
from logger_config import logger

def display_menu():
    print("\n" + "=" * 50)
    print("     EMPLOYEE PROJECT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Add Project")
    print("7. View Projects")
    print("8. Update Project")
    print("9. Delete Project")
    print("10. Allocate Employee to Project")
    print("11. Remove Employee from Project")
    print("12. View Employees of a Project")
    print("13. View Projects of an Employee")
    print("14. Filter Employees by Skill")
    print("15. Filter Employees by Experience")
    print("16. Sort Employees by Salary")
    print("17. Sort Employees by Experience")
    print("18. Show Available Employees")
    print("19. Generate Project Allocation Report")
    print("20. Export Employee Data")
    print("21. Read Exported Report")
    print("0. Exit")
    print("=" * 50)

def main():
    logger.info("Application Started")
    
    while True:
        try:
            display_menu()
            choice = input("Enter choice (0-21): ").strip()
            
            if choice == "0":
                logger.info("Application Closed")
                print("Exiting application. Goodbye!")
                break

            elif choice == "1":
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                exp = float(input("Enter Experience (years): "))
                skill = input("Enter Skill: ")
                salary = float(input("Enter Salary: "))
                emp = add_employee(name, email, exp, skill, salary)
                if emp:
                    print(f"Added: {emp}")

            elif choice == "2":
                report_all_employees()

            elif choice == "3":
                q = input("Enter search query (ID/Name/Skill): ")
                results = search_employee(q)
                for e in results:
                    print_employee(e)

            elif choice == "4":
                emp_id = int(input("Enter Employee ID: "))
                skill = input("Enter New Skill (leave blank to skip): ")
                exp_input = input("Enter New Experience (leave blank to skip): ")
                exp = float(exp_input) if exp_input else None
                sal_input = input("Enter New Salary (leave blank to skip): ")
                sal = float(sal_input) if sal_input else None
                status = input("Enter New Status (Available/Allocated) (leave blank to skip): ")
                updated = update_employee(emp_id, skill, exp, sal, status)
                print(f"Updated: {updated}")

            elif choice == "5":
                emp_id = int(input("Enter Employee ID: "))
                active_alloc_emp_ids = [a.employee_id for a in allocations]
                deleted = delete_employee(emp_id, active_alloc_emp_ids)
                print(f"Deleted Employee: {deleted.employee_name}")

            elif choice == "6":
                pid = input("Enter Project ID (e.g. P105): ")
                name = input("Enter Project Name: ")
                client = input("Enter Client Name: ")
                tech = input("Enter Technology: ")
                dur = int(input("Enter Duration (months): "))
                proj = add_project(pid, name, client, tech, dur)
                if proj:
                    print(f"Added Project: {proj}")

            elif choice == "7":
                for p in get_all_projects():
                    print_project(p)

            elif choice == "8":
                pid = input("Enter Project ID: ")
                name = input("New Name (or blank): ")
                client = input("New Client (or blank): ")
                tech = input("New Tech (or blank): ")
                dur_in = input("New Duration (or blank): ")
                dur = int(dur_in) if dur_in else None
                status = input("New Status (Active/Completed/Hold) (or blank): ")
                p = update_project(pid, name, client, tech, dur, status)
                print(f"Updated Project: {p}")

            elif choice == "9":
                pid = input("Enter Project ID: ")
                alloc_proj_ids = [a.project_id for a in allocations]
                p = delete_project(pid, alloc_proj_ids)
                print(f"Deleted Project: {p.project_name}")

            elif choice == "10":
                emp_id = int(input("Enter Employee ID: "))
                pid = input("Enter Project ID: ")
                role = input("Enter Role (Developer/Tester/Lead): ")
                perc = int(input("Enter Allocation % (25/50/75/100): "))
                alloc = allocate_employee(emp_id, pid, role, perc)
                print(f"Allocated: {alloc}")

            elif choice == "11":
                emp_id = int(input("Enter Employee ID: "))
                pid = input("Enter Project ID: ")
                removed = remove_allocation(emp_id, pid)
                print(f"Removed Allocation: {removed}")

            elif choice == "12":
                pid = input("Enter Project ID: ")
                report_project_wise(pid)

            elif choice == "13":
                emp_id = int(input("Enter Employee ID: "))
                report_employee_wise(emp_id)

            elif choice == "14":
                skill = input("Enter Skill: ")
                report_skill_wise(skill)

            elif choice == "15":
                exp = float(input("Enter Min Experience: "))
                for e in filter_by_experience(exp):
                    print_employee(e)

            elif choice == "16":
                report_sorted_salary()

            elif choice == "17":
                report_sorted_experience()

            elif choice == "18":
                report_available_employees()

            elif choice == "19":
                pid = input("Enter Project ID: ")
                report_project_wise(pid)

            elif choice == "20":
                export_employee_data()

            elif choice == "21":
                read_exported_report()

            else:
                print("Invalid option. Please try again.")

        except (ValueError, TypeError) as e:
            print(f"Input Error: {e}")
            logger.warning(f"Input Error: {e}")
        except (EmployeeNotFoundException, ProjectNotFoundException, InvalidAllocationException, EmployeeAlreadyAllocatedException) as e:
            print(f"Business Rule Error: {e}")
            logger.warning(f"Business Rule Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            logger.error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
