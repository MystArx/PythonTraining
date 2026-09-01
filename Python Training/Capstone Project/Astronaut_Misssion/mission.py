from database import create_connection as cc
from logger_config import logger


class Mission:
    """Class representing a Space Mission domain model with database operations."""

    def __init__(self, mission_id, mission_name, destination, launch_date, duration_days, mission_status, astronaut_id):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.destination = destination
        self.launch_date = str(launch_date)
        self.duration_days = duration_days
        self.mission_status = mission_status
        self.astronaut_id = astronaut_id

    def displayMission(self):
        """Displays mission attributes in readable format."""
        print(f"Mission ID        : {self.mission_id}")
        print(f"Mission Name      : {self.mission_name}")
        print(f"Destination       : {self.destination}")
        print(f"Launch Date       : {self.launch_date}")
        print(f"Duration          : {self.duration_days} Days")
        print(f"Mission Status    : {self.mission_status}")
        print(f"Astronaut ID      : {self.astronaut_id}")

    def updateMission(self, name=None, destination=None, launch_date=None, duration_days=None, status=None, astronaut_id=None):
        """Updates mission details in the database and updates instance attributes."""
        connection = None
        cursor = None
        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()

                # If astronaut_id is being updated, check if target astronaut exists
                if astronaut_id is not None:
                    check_astro = "SELECT COUNT(*) FROM Astronaut WHERE AstronautId = %s"
                    cursor.execute(check_astro, (astronaut_id,))
                    if cursor.fetchone()[0] == 0:
                        print(f"Cannot update mission: Astronaut ID {astronaut_id} does not exist.")
                        logger.warning(f"Failed to update Mission {self.mission_id}: Astronaut ID {astronaut_id} not found.")
                        return False

                fields = []
                values = []

                if name is not None:
                    fields.append("MissionName = %s")
                    values.append(name)
                if destination is not None:
                    fields.append("Destination = %s")
                    values.append(destination)
                if launch_date is not None:
                    fields.append("LaunchDate = %s")
                    values.append(str(launch_date))
                if duration_days is not None:
                    fields.append("DurationDays = %s")
                    values.append(duration_days)
                if status is not None:
                    fields.append("MissionStatus = %s")
                    values.append(status)
                if astronaut_id is not None:
                    fields.append("AstronautId = %s")
                    values.append(astronaut_id)

                if not fields:
                    print("No fields specified for update.")
                    return False

                values.append(self.mission_id)
                query = f"UPDATE Mission SET {', '.join(fields)} WHERE MissionId = %s"

                cursor.execute(query, tuple(values))
                connection.commit()

                # Update local attributes
                if name is not None:
                    self.mission_name = name
                if destination is not None:
                    self.destination = destination
                if launch_date is not None:
                    self.launch_date = str(launch_date)
                if duration_days is not None:
                    self.duration_days = duration_days
                if status is not None:
                    self.mission_status = status
                if astronaut_id is not None:
                    self.astronaut_id = astronaut_id

                logger.info(f"Mission {self.mission_id} Updated Successfully.")
                print("Mission updated successfully.")
                return True
            else:
                print("Connection Failed: Ensure your MySQL server is running.")
                return False

        except Exception as error:
            logger.error(f"Failed to Update Mission {self.mission_id}: {error}")
            print(f"Failed to Update Mission: {error}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    def deleteMission(self):
        """Deletes mission from database."""
        connection = None
        cursor = None
        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()

                query = "DELETE FROM Mission WHERE MissionId = %s"
                cursor.execute(query, (self.mission_id,))
                connection.commit()

                logger.info(f"Mission {self.mission_id} Deleted Successfully.")
                print(f"Mission {self.mission_id} deleted successfully.")
                return True
            else:
                print("Connection Failed: Ensure your MySQL server is running.")
                return False

        except Exception as error:
            logger.error(f"Failed to Delete Mission {self.mission_id}: {error}")
            print(f"Failed to Delete Mission: {error}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
