from db_connection import LocalSession, engine
from models import Base, Employee, Project

def seed_data(reset: bool = True):
    if reset:
        print("Dropping existing tables for Many-to-Many schema update...")
        Base.metadata.drop_all(bind=engine)

    print("Creating new Many-to-Many tables...")
    Base.metadata.create_all(bind=engine)

    session = LocalSession()
    try:
        if session.query(Employee).count() > 0:
            print("Database already populated!")
            return

        print("Seeding sample Employees and Projects into Many-to-Many database...")

        # 1. Create Employees
        emp1 = Employee(employee_name="Amit Sharma", employee_email="amit.sharma@example.com", employee_department="Engineering", employee_salary=85000)
        emp2 = Employee(employee_name="Priya Verma", employee_email="priya.verma@example.com", employee_department="Product", employee_salary=92000)
        emp3 = Employee(employee_name="Rohan Gupta", employee_email="rohan.gupta@example.com", employee_department="DevOps", employee_salary=78000)
        emp4 = Employee(employee_name="Sneha Reddy", employee_email="sneha.reddy@example.com", employee_department="Data Science", employee_salary=95000)
        emp5 = Employee(employee_name="Vikram Singh", employee_email="vikram.singh@example.com", employee_department="QA Engineering", employee_salary=68000)

        session.add_all([emp1, emp2, emp3, emp4, emp5])
        session.commit()

        # 2. Create Projects
        proj1 = Project(project_name="E-Commerce Portal", project_description="Next.js and FastAPI microservices platform", project_status="Active")
        proj2 = Project(project_name="Mobile Banking App", project_description="iOS and Android React Native app", project_status="Active")
        proj3 = Project(project_name="CI/CD Pipeline Automation", project_description="Automated Kubernetes deployment pipelines", project_status="Active")
        proj4 = Project(project_name="Customer Churn Prediction", project_description="Machine learning churn prediction model", project_status="Active")

        session.add_all([proj1, proj2, proj3, proj4])
        session.commit()

        # 3. Associate Employees to Projects (Many-to-Many!)
        # Project 1 (E-Commerce Portal): Amit, Priya, Rohan
        proj1.employees.extend([emp1, emp2, emp3])

        # Project 2 (Mobile Banking App): Amit, Priya, Vikram
        proj2.employees.extend([emp1, emp2, emp5])

        # Project 3 (CI/CD Pipeline Automation): Rohan, Vikram
        proj3.employees.extend([emp3, emp5])

        # Project 4 (Customer Churn Prediction): Sneha, Amit
        proj4.employees.extend([emp4, emp1])

        session.commit()

        print(f"Successfully seeded database!")
        print(f"Total Employees: {session.query(Employee).count()}")
        print(f"Total Projects: {session.query(Project).count()}")
    except Exception as e:
        session.rollback()
        print("Error seeding data:", e)
    finally:
        session.close()

if __name__ == "__main__":
    seed_data(reset=True)
