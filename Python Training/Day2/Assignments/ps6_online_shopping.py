customers = [
    {
        "CustomerId": 101,
        "CustomerName": "Rahul Sharma",
        "City": "Noida",
        "Orders": [
            {
                "ProductId": 1,
                "ProductName": "Laptop",
                "Quantity": 1,
                "Price": 65000
            },
            {
                "ProductId": 2,
                "ProductName": "Mouse",
                "Quantity": 2,
                "Price": 800
            }
        ]
    },
    {
        "CustomerId": 102,
        "CustomerName": "Priya Singh",
        "City": "Delhi",
        "Orders": [
            {
                "ProductId": 3,
                "ProductName": "Keyboard",
                "Quantity": 1,
                "Price": 2500
            }
        ]
    }
]

SearchCustomerByID = lambda cid, c_list: next((cust for cust in c_list if cust["CustomerId"] == cid), None)
SearchProductByID = lambda pid, orders: next((prod for prod in orders if prod["ProductId"] == pid), None)

def addCustomer():
    cid = int(input("Enter Customer ID : "))
    if SearchCustomerByID(cid, customers) != None:
        print("Customer ID already exists.")
    else:
        name = input("Enter Customer Name : ")
        city = input("Enter City : ")
        new_cust = {
            "CustomerId": cid,
            "CustomerName": name,
            "City": city,
            "Orders": []
        }
        customers.append(new_cust)
        print("Customer added successfully.")

def addOrder():
    cid = int(input("Enter Customer ID : "))
    cust = SearchCustomerByID(cid, customers)
    if cust == None:
        print("Customer not found.")
    else:
        pid = int(input("Enter Product ID : "))
        if SearchProductByID(pid, cust["Orders"]) != None:
            print("Product ID already exists for this customer.")
        else:
            pname = input("Enter Product Name : ")
            qty = int(input("Enter Quantity : "))
            price = float(input("Enter Price : "))
            order_item = {
                "ProductId": pid,
                "ProductName": pname,
                "Quantity": qty,
                "Price": price
            }
            cust["Orders"].append(order_item)
            print("Order added successfully.")

def displayCustomerDetails(cust):
    print(f"Customer ID   : {cust['CustomerId']}")
    print(f"Customer Name : {cust['CustomerName']}")
    print(f"City          : {cust['City']}")
    print("Orders:")
    if len(cust["Orders"]) == 0:
        print("  No orders found.")
    else:
        for item in cust["Orders"]:
            print(f"  Product ID   : {item['ProductId']}")
            print(f"  Product Name : {item['ProductName']}")
            print(f"  Quantity     : {item['Quantity']}")
            print(f"  Price        : {item['Price']}")

def viewAllCustomers():
    if len(customers) == 0:
        print("No customer records found.")
    else:
        for cust in customers:
            displayCustomerDetails(cust)
            print("----------------------------------------")

def searchCustomer():
    cid = int(input("Enter Customer ID : "))
    cust = SearchCustomerByID(cid, customers)
    if cust != None:
        displayCustomerDetails(cust)
    else:
        print("Customer not found.")

def updateProductQuantity():
    cid = int(input("Enter Customer ID : "))
    cust = SearchCustomerByID(cid, customers)
    if cust == None:
        print("Customer not found.")
    else:
        pid = int(input("Enter Product ID : "))
        prod = SearchProductByID(pid, cust["Orders"])
        if prod != None:
            new_qty = int(input("Enter New Quantity : "))
            prod["Quantity"] = new_qty
            print("Product quantity updated successfully.")
        else:
            print("Product not found.")

def removeProduct():
    cid = int(input("Enter Customer ID : "))
    cust = SearchCustomerByID(cid, customers)
    if cust == None:
        print("Customer not found.")
    else:
        pid = int(input("Enter Product ID : "))
        prod = SearchProductByID(pid, cust["Orders"])
        if prod != None:
            cust["Orders"].remove(prod)
            print("Product removed successfully.")
        else:
            print("Product not found.")

def calculateTotalOrderValue():
    cid = int(input("Enter Customer ID : "))
    cust = SearchCustomerByID(cid, customers)
    if cust == None:
        print("Customer not found.")
    else:
        if len(cust["Orders"]) == 0:
            print("No orders for this customer.")
        else:
            total_bill = 0
            for item in cust["Orders"]:
                item_total = item["Quantity"] * item["Price"]
                total_bill += item_total
                print(f"{item['ProductName']} : {item_total}")
            print("------------------------")
            print(f"Total Bill : {total_bill}")

def displayMaxOrderCustomer():
    if len(customers) == 0:
        print("No customers available.")
        return
    
    max_cust = None
    max_amount = -1
    for cust in customers:
        total = sum(item["Quantity"] * item["Price"] for item in cust["Orders"])
        if total > max_amount:
            max_amount = total
            max_cust = cust
            
    if max_cust != None:
        print("\nCustomer with Maximum Order Value:")
        print(f"Customer Name : {max_cust['CustomerName']}")
        print(f"Total Amount  : {max_amount}")

def main():
    while True:
        print("\n========== Online Shopping Order Management System ==========")
        print("1. Add New Customer")
        print("2. Add Product Order")
        print("3. View All Customers and Their Orders")
        print("4. Search Customer")
        print("5. Update Product Quantity")
        print("6. Remove a Product")
        print("7. Calculate Total Order Value")
        print("8. Display Customer with Maximum Order Value")
        print("9. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            addCustomer()
        elif ch == 2:
            addOrder()
        elif ch == 3:
            viewAllCustomers()
        elif ch == 4:
            searchCustomer()
        elif ch == 5:
            updateProductQuantity()
        elif ch == 6:
            removeProduct()
        elif ch == 7:
            calculateTotalOrderValue()
        elif ch == 8:
            displayMaxOrderCustomer()
        elif ch == 9:
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
