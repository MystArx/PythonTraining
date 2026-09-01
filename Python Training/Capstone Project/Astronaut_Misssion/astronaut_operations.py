import os
from database import create_connection as cc
from astronaut import Astronaut
from logger_config import logger


def getAstronautById(astronaut_id):
    """Fetches astronaut from database by ID and returns Astronaut object or None."""
    connection = None
    cursor = None
    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Astronaut WHERE AstronautId = %s"
            cursor.execute(query, (astronaut_id,))
            row = cursor.fetchone()
            if row:
                return Astronaut(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            else:
                logger.warning(f"Astronaut {astronaut_id} Not Found")
                return None
        return None
    except Exception as error:
        logger.error(f"Error fetching Astronaut {astronaut_id}: {error}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def addAstronaut():
    """Prompts for input, validates rules, and inserts new Astronaut into DB."""
    print("\n--- Add New Astronaut ---")
    try:
        astro_id_str = input("Enter Astronaut ID: ").strip()
        if not astro_id_str.isdigit() or int(astro_id_str) <= 0:
            print("Invalid Astronaut ID! ID must be a positive integer.")
            logger.warning("Invalid input: Astronaut ID must be a positive integer.")
            return

        astronaut_id = int(astro_id_str)

        # Check duplicate Primary Key
        if getAstronautById(astronaut_id) is not None:
            print(f"Duplicate Astronaut! Astronaut ID {astronaut_id} already exists.")
            print("Please enter a different Astronaut ID.")
            logger.warning(f"Duplicate Astronaut ID attempt: {astronaut_id}")
            return

        name = input("Enter Name: ").strip()
        if not name:
            print("Invalid Name! Name cannot be empty.")
            logger.warning("Invalid input: Empty name.")
            return

        age_str = input("Enter Age (21-65): ").strip()
        if not age_str.isdigit():
            print("Invalid Age! Age must be a number between 21 and 65.")
            return
        age = int(age_str)
        if age < 21 or age > 65:
            print("Invalid Age! Age must be between 21 and 65.")
            logger.warning(f"Invalid input: Age {age} out of bounds (21-65).")
            return

        country = input("Enter Country: ").strip()
        if not country:
            print("Invalid Country! Country cannot be empty.")
            logger.warning("Invalid input: Empty country.")
            return

        exp_str = input("Enter Experience (Years): ").strip()
        if not exp_str.isdigit():
            print("Invalid Experience! Experience cannot be negative.")
            return
        exp_years = int(exp_str)
        if exp_years < 0:
            print("Invalid Experience! Experience cannot be negative.")
            logger.warning(f"Invalid input: Negative experience {exp_years}.")
            return

        spec = input("Enter Specialization (Pilot/Engineer/Scientist/Doctor): ").strip()
        if not spec:
            print("Invalid Specialization! Specialization cannot be empty.")
            return

        print("Select Status:")
        print("1. Active\n2. Training\n3. Retired")
        status_choice = input("Enter choice (1-3): ").strip()
        status_map = {"1": "Active", "2": "Training", "3": "Retired"}
        if status_choice not in status_map:
            print("Invalid Status selection! Must be Active, Training, or Retired.")
            logger.warning(f"Invalid status selection: {status_choice}")
            return
        status = status_map[status_choice]

        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO Astronaut (AstronautId, AstronautName, Age, Country, ExperienceYears, Specialization, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (astronaut_id, name, age, country, exp_years, spec, status))
            connection.commit()
            cursor.close()
            connection.close()

            print("Astronaut added successfully.")
            logger.info(f"Astronaut {astronaut_id} Added Successfully.")
        else:
            print("Connection Failed: Unable to connect to database.")

    except Exception as e:
        logger.error(f"Error adding astronaut: {e}")
        print(f"Error adding astronaut: {e}")


def displayAllAstronauts():
    """Displays all astronaut records formatted in a table."""
    connection = None
    cursor = None
    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Astronaut ORDER BY AstronautId"
            cursor.execute(query)
            rows = cursor.fetchall()

            if not rows:
                print("\nNo astronaut records found.")
                logger.info("View All Astronauts: No records present.")
            else:
                print("\n" + "=" * 80)
                print(f"{'ID':<6} {'Name':<20} {'Age':<6} {'Country':<15} {'Experience':<12} {'Specialization':<15} {'Status':<10}")
                print("-" * 80)
                for r in rows:
                    exp_str = f"{r[4]} Years"
                    print(f"{r[0]:<6} {r[1]:<20} {r[2]:<6} {r[3]:<15} {exp_str:<12} {r[5]:<15} {r[6]:<10}")
                print("=" * 80)
                logger.info(f"Displayed All Astronauts ({len(rows)} record(s)).")
        else:
            print("Connection Failed: Ensure your MySQL server is running.")
    except Exception as e:
        logger.error(f"Failed to display astronauts: {e}")
        print(f"Failed to display astronauts: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def searchAstronautByIdOperation():
    """Prompts for ID and displays full details of astronaut if found."""
    try:
        astro_id_str = input("\nEnter Astronaut ID: ").strip()
        if not astro_id_str.isdigit():
            print("Invalid input! Astronaut ID must be an integer.")
            return
        astro_id = int(astro_id_str)
        astro = getAstronautById(astro_id)
        if astro:
            print("\n--- Astronaut Details ---")
            astro.displayAstronaut()
            logger.info(f"Searched Astronaut ID {astro_id}: Found.")
        else:
            print(f"Astronaut ID {astro_id} was not found. Please check the ID and try again.")
    except Exception as e:
        print(f"Error in search: {e}")


def searchAstronautByNameOperation():
    """Partial-name search for astronauts using SQL LIKE."""
    try:
        name_query = input("\nEnter Astronaut Name (or partial name): ").strip()
        if not name_query:
            print("Search string cannot be empty.")
            return

        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Astronaut WHERE AstronautName LIKE %s"
            cursor.execute(query, (f"%{name_query}%",))
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            if not rows:
                print(f"No astronauts matching '{name_query}' found.")
                logger.info(f"Search by Name '{name_query}': No records found.")
            else:
                print(f"\n--- Search Results for '{name_query}' ---")
                print(f"{'ID':<6} {'Name':<20} {'Country':<15} {'Experience':<12} {'Status':<10}")
                print("-" * 65)
                for r in rows:
                    print(f"{r[0]:<6} {r[1]:<20} {r[3]:<15} {f'{r[4]} Years':<12} {r[6]:<10}")
                logger.info(f"Search by Name '{name_query}': Found {len(rows)} record(s).")
        else:
            print("Connection Failed.")
    except Exception as e:
        logger.error(f"Error searching astronaut by name: {e}")
        print(f"Error in search: {e}")


def updateAstronautOperation():
    """Prompts for Astronaut ID and updates selected fields."""
    try:
        astro_id_str = input("\nEnter Astronaut ID to Update: ").strip()
        if not astro_id_str.isdigit():
            print("Invalid Astronaut ID!")
            return
        astro_id = int(astro_id_str)
        astro = getAstronautById(astro_id)
        if not astro:
            print(f"Astronaut ID {astro_id} not found.")
            return

        print("\nAstronaut Found:")
        astro.displayAstronaut()
        print("\nWhat would you like to update?")
        print("1. Name\n2. Age\n3. Country\n4. Experience\n5. Specialization\n6. Status\n7. Cancel")
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            new_val = input("Enter New Name: ").strip()
            if new_val:
                astro.updateAstronaut(name=new_val)
        elif choice == "2":
            new_val_str = input("Enter New Age (21-65): ").strip()
            if new_val_str.isdigit() and 21 <= int(new_val_str) <= 65:
                astro.updateAstronaut(age=int(new_val_str))
            else:
                print("Invalid Age! Age must be between 21 and 65.")
        elif choice == "3":
            new_val = input("Enter New Country: ").strip()
            if new_val:
                astro.updateAstronaut(country=new_val)
        elif choice == "4":
            new_val_str = input("Enter New Experience (Years): ").strip()
            if new_val_str.isdigit() and int(new_val_str) >= 0:
                astro.updateAstronaut(experience_years=int(new_val_str))
            else:
                print("Invalid Experience! Experience cannot be negative.")
        elif choice == "5":
            new_val = input("Enter New Specialization: ").strip()
            if new_val:
                astro.updateAstronaut(specialization=new_val)
        elif choice == "6":
            print("Select New Status:\n1. Active\n2. Training\n3. Retired")
            sc = input("Choice (1-3): ").strip()
            s_map = {"1": "Active", "2": "Training", "3": "Retired"}
            if sc in s_map:
                astro.updateAstronaut(status=s_map[sc])
            else:
                print("Invalid Status selection.")
        elif choice == "7":
            print("Update cancelled.")
        else:
            print("Invalid choice.")
    except Exception as e:
        logger.error(f"Error in update astronaut operation: {e}")
        print(f"Error in update: {e}")


def deleteAstronautOperation():
    """Prompts for Astronaut ID and deletes astronaut if no missions exist."""
    try:
        astro_id_str = input("\nEnter Astronaut ID to Delete: ").strip()
        if not astro_id_str.isdigit():
            print("Invalid Astronaut ID!")
            return
        astro_id = int(astro_id_str)
        astro = getAstronautById(astro_id)
        if not astro:
            print(f"Astronaut ID {astro_id} not found.")
            return

        confirm = input(f"Are you sure you want to delete Astronaut {astro.astronaut_name} (ID: {astro_id})? (y/n): ").strip().lower()
        if confirm == 'y':
            astro.deleteAstronaut()
        else:
            print("Deletion cancelled.")
    except Exception as e:
        logger.error(f"Error in delete astronaut operation: {e}")
        print(f"Error in delete: {e}")


def filterAstronautsMenu():
    """Filtering menu for Astronauts."""
    while True:
        print("\n========= FILTER ASTRONAUTS =========")
        print("1. Filter by Country")
        print("2. Filter by Status")
        print("3. Filter by Specialization")
        print("4. Experience Greater Than or Equal to")
        print("5. Age Greater Than or Equal to")
        print("6. Back")
        ch = input("Enter choice: ").strip()

        if ch == "6":
            break

        query = "SELECT * FROM Astronaut WHERE "
        param = None

        if ch == "1":
            country = input("Enter Country: ").strip()
            query += "Country = %s"
            param = (country,)
        elif ch == "2":
            status = input("Enter Status (Active/Training/Retired): ").strip()
            query += "Status = %s"
            param = (status,)
        elif ch == "3":
            spec = input("Enter Specialization: ").strip()
            query += "Specialization = %s"
            param = (spec,)
        elif ch == "4":
            exp = input("Enter Minimum Experience: ").strip()
            if not exp.isdigit():
                print("Invalid input.")
                continue
            query += "ExperienceYears >= %s"
            param = (int(exp),)
        elif ch == "5":
            age = input("Enter Minimum Age: ").strip()
            if not age.isdigit():
                print("Invalid input.")
                continue
            query += "Age >= %s"
            param = (int(age),)
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
                    print("No matching astronauts found.")
                else:
                    print("\n" + "=" * 80)
                    print(f"{'ID':<6} {'Name':<20} {'Age':<6} {'Country':<15} {'Experience':<12} {'Specialization':<15} {'Status':<10}")
                    print("-" * 80)
                    for r in rows:
                        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<6} {r[3]:<15} {f'{r[4]} Years':<12} {r[5]:<15} {r[6]:<10}")
                    print("=" * 80)
                    logger.info(f"Filtered Astronauts: {len(rows)} record(s) matched.")
        except Exception as e:
            logger.error(f"Error filtering astronauts: {e}")
            print(f"Error filtering astronauts: {e}")


def sortAstronautsMenu():
    """Sorting menu for Astronauts."""
    while True:
        print("\n========= SORT ASTRONAUTS =========")
        print("1. Sort by Name A-Z")
        print("2. Sort by Name Z-A")
        print("3. Sort by Age Low-High")
        print("4. Sort by Age High-Low")
        print("5. Sort by Experience Low-High")
        print("6. Sort by Experience High-Low")
        print("7. Back")
        ch = input("Enter choice: ").strip()

        if ch == "7":
            break

        sort_sql = {
            "1": "AstronautName ASC",
            "2": "AstronautName DESC",
            "3": "Age ASC",
            "4": "Age DESC",
            "5": "ExperienceYears ASC",
            "6": "ExperienceYears DESC"
        }

        if ch not in sort_sql:
            print("Invalid option.")
            continue

        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()
                query = f"SELECT * FROM Astronaut ORDER BY {sort_sql[ch]}"
                cursor.execute(query)
                rows = cursor.fetchall()
                cursor.close()
                connection.close()

                print("\n" + "=" * 80)
                print(f"{'ID':<6} {'Name':<20} {'Age':<6} {'Country':<15} {'Experience':<12} {'Specialization':<15} {'Status':<10}")
                print("-" * 80)
                for r in rows:
                    print(f"{r[0]:<6} {r[1]:<20} {r[2]:<6} {r[3]:<15} {f'{r[4]} Years':<12} {r[5]:<15} {r[6]:<10}")
                print("=" * 80)
                logger.info(f"Sorted Astronauts using criteria {ch}.")
        except Exception as e:
            logger.error(f"Error sorting astronauts: {e}")
            print(f"Error sorting astronauts: {e}")


def generateAstronautReport():
    """Generates AstronautReport.txt file in reports directory."""
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    report_path = os.path.join(reports_dir, "AstronautReport.txt")

    try:
        connection = cc()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT * FROM Astronaut ORDER BY AstronautId"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            with open(report_path, "w") as f:
                f.write("==================================\n")
                f.write("ASTRONAUT REPORT\n")
                f.write("==================================\n")
                if not rows:
                    f.write("No astronaut records available.\n")
                else:
                    for r in rows:
                        f.write(f"Astronaut ID : {r[0]}\n")
                        f.write(f"Name         : {r[1]}\n")
                        f.write(f"Age          : {r[2]}\n")
                        f.write(f"Country      : {r[3]}\n")
                        f.write(f"Experience   : {r[4]} Years\n")
                        f.write(f"Specialization: {r[5]}\n")
                        f.write(f"Status       : {r[6]}\n")
                        f.write("----------------------------------\n")

            print(f"\nAstronaut report generated successfully at: {report_path}")
            logger.info(f"Generated Astronaut Report: {report_path}")
        else:
            print("Connection Failed: Unable to generate report.")
    except Exception as e:
        logger.error(f"Failed to generate Astronaut Report: {e}")
        print(f"Failed to generate Astronaut Report: {e}")
