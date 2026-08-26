players = [
    (
        101,
        "Virat Kohli",
        "India",
        {
            "Matches": 295,
            "Runs": 14181,
            "Centuries": 51,
            "HalfCenturies": 74
        }
    ),
    (
        102,
        "Joe Root",
        "England",
        {
            "Matches": 180,
            "Runs": 13500,
            "Centuries": 36,
            "HalfCenturies": 62
        }
    ),
    (
        103,
        "Steve Smith",
        "Australia",
        {
            "Matches": 170,
            "Runs": 11250,
            "Centuries": 34,
            "HalfCenturies": 45
        }
    )
]

SearchByID = lambda pid, p_list: next((p for p in p_list if p[0] == pid), None)

def registerPlayer():
    pid = int(input("Enter Player ID : "))
    if SearchByID(pid, players) != None:
        print("Player ID already exists.")
        return
    name = input("Enter Player Name : ")
    team = input("Enter Team Name : ")
    matches = int(input("Enter Matches Played : "))
    runs = int(input("Enter Total Runs : "))
    centuries = int(input("Enter Centuries : "))
    half_centuries = int(input("Enter Half Centuries : "))
    
    stats = {
        "Matches": matches,
        "Runs": runs,
        "Centuries": centuries,
        "HalfCenturies": half_centuries
    }
    
    player_tuple = (pid, name, team, stats)
    players.append(player_tuple)
    print("Player registered successfully.")

def displayPlayerDetails(p):
    print(f"Player ID      : {p[0]}")
    print(f"Player Name    : {p[1]}")
    print(f"Team           : {p[2]}")
    print(f"Matches        : {p[3]['Matches']}")
    print(f"Runs           : {p[3]['Runs']}")
    print(f"Centuries      : {p[3]['Centuries']}")
    print(f"Half Centuries : {p[3]['HalfCenturies']}")

def viewAllPlayers():
    if len(players) == 0:
        print("No player records found.")
    else:
        for p in players:
            displayPlayerDetails(p)
            print("----------------------------------------")

def updatePlayerStats():
    pid = int(input("Enter Player ID : "))
    p = SearchByID(pid, players)
    if p == None:
        print("Player not found.")
        return
    
    print("\nWhich statistic would you like to update?")
    print("1. Matches")
    print("2. Runs")
    print("3. Centuries")
    print("4. Half Centuries")
    stat_ch = int(input("Enter Stat Choice : "))
    
    if stat_ch == 1:
        val = int(input("Enter New Matches : "))
        p[3]["Matches"] = val
        print("Matches updated successfully.")
    elif stat_ch == 2:
        val = int(input("Enter New Runs : "))
        p[3]["Runs"] = val
        print("Runs updated successfully.")
    elif stat_ch == 3:
        val = int(input("Enter New Centuries : "))
        p[3]["Centuries"] = val
        print("Centuries updated successfully.")
    elif stat_ch == 4:
        val = int(input("Enter New Half Centuries : "))
        p[3]["HalfCenturies"] = val
        print("Half Centuries updated successfully.")
    else:
        print("Invalid Stat Choice.")

def searchPlayer():
    pid = int(input("Enter Player ID : "))
    p = SearchByID(pid, players)
    if p != None:
        displayPlayerDetails(p)
    else:
        print("Player not found.")

def displayHighestRunScorer():
    if len(players) == 0:
        print("No players available.")
        return
    
    highest_p = max(players, key=lambda p: p[3]["Runs"])
    print("\nHighest Run Scorer:")
    print(f"Player Name : {highest_p[1]}")
    print(f"Runs        : {highest_p[3]['Runs']}")

def displayPlayersAbove10Centuries():
    top_players = [p for p in players if p[3]["Centuries"] > 10]
    if len(top_players) == 0:
        print("No players found with more than 10 centuries.")
    else:
        print("\nPlayers with More Than 10 Centuries:")
        for p in top_players:
            print(p[1])
            print(f"Centuries : {p[3]['Centuries']}")
            print("----------------------------------------")

def displayTeamWiseCount():
    team_counts = {}
    for p in players:
        team = p[2]
        team_counts[team] = team_counts.get(team, 0) + 1
        
    if len(team_counts) == 0:
        print("No players found.")
    else:
        print("\nTeam-wise Player Count:")
        for team, count in team_counts.items():
            print(f"{team:<12} : {count}")

def main():
    while True:
        print("\n========== Cricket Team Management System ==========")
        print("1. Register a New Player")
        print("2. View All Players")
        print("3. Update Player Statistics")
        print("4. Search Player")
        print("5. Display Highest Run Scorer")
        print("6. Display Players with More Than 10 Centuries")
        print("7. Team-wise Player Count")
        print("8. Exit")
        
        ch = int(input("Enter Choice : "))
        
        if ch == 1:
            registerPlayer()
        elif ch == 2:
            viewAllPlayers()
        elif ch == 3:
            updatePlayerStats()
        elif ch == 4:
            searchPlayer()
        elif ch == 5:
            displayHighestRunScorer()
        elif ch == 6:
            displayPlayersAbove10Centuries()
        elif ch == 7:
            displayTeamWiseCount()
        elif ch == 8:
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()