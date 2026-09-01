from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import SessionLocal
from models import Employee
from logger_config import logger
from exceptions import EmployeeNotFoundException
from utils import (
    get_required_text,
    get_positive_integer,
    get_non_negative_integer,
    get_positive_float,
    get_valid_status
)


def add_employee():
    session = SessionLocal()
    try:
        print("\n--- Add New Employee ---")

        emp_name = get_required_text("Enter Employee Name: ")
        emp_email = get_required_text("Enter Employee Email: ")

        query = select(Employee).where(Employee.employee_email == emp_email)
        if session.scalars(query).first() is not None:
            print(f"Error: An employee with email '{emp_email}' already exists.")
            logger.warning(f"Duplicate email '{emp_email}'")
            return

        emp_experience = get_non_negative_integer("Enter Experience (in Years): ")
        emp_skill = get_required_text("Enter Primary Skill: ")
        emp_salary = get_positive_float("Enter Salary: ")
        emp_status = get_valid_status("Enter Status", ["Available", "Allocated"])

        employee = Employee(
            employee_name=emp_name,
            employee_email=emp_email,
            employee_experience=emp_experience,
            employee_skill=emp_skill,
            employee_salary=emp_salary,
            employee_status=emp_status
        )

        session.add(employee)
        session.commit()

        print(f"\nEmployee added successfully! ID: {employee.employee_id}")
        logger.info(f"Employee {employee.employee_id} created")

    except IntegrityError as error:
        session.rollback()
        print(f"Database Integrity Error: {error}")
        logger.error(f"IntegrityError: {error}")

    except SQLAlchemyError as error:
        session.rollback()
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    except Exception as error:
        session.rollback()
        print(f"Unexpected error: {error}")
        logger.error(f"Unexpected error: {error}")

    finally:
        session.close()


def view_all_employees():
    session = SessionLocal()
    try:
        query = select(Employee).order_by(Employee.employee_id)
        employees = session.scalars(query).all()

        if not employees:
            print("\nNo employees found.")
            return

        print("\n" + "=" * 95)
        print(f"{'ID':<6} {'Name':<22} {'Email':<25} {'Skill':<15} {'Exp':<10} {'Salary':<10} {'Status':<10}")
        print("=" * 95)

        for emp in employees:
            print(f"{emp.employee_id:<6} {emp.employee_name:<22} {emp.employee_email:<25} {emp.employee_skill:<15} {emp.employee_experience:<10} {emp.employee_salary:<10.2f} {emp.employee_status:<10}")

        print("=" * 95)

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def search_employee():
    session = SessionLocal()
    try:
        print("\n--- Search Employee ---")
        print("1. Search by Employee ID")
        print("2. Search by Employee Name")
        print("3. Search by Skill")

        choice = input("Enter search option (1-3): ").strip()
        employees = []

        if choice == "1":
            emp_id = get_positive_integer("Enter Employee ID: ")
            employee = session.get(Employee, emp_id)

            if employee:
                employees.append(employee)

        elif choice == "2":
            name = get_required_text("Enter Employee Name: ")
            query = select(Employee).where(
                Employee.employee_name.ilike(f"%{name}%")
            )
            employees = session.scalars(query).all()

        elif choice == "3":
            skill = get_required_text("Enter Skill: ")
            query = select(Employee).where(
                Employee.employee_skill.ilike(f"%{skill}%")
            )
            employees = session.scalars(query).all()

        else:
            print("Invalid search choice.")
            return

        if not employees:
            print("\nNo matching employees found.")
            return

        print("\nEmployees Found:")
        print("-" * 95)

        for emp in employees:
            print(
                f"ID: {emp.employee_id} | "
                f"Name: {emp.employee_name} | "
                f"Email: {emp.employee_email} | "
                f"Skill: {emp.employee_skill} | "
                f"Experience: {emp.employee_experience} | "
                f"Salary: {emp.employee_salary:.2f} | "
                f"Status: {emp.employee_status}"
            )

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def update_employee():
    session = SessionLocal()
    try:
        print("\n--- Update Employee ---")

        emp_id = get_positive_integer("Enter Employee ID to update: ")
        employee = session.get(Employee, emp_id)

        if employee is None:
            raise EmployeeNotFoundException(
                f"Employee with ID {emp_id} does not exist."
            )

        print(f"\nEmployee: {employee.employee_name}")
        print("1. Update Skill")
        print("2. Update Experience")
        print("3. Update Salary")
        print("4. Update Status")
        print("5. Update All Details")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            employee.employee_skill = get_required_text("Enter New Skill: ")

        elif choice == "2":
            employee.employee_experience = get_non_negative_integer(
                "Enter New Experience: "
            )

        elif choice == "3":
            employee.employee_salary = get_positive_float(
                "Enter New Salary: "
            )

        elif choice == "4":
            employee.employee_status = get_valid_status(
                "Enter New Status",
                ["Available", "Allocated"]
            )

        elif choice == "5":
            employee.employee_skill = get_required_text("Enter New Skill: ")
            employee.employee_experience = get_non_negative_integer(
                "Enter New Experience: "
            )
            employee.employee_salary = get_positive_float(
                "Enter New Salary: "
            )
            employee.employee_status = get_valid_status(
                "Enter New Status",
                ["Available", "Allocated"]
            )

        else:
            print("Invalid choice.")
            return

        session.commit()

        print(f"\nEmployee ID {emp_id} updated successfully!")
        logger.info(f"Employee {emp_id} updated")

    except EmployeeNotFoundException as error:
        print(f"Error: {error}")

    except SQLAlchemyError as error:
        session.rollback()
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def delete_employee():
    session = SessionLocal()
    try:
        print("\n--- Delete Employee ---")

        emp_id = get_positive_integer("Enter Employee ID to delete: ")
        employee = session.get(Employee, emp_id)

        if employee is None:
            raise EmployeeNotFoundException(
                f"Employee with ID {emp_id} does not exist."
            )

        if employee.allocations:
            print(f"\nEmployee is allocated to {len(employee.allocations)} project(s).")

            for alloc in employee.allocations:
                print(
                    f"Project: {alloc.project_id} | "
                    f"Role: {alloc.role} | "
                    f"Allocation: {alloc.allocation_percentage}%"
                )

            confirm = input(
                "Delete employee and all allocations? (y/n): "
            ).strip().lower()

            if confirm != "y":
                print("Employee deletion cancelled.")
                return

        session.delete(employee)
        session.commit()

        print(f"\nEmployee ID {emp_id} deleted successfully.")
        logger.info(f"Employee {emp_id} deleted")

    except EmployeeNotFoundException as error:
        print(f"Error: {error}")

    except SQLAlchemyError as error:
        session.rollback()
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def filter_employees_by_skill():
    session = SessionLocal()
    try:
        skill = get_required_text("\nEnter Skill to filter by: ")

        query = select(Employee).where(
            Employee.employee_skill.ilike(f"%{skill}%")
        )

        employees = session.scalars(query).all()

        if not employees:
            print(f"No employees found with skill '{skill}'.")
            return

        print(f"\nEmployees with skill '{skill}':")

        for emp in employees:
            print(
                f"ID: {emp.employee_id} | "
                f"Name: {emp.employee_name} | "
                f"Skill: {emp.employee_skill} | "
                f"Experience: {emp.employee_experience} | "
                f"Salary: {emp.employee_salary:.2f}"
            )

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def filter_employees_by_experience():
    session = SessionLocal()
    try:
        min_exp = get_non_negative_integer(
            "\nEnter minimum experience (in years): "
        )

        employees = session.scalars(select(Employee)).all()

        filtered = list(
            filter(
                lambda emp: emp.employee_experience >= min_exp,
                employees
            )
        )

        if not filtered:
            print(f"No employees found with at least {min_exp} years.")
            return

        print(f"\nEmployees with >= {min_exp} years experience:")

        for emp in filtered:
            print(
                f"ID: {emp.employee_id} | "
                f"Name: {emp.employee_name} | "
                f"Experience: {emp.employee_experience}"
            )

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def sort_employees_by_salary():
    session = SessionLocal()
    try:
        employees = session.scalars(select(Employee)).all()

        if not employees:
            print("\nNo employees to sort.")
            return

        print("\n1. Low to High")
        print("2. High to Low")

        choice = input("Enter choice: ").strip()

        if choice == "2":
            employees = sorted(
                employees,
                key=lambda emp: emp.employee_salary,
                reverse=True
            )
            order = "High to Low"
        else:
            employees = sorted(
                employees,
                key=lambda emp: emp.employee_salary
            )
            order = "Low to High"

        print(f"\nEmployees Sorted by Salary ({order}):")

        for emp in employees:
            print(
                f"ID: {emp.employee_id} | "
                f"Name: {emp.employee_name} | "
                f"Salary: {emp.employee_salary:.2f}"
            )

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def sort_employees_by_experience():
    session = SessionLocal()
    try:
        employees = session.scalars(select(Employee)).all()

        if not employees:
            print("\nNo employees to sort.")
            return

        print("\n1. Low to High")
        print("2. High to Low")

        choice = input("Enter choice: ").strip()

        if choice == "2":
            employees = sorted(
                employees,
                key=lambda emp: emp.employee_experience,
                reverse=True
            )
            order = "High to Low"
        else:
            employees = sorted(
                employees,
                key=lambda emp: emp.employee_experience
            )
            order = "Low to High"

        print(f"\nEmployees Sorted by Experience ({order}):")

        for emp in employees:
            print(
                f"ID: {emp.employee_id} | "
                f"Name: {emp.employee_name} | "
                f"Experience: {emp.employee_experience}"
            )

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()


def show_available_employees():
    session = SessionLocal()
    try:
        query = select(Employee).where(
            Employee.employee_status == "Available"
        ).order_by(Employee.employee_id)

        employees = session.scalars(query).all()

        if not employees:
            print("\nNo available employees found.")
            return

        print("\n--- Available Employees ---")

        for emp in employees:
            print(
                f"ID: {emp.employee_id} | "
                f"Name: {emp.employee_name} | "
                f"Skill: {emp.employee_skill} | "
                f"Experience: {emp.employee_experience} | "
                f"Salary: {emp.employee_salary:.2f} | "
                f"Status: {emp.employee_status}"
            )

    except SQLAlchemyError as error:
        print(f"Database error: {error}")
        logger.error(f"SQLAlchemyError: {error}")

    finally:
        session.close()