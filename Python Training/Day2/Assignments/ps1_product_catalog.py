products = (
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Printer",
    "Webcam"
)

SearchProduct = lambda name, prod_tuple: name in prod_tuple

def displayProducts():
    print("\nAvailable Products:")
    for prod in products:
        print(prod)

def searchProduct():
    name = input("Enter Product Name : ")
    if SearchProduct(name, products):
        print(f"{name} is available in the catalog.")
    else:
        print(f"{name} is not available in the catalog.")

def displayTotalProducts():
    print(f"Total Products : {len(products)}")

def displayProductByPosition():
    pos = int(input("Enter Position : "))
    if 1 <= pos <= len(products):
        print(f"Product : {products[pos - 1]}")
    else:
        print("Invalid position.")

def main():
    while True:
        print("\n========== Product Catalog System ==========")
        print("1. Display All Products")
        print("2. Search a Product")
        print("3. Display Total Products")
        print("4. Display Product by Position")
        print("5. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            displayProducts()
        elif ch == 2:
            searchProduct()
        elif ch == 3:
            displayTotalProducts()
        elif ch == 4:
            displayProductByPosition()
        elif ch == 5:
            print("Thank you for using the Product Catalog System.")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
