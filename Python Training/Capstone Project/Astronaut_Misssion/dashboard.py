from database import create_connection as cc
from logger_config import logger


def displayMissionDashboard():
    """Calculates space mission metrics using SQL queries and displays the dashboard."""
    connection = None
    cursor = None
    try:
        connection = cc()
        if connection is None:
            print("Connection Failed: Unable to display dashboard.")
            return

        cursor = connection.cursor()

        # Total Astronauts
        cursor.execute("SELECT COUNT(*) FROM Astronaut")
        total_astronauts = cursor.fetchone()[0]

        # Active Astronauts
        cursor.execute("SELECT COUNT(*) FROM Astronaut WHERE Status = 'Active'")
        active_astronauts = cursor.fetchone()[0]

        # Astronauts in Training
        cursor.execute("SELECT COUNT(*) FROM Astronaut WHERE Status = 'Training'")
        training_astronauts = cursor.fetchone()[0]

        # Retired Astronauts
        cursor.execute("SELECT COUNT(*) FROM Astronaut WHERE Status = 'Retired'")
        retired_astronauts = cursor.fetchone()[0]

        # Total Missions
        cursor.execute("SELECT COUNT(*) FROM Mission")
        total_missions = cursor.fetchone()[0]

        # Planned Missions
        cursor.execute("SELECT COUNT(*) FROM Mission WHERE MissionStatus = 'Planned'")
        planned_missions = cursor.fetchone()[0]

        # Active Missions
        cursor.execute("SELECT COUNT(*) FROM Mission WHERE MissionStatus = 'Active'")
        active_missions = cursor.fetchone()[0]

        # Completed Missions
        cursor.execute("SELECT COUNT(*) FROM Mission WHERE MissionStatus = 'Completed'")
        completed_missions = cursor.fetchone()[0]

        # Most Experienced Astronaut
        cursor.execute("SELECT AstronautName, ExperienceYears FROM Astronaut ORDER BY ExperienceYears DESC LIMIT 1")
        most_exp_row = cursor.fetchone()
        most_exp_str = f"{most_exp_row[0]} - {most_exp_row[1]} Years" if most_exp_row else "N/A"

        # Longest Mission
        cursor.execute("SELECT MissionName, DurationDays FROM Mission ORDER BY DurationDays DESC LIMIT 1")
        longest_mission_row = cursor.fetchone()
        longest_mission_str = f"{longest_mission_row[0]} - {longest_mission_row[1]} Days" if longest_mission_row else "N/A"

        print("\n====================================")
        print("        SPACE MISSION DASHBOARD     ")
        print("====================================")
        print(f"Total Astronauts       : {total_astronauts}")
        print(f"Active Astronauts      : {active_astronauts}")
        print(f"Astronauts in Training : {training_astronauts}")
        print(f"Retired Astronauts     : {retired_astronauts}")
        print("-" * 36)
        print(f"Total Missions         : {total_missions}")
        print(f"Planned Missions       : {planned_missions}")
        print(f"Active Missions        : {active_missions}")
        print(f"Completed Missions     : {completed_missions}")
        print("-" * 36)
        print("Most Experienced Astronaut:")
        print(f"  {most_exp_str}")
        print("Longest Mission:")
        print(f"  {longest_mission_str}")
        print("====================================\n")

        logger.info("Displayed Space Mission Dashboard.")

    except Exception as e:
        logger.error(f"Failed to generate Space Mission Dashboard: {e}")
        print(f"Failed to generate Space Mission Dashboard: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    displayMissionDashboard()
