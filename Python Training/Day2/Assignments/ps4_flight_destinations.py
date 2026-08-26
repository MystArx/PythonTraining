destinations = set()

SearchDestination = lambda dest, dest_set: dest in dest_set

def addDestination():
    dest = input("Enter destination name : ")
    if SearchDestination(dest, destinations):
        print(f"'{dest}' already exists in destinations.")
    else:
        destinations.add(dest)
        print("Destination added successfully.")

def removeDestination():
    dest = input("Enter destination name to remove : ")
    if SearchDestination(dest, destinations):
        destinations.remove(dest)
        print("Destination removed successfully.")
    else:
        print("Destination not found.")

def displayDestinations():
    if len(destinations) == 0:
        print("No flight destinations available.")
    else:
        print("\nAvailable Flight Destinations:")
        for dest in destinations:
            print(f"- {dest}")

def searchDestination():
    dest = input("Enter destination name to search : ")
    if SearchDestination(dest, destinations):
        print(f"'{dest}' is available.")
    else:
        print(f"'{dest}' is not available.")

def countDestinations():
    print(f"Total Unique Destinations : {len(destinations)}")

def main():
    while True:
        print("\n========== Flight Destination Management ==========")
        print("1. Add Destination")
        print("2. Remove Destination")
        print("3. Display Destinations")
        print("4. Search Destination")
        print("5. Count Destinations")
        print("6. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            addDestination()
        elif ch == 2:
            removeDestination()
        elif ch == 3:
            displayDestinations()
        elif ch == 4:
            searchDestination()
        elif ch == 5:
            countDestinations()
        elif ch == 6:
            print("Thank you for using Flight Destination Management System.")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
