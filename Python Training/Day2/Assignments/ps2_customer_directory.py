customer_directory = {
    1001: "Delhi",
    1002: "Mumbai",
    1003: "Bengaluru"
}

SearchByID = lambda cid, c_dir: c_dir.get(cid, None)

def addCustomer():
    cid = int(input("Enter Customer ID : "))
    if cid in customer_directory:
        print("Customer ID already exists.")
    else:
        city = input("Enter Customer City : ")
        customer_directory[cid] = city
        print("Customer added successfully.")

def viewAllCustomers():
    if len(customer_directory) == 0:
        print("No customer records found.")
    else:
        for cid, city in customer_directory.items():
            print(f"Customer ID : {cid}")
            print(f"City        : {city}")

def searchCustomer():
    cid = int(input("Enter Customer ID : "))
    city = SearchByID(cid, customer_directory)
    if city != None:
        print(f"Customer City : {city}")
    else:
        print("Customer not found.")

def main():
    while True:
        print("\n========== Customer City Directory ==========")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            addCustomer()
        elif ch == 2:
            viewAllCustomers()
        elif ch == 3:
            searchCustomer()
        elif ch == 4:
            print("Thank you for using the Customer City Directory.")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
