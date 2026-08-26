# Payroll Calculation Rules
1.	House Rent Allowance (HRA)
HRA = 20% of Basic Salary 

2.	Dearness Allowance (DA)
DA = 10% of Basic Salary 

3.	Overtime Payment
Overtime payment = Overtime Hours × ₹500 

4.	Leave Deduction
Two leave days are allowed without deduction.
For every additional leave day, deduct ₹1,000. 

5.	Provident Fund Deduction (PF)
PF = 12% of Basic Salary 

6.	Professional Tax 
o	Gross Salary up to ₹30,000: ₹200 
o	Gross Salary from ₹30,001 to ₹60,000: ₹500 
o	Gross Salary above ₹60,000: ₹1,000 


# Salary Formulas
Gross Salary = Basic Salary + HRA + DA + Overtime Payment

Total Deduction = PF + Professional Tax + Leave Deduction

Net Salary = Gross Salary - Total Deduction

# Functions to Create

## def get_employee_details():
Accept and return employee information.

## def calculate_hra(basic_salary):
Calculate HRA.

## def calculate_da(basic_salary):
Calculate DA.

## def calculate_overtime(overtime_hours):
Calculate overtime payment.

## def calculate_leave_deduction(leave_days):
Calculate deduction for additional leave days.

## def calculate_pf(basic_salary):
Calculate PF deduction.

## def calculate_professional_tax(gross_salary):
Calculate professional tax using if, elif, and else.

## def calculate_payroll(employee):
Calculate gross salary, deductions, and net salary.

## def display_salary_slip(employee, payroll):
Display the complete salary slip.


# Menu Operations
1. Enter Employee Details
2. Calculate Monthly Payroll
3. Display Salary Slip
4. Calculate Annual Net Salary
5. Exit



# Sample Salary Slip
----------------------------------------
          EMPLOYEE SALARY SLIP
----------------------------------------
Employee ID       : EMP101
Employee Name     : Rahul Sharma
Basic Salary      : ₹40,000.00
HRA               : ₹8,000.00
DA                : ₹4,000.00
Overtime Payment  : ₹2,500.00
Gross Salary      : ₹54,500.00
PF Deduction      : ₹4,800.00
Professional Tax  : ₹500.00
Leave Deduction   : ₹1,000.00
Total Deduction   : ₹6,300.00
Net Salary        : ₹48,200.00
----------------------------------------


# Validation Requirements
The program should ensure that:
•	Employee ID and name cannot be empty. 
•	Basic salary must be greater than zero. 
•	Overtime hours cannot be negative. 
•	Leave days cannot be negative. 
•	Payroll cannot be displayed before employee details are entered. 
•	Annual salary should be calculated as: 
Annual Net Salary = Monthly Net Salary × 12