def CreateAccount():
    account_number=input("Enter account number : ")
    customer_name=input("Enter customer name : ")
    account_type=input("Enter account type : ")
    opening_balance=float(input("Enter opening balance : "))

    if opening_balance<0:
        print("INVALID INPUT!")
        opening_balance=0

    return account_number,customer_name,account_type,opening_balance


def DepositMoney(balance):
    amount=float(input("Enter deposit amount : "))

    if amount<0:
        print("INVALID DEPOSIT AMOUNT!")
        return balance

    balance=balance+amount
    print(f"Current balance : {balance}")
    return balance


def WithdrawMoney(balance):
    amount=float(input("Enter withdrawal amount : "))

    if amount<0:
        print("INVALID WITHDRAWAL AMOUNT!")
        return balance

    if amount>balance:
        print("INSUFFICIENT BALANCE!")
        return balance

    balance=balance-amount
    print(f"Current balance : {balance}")
    return balance


def CheckBalance(account_number,customer_name,account_type,balance):
    print(f"Account Number : {account_number}")
    print(f"Customer Name : {customer_name}")
    print(f"Account Type : {account_type}")
    print(f"Current Balance : {balance}")


def SavingsInterest(principle,rate,time):
    if rate<0:
        print("INVALID INTEREST RATE!")
        return 0,principle

    interest=(principle*rate*time)/100
    final_balance=principle+interest

    print(f"Interest Amount : {interest}")
    print(f"Final Balance : {final_balance}")

    return interest,final_balance


def LoanEMI(principle,annual_rate,tenure):
    if annual_rate<0:
        print("INVALID INTEREST RATE!")
        return 0,0,0

    if tenure<=0:
        print("INVALID LOAN TENURE!")
        return 0,0,0

    monthly_rate=annual_rate/(12*100)
    months=tenure*12

    if monthly_rate==0:
        emi=principle/months
    else:
        emi=(principle*monthly_rate*(1+monthly_rate)**months)/((1+monthly_rate)**months-1)

    total_amount=emi*months
    total_interest=total_amount-principle

    print(f"Monthly EMI : {emi}")
    print(f"Total Amount Payable : {total_amount}")
    print(f"Total Interest Paid : {total_interest}")

    return emi,total_amount,total_interest


def FixedDeposit(principle,rate,time):
    if rate<0:
        print("INVALID INTEREST RATE!")
        return 0,0

    if time<=0:
        print("INVALID DURATION!")
        return 0,0

    maturity=principle*(1+rate/100)**time
    interest=maturity-principle

    print(f"Interest Earned : {interest}")
    print(f"Maturity Amount : {maturity}")

    return interest,maturity


def MinimumBalancePenalty(balance):
    minimum_balance=10000

    if balance<minimum_balance:
        shortage=minimum_balance-balance
        penalty=shortage*2/100
        print(f"Shortage Amount : {shortage}")
        print(f"Penalty : {penalty}")
        return penalty

    print("No minimum balance penalty.")
    return 0


def ServiceCharges(transactions):
    if transactions<0:
        print("INVALID NUMBER OF TRANSACTIONS!")
        return 0

    if transactions<=5:
        charge=0
    else:
        charge=(transactions-5)*20

    print(f"Total Service Charge : {charge}")
    return charge


account_number=""
customer_name=""
account_type=""
balance=0
account_created=False

while True:
    choice=int(input("\nEnter choice :\n 1 : Create Account\n 2 : Deposit Money\n 3 : Withdraw Money\n 4 : Check Balance\n 5 : Calculate Savings Interest\n 6 : Calculate Loan EMI\n 7 : Calculate Fixed Deposit Maturity\n 8 : Calculate Minimum Balance Penalty\n 9 : Calculate Service Charges\n 10 : Exit\n"))

    if choice==1:
        account_number,customer_name,account_type,balance=CreateAccount()
        account_created=True
        print("Account created successfully.")

    elif choice==2:
        if account_created:
            balance=DepositMoney(balance)
        else:
            print("Please create an account first.")

    elif choice==3:
        if account_created:
            balance=WithdrawMoney(balance)
        else:
            print("Please create an account first.")

    elif choice==4:
        if account_created:
            CheckBalance(account_number,customer_name,account_type,balance)
        else:
            print("Please create an account first.")

    elif choice==5:
        principle=float(input("Enter principal amount : "))
        rate=float(input("Enter rate of interest : "))
        time=int(input("Enter time duration : "))
        SavingsInterest(principle,rate,time)

    elif choice==6:
        principle=float(input("Enter loan amount : "))
        rate=float(input("Enter annual interest rate : "))
        tenure=int(input("Enter loan tenure in years : "))
        LoanEMI(principle,rate,tenure)

    elif choice==7:
        principle=float(input("Enter FD amount : "))
        rate=float(input("Enter interest rate : "))
        time=int(input("Enter duration in years : "))
        FixedDeposit(principle,rate,time)

    elif choice==8:
        if account_created:
            MinimumBalancePenalty(balance)
        else:
            print("Please create an account first.")

    elif choice==9:
        transactions=int(input("Enter number of banking transactions : "))
        ServiceCharges(transactions)

    elif choice==10:
        print("Exiting")
        break

    else:
        print("Enter valid input!")
