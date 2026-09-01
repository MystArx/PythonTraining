import sys
from database import init_db
from logger_config import logger
from astronaut_operations import (
    addAstronaut,
    displayAllAstronauts,
    searchAstronautByIdOperation,
    searchAstronautByNameOperation,
    updateAstronautOperation,
    deleteAstronautOperation,
    filterAstronautsMenu,
    sortAstronautsMenu,
    generateAstronautReport
)
from mission_operations import (
    addMission,
    displayAllMissions,
    searchMissionByIdOperation,
    updateMissionOperation,
    deleteMissionOperation,
    viewMissionsOfAstronautOperation,
    filterMissionsMenu,
    sortMissionsMenu,
    viewMissionsWithAstronautDetails,
    generateMissionReport
)
from dashboard import displayMissionDashboard


def display_menu():
    """Prints the main interactive application menu."""
    print("\n========================================")
    print("   ASTRONAUT MISSION MANAGEMENT SYSTEM  ")
    print("========================================")
    print(" 1. Add Astronaut")
    print(" 2. View All Astronauts")
    print(" 3. Search Astronaut by ID")
    print(" 4. Search Astronaut by Name")
    print(" 5. Update Astronaut")
    print(" 6. Delete Astronaut")
    print(" 7. Add Mission")
    print(" 8. View All Missions")
    print(" 9. Search Mission by ID")
    print("10. Update Mission")
    print("11. Delete Mission")
    print("12. View Missions of an Astronaut")
    print("13. Filter Astronauts")
    print("14. Sort Astronauts")
    print("15. Filter Missions")
    print("16. Sort Missions")
    print("17. Generate Astronaut Report")
    print("18. Generate Mission Report")
    print("19. View Missions with Astronaut Details (JOIN)")
    print("20. Space Mission Dashboard")
    print("21. Exit")
    print("========================================")


def main():
    """Main application entry point and event loop."""
    logger.info("Application Started")
    print("Initializing Database & Tables...")
    if not init_db():
        print("Database connection initialization failed. Exiting application.")
        logger.critical("Database initialization failed at startup.")
        sys.exit(1)

    while True:
        try:
            display_menu()
            choice_str = input("Enter your choice (1-21): ").strip()

            if not choice_str.isdigit():
                print("\nInvalid choice! Please enter a number between 1 and 21.")
                logger.warning(f"Invalid menu input received: '{choice_str}'")
                continue

            choice = int(choice_str)

            if choice == 1:
                addAstronaut()
            elif choice == 2:
                displayAllAstronauts()
            elif choice == 3:
                searchAstronautByIdOperation()
            elif choice == 4:
                searchAstronautByNameOperation()
            elif choice == 5:
                updateAstronautOperation()
            elif choice == 6:
                deleteAstronautOperation()
            elif choice == 7:
                addMission()
            elif choice == 8:
                displayAllMissions()
            elif choice == 9:
                searchMissionByIdOperation()
            elif choice == 10:
                updateMissionOperation()
            elif choice == 11:
                deleteMissionOperation()
            elif choice == 12:
                viewMissionsOfAstronautOperation()
            elif choice == 13:
                filterAstronautsMenu()
            elif choice == 14:
                sortAstronautsMenu()
            elif choice == 15:
                filterMissionsMenu()
            elif choice == 16:
                sortMissionsMenu()
            elif choice == 17:
                generateAstronautReport()
            elif choice == 18:
                generateMissionReport()
            elif choice == 19:
                viewMissionsWithAstronautDetails()
            elif choice == 20:
                displayMissionDashboard()
            elif choice == 21:
                print("\nExiting Astronaut Mission Management System. Goodbye!")
                logger.info("Application Closed")
                break
            else:
                print("\nChoice out of range! Please select between 1 and 21.")
                logger.warning(f"Menu choice out of range: {choice}")

        except KeyboardInterrupt:
            print("\nApplication interrupted by user. Exiting...")
            logger.info("Application Closed via KeyboardInterrupt")
            break
        except Exception as error:
            logger.error(f"Unexpected error in main loop: {error}")
            print(f"\nAn unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
