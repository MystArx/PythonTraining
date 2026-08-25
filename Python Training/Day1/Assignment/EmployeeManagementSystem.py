def CreateEmployee():
    employee_id=input("Enter employee ID : ")
    employee_name=input("Enter employee name : ")
    department=input("Enter department : ")
    designation=input("Enter designation : ")
    basic_salary=float(input("Enter basic salary : "))
    experience=float(input("Enter years of experience : "))

    if basic_salary<0:
        print("INVALID SALARY!")
        basic_salary=0

    if experience<0:
        print("INVALID EXPERIENCE!")
        experience=0

    return employee_id,employee_name,department,designation,basic_salary,experience


def GrossSalary(basic_salary):
    hra=basic_salary*20/100
    da=basic_salary*10/100
    special_allowance=basic_salary*5/100

    gross_salary=basic_salary+hra+da+special_allowance

    print(f"HRA : {hra}")
    print(f"DA : {da}")
    print(f"Special Allowance : {special_allowance}")
    print(f"Gross Salary : {gross_salary}")

    return gross_salary


def SalaryDeductions(basic_salary,gross_salary):
    pf=basic_salary*12/100
    professional_tax=200

    if gross_salary>50000:
        income_tax=gross_salary*5/100
    else:
        income_tax=0

    total_deductions=pf+professional_tax+income_tax

    print(f"PF : {pf}")
    print(f"Professional Tax : {professional_tax}")
    print(f"Income Tax : {income_tax}")
    print(f"Total Deductions : {total_deductions}")

    return total_deductions


def NetSalary(gross_salary,total_deductions):
    net_salary=gross_salary-total_deductions
    print(f"Net Salary : {net_salary}")
    return net_salary


def AnnualSalary(net_salary):
    annual_salary=net_salary*12
    print(f"Annual Salary : {annual_salary}")
    return annual_salary


def PerformanceBonus(basic_salary,rating):
    if rating<1 or rating>5:
        print("INVALID PERFORMANCE RATING!")
        return 0

    if rating==5:
        bonus=basic_salary*15/100
    elif rating==4:
        bonus=basic_salary*10/100
    elif rating==3:
        bonus=basic_salary*5/100
    else:
        bonus=0

    salary_after_bonus=basic_salary+bonus

    print(f"Performance Bonus : {bonus}")
    print(f"Salary After Bonus : {salary_after_bonus}")

    return bonus


def SalaryIncrement(basic_salary,experience):
    if experience<0:
        print("INVALID EXPERIENCE!")
        return 0,0

    if experience<2:
        increment=basic_salary*5/100
    elif experience<=5:
        increment=basic_salary*10/100
    else:
        increment=basic_salary*15/100

    revised_salary=basic_salary+increment

    print(f"Increment Amount : {increment}")
    print(f"Revised Basic Salary : {revised_salary}")

    return increment,revised_salary


def OvertimePayment(hours):
    if hours<0:
        print("INVALID OVERTIME HOURS!")
        return 0

    if hours<=10:
        payment=hours*500
    else:
        payment=(10*500)+((hours-10)*750)

    print(f"Overtime Payment : {payment}")
    return payment


def LeaveDeduction(basic_salary,leave_days):
    if leave_days<0:
        print("INVALID LEAVE DAYS!")
        return 0

    per_day_salary=basic_salary/30
    deduction=per_day_salary*leave_days
    salary_after_deduction=basic_salary-deduction

    print(f"Per Day Salary : {per_day_salary}")
    print(f"Leave Deduction : {deduction}")
    print(f"Salary After Deduction : {salary_after_deduction}")

    return deduction


def EmployeeSummary(employee_id,employee_name,department,designation,basic_salary,gross_salary,total_deductions,net_salary):
    print(f"Employee ID : {employee_id}")
    print(f"Employee Name : {employee_name}")
    print(f"Department : {department}")
    print(f"Designation : {designation}")
    print(f"Basic Salary : {basic_salary}")
    print(f"Gross Salary : {gross_salary}")
    print(f"Total Deductions : {total_deductions}")
    print(f"Net Salary : {net_salary}")


employee_id=""
employee_name=""
department=""
designation=""
basic_salary=0
experience=0
gross_salary=0
total_deductions=0
net_salary=0
employee_created=False

while True:
    choice=int(input("\nEnter choice :\n 1 : Create Employee Profile\n 2 : Calculate Gross Salary\n 3 : Calculate Salary Deductions\n 4 : Calculate Net Salary\n 5 : Calculate Annual Salary\n 6 : Calculate Performance Bonus\n 7 : Calculate Salary Increment\n 8 : Calculate Overtime Payment\n 9 : Calculate Leave Deduction\n 10 : Display Employee Salary Summary\n 11 : Exit\n"))

    if choice==1:
        employee_id,employee_name,department,designation,basic_salary,experience=CreateEmployee()
        employee_created=True
        gross_salary=0
        total_deductions=0
        net_salary=0
        print("Employee profile created successfully.")

    elif choice==2:
        if employee_created:
            gross_salary=GrossSalary(basic_salary)
        else:
            print("Please create an employee profile first.")

    elif choice==3:
        if employee_created:
            if gross_salary==0:
                gross_salary=GrossSalary(basic_salary)
            total_deductions=SalaryDeductions(basic_salary,gross_salary)
        else:
            print("Please create an employee profile first.")

    elif choice==4:
        if employee_created:
            if gross_salary==0:
                gross_salary=GrossSalary(basic_salary)
            if total_deductions==0:
                total_deductions=SalaryDeductions(basic_salary,gross_salary)
            net_salary=NetSalary(gross_salary,total_deductions)
        else:
            print("Please create an employee profile first.")

    elif choice==5:
        if employee_created:
            if net_salary==0:
                if gross_salary==0:
                    gross_salary=GrossSalary(basic_salary)
                if total_deductions==0:
                    total_deductions=SalaryDeductions(basic_salary,gross_salary)
                net_salary=NetSalary(gross_salary,total_deductions)
            AnnualSalary(net_salary)
        else:
            print("Please create an employee profile first.")

    elif choice==6:
        if employee_created:
            rating=int(input("Enter performance rating from 1 to 5 : "))
            PerformanceBonus(basic_salary,rating)
        else:
            print("Please create an employee profile first.")

    elif choice==7:
        if employee_created:
            SalaryIncrement(basic_salary,experience)
        else:
            print("Please create an employee profile first.")

    elif choice==8:
        if employee_created:
            hours=float(input("Enter overtime hours worked : "))
            OvertimePayment(hours)
        else:
            print("Please create an employee profile first.")

    elif choice==9:
        if employee_created:
            leave_days=float(input("Enter number of unpaid leave days : "))
            LeaveDeduction(basic_salary,leave_days)
        else:
            print("Please create an employee profile first.")

    elif choice==10:
        if employee_created:
            if gross_salary==0:
                gross_salary=GrossSalary(basic_salary)
            if total_deductions==0:
                total_deductions=SalaryDeductions(basic_salary,gross_salary)
            if net_salary==0:
                net_salary=NetSalary(gross_salary,total_deductions)
            EmployeeSummary(employee_id,employee_name,department,designation,basic_salary,gross_salary,total_deductions,net_salary)
        else:
            print("Please create an employee profile first.")

    elif choice==11:
        print("Exiting")
        break

    else:
        print("Enter valid input!")
