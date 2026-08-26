import functions as f



while True:
    ch=int(input("""1. Enter Employee Details
2. Calculate Monthly Payroll
3. Display Salary Slip
4. Calculate Annual Net Salary
5. Exit
"""))

    if ch==1:
        f.get_employee_details()

    if ch==2:
        leaves=int(input("Enter leaves : "))
        overtime_hours=int(input("Enter overtime hours : "))
        f.calculate_payroll(f.employee_list[0],leaves,overtime_hours)
    if ch==3:
        leaves=int(input("Enter leaves : "))
        overtime_hours=int(input("Enter overtime hours : "))
        f.display_salary_slip(f.employee_list[0],f.calculate_payroll(f.employee_list[0],leaves,overtime_hours))

    if ch==4:
        f.calculate_annual_salary(f.employee_list[0])

    if ch==5:
        print(" EXITING ")
        break