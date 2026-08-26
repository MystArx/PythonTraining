account_types = (
    "Savings Account",
    "Current Account",
    "Fixed Deposit",
    "Recurring Deposit",
    "Salary Account",
    "NRI Account"
)

SearchAccountType = lambda acc_type, acc_tuple: acc_type in acc_tuple

def displayAllAccountTypes():
    print("\nAvailable Account Types:")
    for acc in account_types:
        print(acc)

def searchAccountType():
    acc_type = input("Enter Account Type : ")
    if SearchAccountType(acc_type, account_types):
        print(f"{acc_type} is available.")
    else:
        print(f"{acc_type} is not available.")

def displayTotalAccountTypes():
    print(f"Total Account Types : {len(account_types)}")

def displayAccountTypeByPosition():
    pos = int(input("Enter Position : "))
    if 1 <= pos <= len(account_types):
        print(f"Account Type : {account_types[pos - 1]}")
    else:
        print("Invalid position entered.")

def main():
    while True:
        print("\n========== Bank Account Types Management ==========")
        print("1. Display All Account Types")
        print("2. Search Account Type")
        print("3. Display Total Account Types")
        print("4. Display Account Type by Position")
        print("5. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            displayAllAccountTypes()
        elif ch == 2:
            searchAccountType()
        elif ch == 3:
            displayTotalAccountTypes()
        elif ch == 4:
            displayAccountTypeByPosition()
        elif ch == 5:
            print("Thank you for using Bank Account Types Management.")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
