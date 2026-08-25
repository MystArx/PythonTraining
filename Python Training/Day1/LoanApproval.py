def LoanApproval(monthly_salary, credit_score, existing_loan_amount,employment_type):
    if monthly_salary > 80000 and credit_score > 750 and existing_loan_amount < 20000:
        return "Loan Approved"
    elif monthly_salary > 50000 and credit_score > 650 :
        return "Approve with Caution"
    elif credit_score<600:
        return "Under Manual REview"


monthly_salary=int(input("Enter monthly salary : "))
credit_score=int(input("Enter credit score : "))
existing_loan_amount=int(input("Enter existing loan amount : "))
employment_type=input("Enter employment type : ")
print(f"Loan Status : {LoanApproval(monthly_salary, credit_score, existing_loan_amount,employment_type)}")