import os
from datetime import datetime
from database import create_connection as cc
from mission import Mission
from astronaut_operations import getAstronautById
from logger_config import logger


def getMissionById(mission_id):
    """Fetches mission from database by ID and returns Mission object or None."""
    connection = None
    cursor = None
    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Mission WHERE MissionId = %s"
            cursor.execute(query, (mission_id,))
            row = cursor.fetchone()
            if row:
                return Mission(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            else:
                logger.warning(f"Mission {mission_id} Not Found")
                return None
        return None
    except Exception as error:
        logger.error(f"Error fetching Mission {mission_id}: {error}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def addMission():
    """Prompts for mission details, validates foreign key & constraints, and inserts record."""
    print("\n--- Add New Mission ---")
    try:
        # Step 1: Verify foreign key astronaut exists
        astro_id_str = input("Enter Astronaut ID: ").strip()
        if not astro_id_str.isdigit():
            print("Invalid Astronaut ID! Must be a positive integer.")
            return

        astronaut_id = int(astro_id_str)
        print("Checking Astronaut...")
        astro = getAstronautById(astronaut_id)
        if astro is None:
            print(f"Mission cannot be created.")
            print(f"Astronaut ID {astronaut_id} does not exist.")
            print("Please create the astronaut first.")
            logger.warning(f"Failed to create Mission: Astronaut ID {astronaut_id} does not exist.")
            return

        print(f"Astronaut Found:\n{astro.astronaut_id} - {astro.astronaut_name}")

        # Step 2: Prompt for Mission details
        mission_id_str = input("\nEnter Mission ID: ").strip()
        if not mission_id_str.isdigit() or int(mission_id_str) <= 0:
            print("Invalid Mission ID! Must be a positive integer.")
            logger.warning("Invalid input: Mission ID must be a positive integer.")
            return
        mission_id = int(mission_id_str)

        # Check duplicate Primary Key
        if getMissionById(mission_id) is not None:
            print(f"Duplicate Mission! Mission ID {mission_id} already exists.")
            logger.warning(f"Duplicate Mission ID attempt: {mission_id}")
            return

        name = input("Enter Mission Name: ").strip()
        if not name:
            print("Invalid Mission Name! Cannot be empty.")
            return

        destination = input("Enter Destination (e.g., Moon, Mars, ISS): ").strip()
        if not destination:
            print("Invalid Destination! Cannot be empty.")
            return

        launch_date_str = input("Enter Launch Date (YYYY-MM-DD): ").strip()
        try:
            launch_date = datetime.strptime(launch_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("ERROR | Invalid Mission Date!")
            print("Please enter a valid date in YYYY-MM-DD format.")
            logger.error(f"Invalid Mission Date entered: {launch_date_str}")
            return

        duration_str = input("Enter Duration (Days): ").strip()
        if not duration_str.isdigit() or int(duration_str) <= 0:
            print("Invalid Duration! Duration must be greater than 0 days.")
            logger.warning(f"Invalid input: Duration {duration_str}.")
            return
        duration_days = int(duration_str)

        print("Select Mission Status:")
        print("1. Planned\n2. Active\n3. Completed")
        status_choice = input("Enter choice (1-3): ").strip()
        status_map = {"1": "Planned", "2": "Active", "3": "Completed"}
        if status_choice not in status_map:
            print("Invalid Mission Status selection!")
            return
        status = status_map[status_choice]

        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO Mission (MissionId, MissionName, Destination, LaunchDate, DurationDays, MissionStatus, AstronautId)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (mission_id, name, destination, str(launch_date), duration_days, status, astronaut_id))
            connection.commit()
            cursor.close()
            connection.close()

            print("Mission added successfully.")
            logger.info(f"Mission {mission_id} Created Successfully.")
        else:
            print("Connection Failed: Unable to connect to database.")

    except Exception as e:
        logger.error(f"Error adding mission: {e}")
        print(f"Error adding mission: {e}")


def displayAllMissions():
    """Displays all mission records formatted in a table."""
    connection = None
    cursor = None
    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Mission ORDER BY MissionId"
            cursor.execute(query)
            rows = cursor.fetchall()

            if not rows:
                print("\nNo mission records found.")
                logger.info("View All Missions: No records present.")
            else:
                print("\n" + "=" * 90)
                print(f"{'ID':<6} {'Mission Name':<20} {'Destination':<15} {'Launch Date':<12} {'Duration':<12} {'Status':<12} {'Astronaut ID':<12}")
                print("-" * 90)
                for r in rows:
                    dur_str = f"{r[4]} Days"
                    print(f"{r[0]:<6} {r[1]:<20} {r[2]:<15} {str(r[3]):<12} {dur_str:<12} {r[5]:<12} {r[6]:<12}")
                print("=" * 90)
                logger.info(f"Displayed All Missions ({len(rows)} record(s)).")
        else:
            print("Connection Failed: Ensure your MySQL server is running.")
    except Exception as e:
        logger.error(f"Failed to display missions: {e}")
        print(f"Failed to display missions: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def searchMissionByIdOperation():
    """Prompts for Mission ID and displays full details."""
    try:
        mission_id_str = input("\nEnter Mission ID: ").strip()
        if not mission_id_str.isdigit():
            print("Invalid input! Mission ID must be an integer.")
            return
        mission_id = int(mission_id_str)
        m = getMissionById(mission_id)
        if m:
            print("\n--- Mission Details ---")
            m.displayMission()
            logger.info(f"Searched Mission ID {mission_id}: Found.")
        else:
            print(f"Mission ID {mission_id} was not found.")
    except Exception as e:
        print(f"Error in search: {e}")


def updateMissionOperation():
    """Prompts for Mission ID and updates selected fields."""
    try:
        mission_id_str = input("\nEnter Mission ID to Update: ").strip()
        if not mission_id_str.isdigit():
            print("Invalid Mission ID!")
            return
        mission_id = int(mission_id_str)
        m = getMissionById(mission_id)
        if not m:
            print(f"Mission ID {mission_id} not found.")
            return

        print("\nMission Found:")
        m.displayMission()
        print("\nWhat would you like to update?")
        print("1. Mission Name\n2. Destination\n3. Launch Date\n4. Duration Days\n5. Mission Status\n6. Reassign Astronaut ID\n7. Cancel")
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            new_val = input("Enter New Mission Name: ").strip()
            if new_val:
                m.updateMission(name=new_val)
        elif choice == "2":
            new_val = input("Enter New Destination: ").strip()
            if new_val:
                m.updateMission(destination=new_val)
        elif choice == "3":
            new_val_str = input("Enter New Launch Date (YYYY-MM-DD): ").strip()
            try:
                dt = datetime.strptime(new_val_str, "%Y-%m-%d").date()
                m.updateMission(launch_date=dt)
            except ValueError:
                print("Invalid Date format! Please use YYYY-MM-DD.")
        elif choice == "4":
            new_val_str = input("Enter New Duration (Days): ").strip()
            if new_val_str.isdigit() and int(new_val_str) > 0:
                m.updateMission(duration_days=int(new_val_str))
            else:
                print("Invalid Duration! Must be > 0.")
        elif choice == "5":
            print("Select New Status:\n1. Planned\n2. Active\n3. Completed")
            sc = input("Choice (1-3): ").strip()
            s_map = {"1": "Planned", "2": "Active", "3": "Completed"}
            if sc in s_map:
                m.updateMission(status=s_map[sc])
            else:
                print("Invalid Status selection.")
        elif choice == "6":
            new_astro_str = input("Enter New Astronaut ID: ").strip()
            if new_astro_str.isdigit():
                m.updateMission(astronaut_id=int(new_astro_str))
            else:
                print("Invalid Astronaut ID.")
        elif choice == "7":
            print("Update cancelled.")
        else:
            print("Invalid choice.")
    except Exception as e:
        logger.error(f"Error in update mission operation: {e}")
        print(f"Error in update: {e}")


def deleteMissionOperation():
    """Prompts for Mission ID and deletes mission."""
    try:
        mission_id_str = input("\nEnter Mission ID to Delete: ").strip()
        if not mission_id_str.isdigit():
            print("Invalid Mission ID!")
            return
        mission_id = int(mission_id_str)
        m = getMissionById(mission_id)
        if not m:
            print(f"Mission ID {mission_id} not found.")
            return

        confirm = input(f"Are you sure you want to delete Mission '{m.mission_name}' (ID: {mission_id})? (y/n): ").strip().lower()
        if confirm == 'y':
            m.deleteMission()
        else:
            print("Deletion cancelled.")
    except Exception as e:
        logger.error(f"Error in delete mission operation: {e}")
        print(f"Error in delete: {e}")


def viewMissionsOfAstronautOperation():
    """Displays all missions assigned to a specific astronaut."""
    try:
        astro_id_str = input("\nEnter Astronaut ID: ").strip()
        if not astro_id_str.isdigit():
            print("Invalid Astronaut ID!")
            return
        astro_id = int(astro_id_str)
        astro = getAstronautById(astro_id)
        if not astro:
            print(f"Astronaut ID {astro_id} not found.")
            return

        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Mission WHERE AstronautId = %s ORDER BY MissionId"
            cursor.execute(query, (astro_id,))
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            print(f"\n--- Missions Assigned to Astronaut {astro.astronaut_name} (ID: {astro_id}) ---")
            if not rows:
                print("No missions currently assigned to this astronaut.")
            else:
                print(f"{'ID':<6} {'Mission Name':<20} {'Destination':<15} {'Launch Date':<12} {'Duration':<12} {'Status':<12}")
                print("-" * 80)
                for r in rows:
                    print(f"{r[0]:<6} {r[1]:<20} {r[2]:<15} {str(r[3]):<12} {f'{r[4]} Days':<12} {r[5]:<12}")
            logger.info(f"Viewed Missions of Astronaut {astro_id}: Found {len(rows)} record(s).")
        else:
            print("Connection Failed.")
    except Exception as e:
        logger.error(f"Error viewing missions of astronaut: {e}")
        print(f"Error: {e}")


def filterMissionsMenu():
    """Filtering menu for Missions."""
    while True:
        print("\n========= FILTER MISSIONS =========")
        print("1. Filter by Destination")
        print("2. Filter by Mission Status")
        print("3. Filter by Astronaut ID")
        print("4. Filter by Minimum Duration Days")
        print("5. Back")
        ch = input("Enter choice: ").strip()

        if ch == "5":
            break

        query = "SELECT * FROM Mission WHERE "
        param = None

        if ch == "1":
            dest = input("Enter Destination (e.g. Mars, Moon): ").strip()
            query += "Destination = %s"
            param = (dest,)
        elif ch == "2":
            st = input("Enter Mission Status (Planned/Active/Completed): ").strip()
            query += "MissionStatus = %s"
            param = (st,)
        elif ch == "3":
            aid = input("Enter Astronaut ID: ").strip()
            if not aid.isdigit():
                print("Invalid input.")
                continue
            query += "AstronautId = %s"
            param = (int(aid),)
        elif ch == "4":
            dur = input("Enter Minimum Duration Days: ").strip()
            if not dur.isdigit():
                print("Invalid input.")
                continue
            query += "DurationDays >= %s"
            param = (int(dur),)
        else:
            print("Invalid option.")
            continue

        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()
                cursor.execute(query, param)
                rows = cursor.fetchall()
                cursor.close()
                connection.close()

                if not rows:
                    print("No matching missions found.")
                else:
                    print("\n" + "=" * 90)
                    print(f"{'ID':<6} {'Mission Name':<20} {'Destination':<15} {'Launch Date':<12} {'Duration':<12} {'Status':<12} {'Astronaut ID':<12}")
                    print("-" * 90)
                    for r in rows:
                        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<15} {str(r[3]):<12} {f'{r[4]} Days':<12} {r[5]:<12} {r[6]:<12}")
                    print("=" * 90)
                    logger.info(f"Filtered Missions: {len(rows)} record(s) matched.")
        except Exception as e:
            logger.error(f"Error filtering missions: {e}")
            print(f"Error filtering missions: {e}")


def sortMissionsMenu():
    """Sorting menu for Missions."""
    while True:
        print("\n========= SORT MISSIONS =========")
        print("1. Sort by Launch Date (Earliest First)")
        print("2. Sort by Launch Date (Latest First)")
        print("3. Sort by Duration (Shortest First)")
        print("4. Sort by Duration (Longest First)")
        print("5. Sort by Mission Name (A-Z)")
        print("6. Back")
        ch = input("Enter choice: ").strip()

        if ch == "6":
            break

        sort_sql = {
            "1": "LaunchDate ASC",
            "2": "LaunchDate DESC",
            "3": "DurationDays ASC",
            "4": "DurationDays DESC",
            "5": "MissionName ASC"
        }

        if ch not in sort_sql:
            print("Invalid option.")
            continue

        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()
                query = f"SELECT * FROM Mission ORDER BY {sort_sql[ch]}"
                cursor.execute(query)
                rows = cursor.fetchall()
                cursor.close()
                connection.close()

                print("\n" + "=" * 90)
                print(f"{'ID':<6} {'Mission Name':<20} {'Destination':<15} {'Launch Date':<12} {'Duration':<12} {'Status':<12} {'Astronaut ID':<12}")
                print("-" * 90)
                for r in rows:
                    print(f"{r[0]:<6} {r[1]:<20} {r[2]:<15} {str(r[3]):<12} {f'{r[4]} Days':<12} {r[5]:<12} {r[6]:<12}")
                print("=" * 90)
                logger.info(f"Sorted Missions using criteria {ch}.")
        except Exception as e:
            logger.error(f"Error sorting missions: {e}")
            print(f"Error sorting missions: {e}")


def viewMissionsWithAstronautDetails():
    """SQL JOIN operation: View Missions with assigned Astronaut Details."""
    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = """
            SELECT Mission.MissionId,
                   Mission.MissionName,
                   Mission.Destination,
                   Mission.LaunchDate,
                   Mission.DurationDays,
                   Mission.MissionStatus,
                   Astronaut.AstronautId,
                   Astronaut.AstronautName
            FROM Mission
            JOIN Astronaut
            ON Mission.AstronautId = Astronaut.AstronautId
            ORDER BY Mission.MissionId
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            print("\n" + "=" * 95)
            print("ASTRONAUT & MISSION JOINED DETAILS")
            print("=" * 95)
            if not rows:
                print("No assigned mission records found.")
            else:
                print(f"{'Mission ID':<12} {'Mission Name':<20} {'Destination':<15} {'Astronaut ID':<14} {'Astronaut Name':<20}")
                print("-" * 95)
                for r in rows:
                    print(f"{r[0]:<12} {r[1]:<20} {r[2]:<15} {r[6]:<14} {r[7]:<20}")
                print("=" * 95)
            logger.info("Viewed Missions with Astronaut Details (JOIN operation).")
        else:
            print("Connection Failed.")
    except Exception as e:
        logger.error(f"Error executing JOIN query: {e}")
        print(f"Error executing JOIN operation: {e}")


def generateMissionReport():
    """Generates MissionReport.txt file in reports directory."""
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    report_path = os.path.join(reports_dir, "MissionReport.txt")

    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = """
            SELECT Mission.MissionId, Mission.MissionName, Mission.Destination,
                   Mission.LaunchDate, Mission.DurationDays, Mission.MissionStatus,
                   Astronaut.AstronautId, Astronaut.AstronautName
            FROM Mission
            LEFT JOIN Astronaut ON Mission.AstronautId = Astronaut.AstronautId
            ORDER BY Mission.MissionId
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            with open(report_path, "w") as f:
                f.write("==================================\n")
                f.write("MISSION REPORT\n")
                f.write("==================================\n")
                if not rows:
                    f.write("No mission records available.\n")
                else:
                    for r in rows:
                        f.write(f"Mission ID     : {r[0]}\n")
                        f.write(f"Mission Name   : {r[1]}\n")
                        f.write(f"Destination    : {r[2]}\n")
                        f.write(f"Launch Date    : {r[3]}\n")
                        f.write(f"Duration       : {r[4]} Days\n")
                        f.write(f"Status         : {r[5]}\n")
                        f.write(f"Assigned To    : {r[7]} (ID: {r[6]})\n")
                        f.write("----------------------------------\n")

            print(f"\nMission report generated successfully at: {report_path}")
            logger.info(f"Generated Mission Report: {report_path}")
        else:
            print("Connection Failed: Unable to generate report.")
    except Exception as e:
        logger.error(f"Failed to generate Mission Report: {e}")
        print(f"Failed to generate Mission Report: {e}")
