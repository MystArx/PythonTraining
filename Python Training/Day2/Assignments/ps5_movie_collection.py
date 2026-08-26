movies = {
    101: "3 Idiots",
    102: "Inception",
    103: "Interstellar"
}

SearchByID = lambda mid, m_dict: m_dict.get(mid, None)

def addMovie():
    mid = int(input("Enter Movie ID : "))
    if SearchByID(mid, movies) != None:
        print("Movie ID already exists.")
    else:
        name = input("Enter Movie Name : ")
        movies[mid] = name
        print("Movie added successfully.")

def viewAllMovies():
    if len(movies) == 0:
        print("No movies found.")
    else:
        for mid, name in movies.items():
            print(f"Movie ID   : {mid}")
            print(f"Movie Name : {name}")

def searchMovie():
    mid = int(input("Enter Movie ID : "))
    name = SearchByID(mid, movies)
    if name != None:
        print(f"Movie Name : {name}")
    else:
        print("Movie not found.")

def updateMovie():
    mid = int(input("Enter Movie ID : "))
    if SearchByID(mid, movies) != None:
        new_name = input("Enter New Movie Name : ")
        movies[mid] = new_name
        print("Movie updated successfully.")
    else:
        print("Movie not found.")

def deleteMovie():
    mid = int(input("Enter Movie ID : "))
    if SearchByID(mid, movies) != None:
        del movies[mid]
        print("Movie deleted successfully.")
    else:
        print("Movie not found.")

def main():
    while True:
        print("\n========== Movie Collection Management System ==========")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            addMovie()
        elif ch == 2:
            viewAllMovies()
        elif ch == 3:
            searchMovie()
        elif ch == 4:
            updateMovie()
        elif ch == 5:
            deleteMovie()
        elif ch == 6:
            print("Exiting")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
