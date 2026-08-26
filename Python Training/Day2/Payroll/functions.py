from classes import Employee
employee_list=[]
def get_employee_details():
    employee_id=input("Enter employee ID : ")
    employee_name=input("Enter employee name : ")
    department=input("Enter department : ")
    designation=input("Enter designation : ")
    basic_salary=float(input("Enter basic salary : "))
    experience=float(input("Enter years of experience : "))

    employee = Employee(employee_id, employee_name, department, designation, basic_salary, experience)
    employee_list.append(employee)
    if basic_salary<0:
        print("INVALID SALARY!")
        basic_salary=0

    if experience<0:
        print("INVALID EXPERIENCE!")
        experience=0

    return employee


def calculate_hra(basic_salary):
    return 0.2*basic_salary



def calculate_da(basic_salary):
    return 0.1*basic_salary


def calculate_overtime(overtime_hours):
    return 500 * overtime_hours


def calculate_leave_deduction(leave_days):
    if leave_days<=2:
        return 0
    else:
        return (1000* (leave_days-2))

def calculate_pf(basic_salary):
    return 0.12*basic_salary

def calculate_professional_tax(gross_salary):
    if gross_salary<=30000:
        return 200
    elif gross_salary<=60000:
        return 500
    else:
        return 1000


def calculate_payroll(employee,leaves,overtime_hours):
    hra = calculate_hra(employee.basic_salary)
    da = calculate_da(employee.basic_salary)
    gross_salary = employee.basic_salary + hra + da
    overtime_payment=calculate_overtime(overtime_hours)
    pf = calculate_pf(employee.basic_salary)
    professional_tax = calculate_professional_tax(gross_salary)
    leave_deduction = calculate_leave_deduction(leaves) 
    total_deductions = pf + professional_tax +leave_deduction

    net_salary = gross_salary - total_deductions

    payroll = {
        "Basic Salary": employee.basic_salary,
        "HRA": hra,
        "DA": da,
        "Overtime Payment": overtime_payment,
        "Gross Salary": gross_salary,
        "PF Deduction": pf,
        "Professional Tax": professional_tax,
        "Leave Deduction" : leave_deduction,
        "Total Deductions": total_deductions,
        "Net Salary": net_salary
    }

    return payroll


def display_salary_slip(employee, payroll):
    print("       -------------------------")
    print("         EMPLOYEE SALARY SLIP")
    print("       -------------------------")

    for key,value in payroll.items():
        print(f"{key} : {value}")

def calculate_annual_salary(employee):
    pass