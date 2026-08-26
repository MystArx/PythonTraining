book_set = set()

SearchBook = lambda title, b_set: title in b_set

def addBook():
    title = input("Enter book title : ")
    if SearchBook(title, book_set):
        print(f"'{title}' already exists in the collection.")
    else:
        book_set.add(title)
        print("Book added successfully.")

def removeBook():
    title = input("Enter book title to remove : ")
    if SearchBook(title, book_set):
        book_set.remove(title)
        print("Book removed successfully.")
    else:
        print("Book not found.")

def displayBooks():
    if len(book_set) == 0:
        print("No books available in the library.")
    else:
        print("\nAvailable Books:")
        for book in book_set:
            print(f"- {book}")

def searchBook():
    title = input("Enter book title to search : ")
    if SearchBook(title, book_set):
        print(f"'{title}' is available in the library.")
    else:
        print(f"'{title}' is not available in the library.")

def main():
    while True:
        print("\n========== Library Book Collection ==========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Search Book")
        print("5. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            addBook()
        elif ch == 2:
            removeBook()
        elif ch == 3:
            displayBooks()
        elif ch == 4:
            searchBook()
        elif ch == 5:
            print("Thank you for using the Library Book Collection Management System.")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
