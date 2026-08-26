astronauts = [
    (201, "Neil", "NASA", ["Artemis I", "Lunar Research"]),
    (202, "Rakesh", "ISRO", ["Gaganyaan", "Orbital Training"]),
    (203, "Emma", "ESA", ["Mars Explorer", "Moon Base", "Deep Space Research"])
]

SearchByID = lambda aid, a_list: next((astro for astro in a_list if astro[0] == aid), None)

def registerAstronaut():
    aid = int(input("Enter Astronaut ID : "))
    if SearchByID(aid, astronauts) != None:
        print("Astronaut ID already exists.")
        return
    name = input("Enter Astronaut Name : ")
    agency = input("Enter Space Agency : ")
    num_missions = int(input("Enter Number of Missions : "))
    mission_list = []
    for i in range(num_missions):
        m_name = input(f"Enter Mission {i + 1} Name : ")
        mission_list.append(m_name)
    
    astro_tuple = (aid, name, agency, mission_list)
    astronauts.append(astro_tuple)
    print("Astronaut registered successfully.")

def displayAstronautDetails(astro):
    print(f"Astronaut ID : {astro[0]}")
    print(f"Name         : {astro[1]}")
    print(f"Agency       : {astro[2]}")
    print(f"Missions     : {', '.join(astro[3]) if astro[3] else 'None'}")

def viewAllAstronauts():
    if len(astronauts) == 0:
        print("No astronaut records found.")
    else:
        for astro in astronauts:
            displayAstronautDetails(astro)
            print("--------------------------------------------")

def assignNewMission():
    aid = int(input("Enter Astronaut ID : "))
    astro = SearchByID(aid, astronauts)
    if astro == None:
        print("Astronaut not found.")
    else:
        new_mission = input("Enter New Mission Name : ")
        if new_mission in astro[3]:
            print("Mission already assigned.")
        else:
            astro[3].append(new_mission)
            print("New mission assigned successfully.")

def completeMission():
    aid = int(input("Enter Astronaut ID : "))
    astro = SearchByID(aid, astronauts)
    if astro == None:
        print("Astronaut not found.")
    else:
        m_name = input("Enter Mission Name to complete/remove : ")
        if m_name in astro[3]:
            astro[3].remove(m_name)
            print("Mission removed successfully.")
        else:
            print("Mission not found in astronaut's mission list.")

def searchAstronaut():
    aid = int(input("Enter Astronaut ID : "))
    astro = SearchByID(aid, astronauts)
    if astro != None:
        displayAstronautDetails(astro)
    else:
        print("Astronaut not found.")

def displayExperiencedAstronauts():
    exp_astros = [astro for astro in astronauts if len(astro[3]) >= 3]
    if len(exp_astros) == 0:
        print("No experienced astronauts (with 3 or more missions) found.")
    else:
        print("\nExperienced Astronauts:")
        for astro in exp_astros:
            print(astro[1])
            print(f"Agency         : {astro[2]}")
            print(f"Total Missions : {len(astro[3])}")
            print("--------------------------------------------")

def displayAgencyWiseCount():
    agency_counts = {}
    for astro in astronauts:
        agency = astro[2]
        agency_counts[agency] = agency_counts.get(agency, 0) + 1
        
    if len(agency_counts) == 0:
        print("No astronauts found.")
    else:
        print("\nSpace Agency-wise Astronaut Count:")
        for agency, count in agency_counts.items():
            print(f"{agency:<10} : {count}")

def main():
    while True:
        print("\n========== Astronaut Mission Management System ==========")
        print("1. Register a New Astronaut")
        print("2. View All Astronauts")
        print("3. Assign a New Mission")
        print("4. Complete (Remove) a Mission")
        print("5. Search an Astronaut")
        print("6. Display Experienced Astronauts")
        print("7. Display Space Agency-wise Astronaut Count")
        print("8. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            registerAstronaut()
        elif ch == 2:
            viewAllAstronauts()
        elif ch == 3:
            assignNewMission()
        elif ch == 4:
            completeMission()
        elif ch == 5:
            searchAstronaut()
        elif ch == 6:
            displayExperiencedAstronauts()
        elif ch == 7:
            displayAgencyWiseCount()
        elif ch == 8:
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()