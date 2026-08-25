def income_tax(annual_income, age):
    if age>=60:
        return 0
    elif annual_income<500000:
        return 1

    elif annual_income<=1000000:
        return 0.1

    elif annual_income<2000000:
        return 0.2

    else:
        return 0.3

def tax_deduction(annual_income,invested_amount):
    if invested_amount<=0.05*annual_income:
        return 0
    if invested_amount<=0.1*annual_income:
        return 0.1
    if invested_amount<=0.2*annual_income:
        return 0.2
    else:
        return 0.25


annual_income=int(input("Enter annual income : "))
age=int(input("Enter age : "))
invested_amount=int(input("Enter invested amount : "))
incometax=income_tax(annual_income, age)*annual_income
print(f"Tax Status : {incometax}")
print(f"Rebate : {incometax*tax_deduction(annual_income,invested_amount)}")