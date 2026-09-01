from database import create_connection as cc
from logger_config import logger


class Astronaut:
    """Class representing an Astronaut domain model with database operations."""

    def __init__(self, astronaut_id, astronaut_name, age, country, experience_years, specialization, status):
        self.astronaut_id = astronaut_id
        self.astronaut_name = astronaut_name
        self.age = age
        self.country = country
        self.experience_years = experience_years
        self.specialization = specialization
        self.status = status

    def displayAstronaut(self):
        """Displays astronaut attributes in readable format."""
        print(f"Astronaut ID      : {self.astronaut_id}")
        print(f"Name              : {self.astronaut_name}")
        print(f"Age               : {self.age}")
        print(f"Country           : {self.country}")
        print(f"Experience        : {self.experience_years} Years")
        print(f"Specialization    : {self.specialization}")
        print(f"Status            : {self.status}")

    def updateAstronaut(self, name=None, age=None, country=None, experience_years=None, specialization=None, status=None):
        """Updates astronaut details in the database and updates instance attributes."""
        connection = None
        cursor = None
        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()

                # Build dynamic UPDATE query based on passed parameters
                fields = []
                values = []

                if name is not None:
                    fields.append("AstronautName = %s")
                    values.append(name)
                if age is not None:
                    fields.append("Age = %s")
                    values.append(age)
                if country is not None:
                    fields.append("Country = %s")
                    values.append(country)
                if experience_years is not None:
                    fields.append("ExperienceYears = %s")
                    values.append(experience_years)
                if specialization is not None:
                    fields.append("Specialization = %s")
                    values.append(specialization)
                if status is not None:
                    fields.append("Status = %s")
                    values.append(status)

                if not fields:
                    print("No fields specified for update.")
                    return False

                values.append(self.astronaut_id)
                query = f"UPDATE Astronaut SET {', '.join(fields)} WHERE AstronautId = %s"

                cursor.execute(query, tuple(values))
                connection.commit()

                # Update instance attributes if database query succeeds
                if name is not None:
                    self.astronaut_name = name
                if age is not None:
                    self.age = age
                if country is not None:
                    self.country = country
                if experience_years is not None:
                    self.experience_years = experience_years
                if specialization is not None:
                    self.specialization = specialization
                if status is not None:
                    self.status = status

                logger.info(f"Astronaut {self.astronaut_id} Updated Successfully.")
                print("Astronaut updated successfully.")
                return True
            else:
                print("Connection Failed: Ensure your MySQL server is running.")
                return False

        except Exception as error:
            logger.error(f"Failed to Update Astronaut {self.astronaut_id}: {error}")
            print(f"Failed to Update Astronaut: {error}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    def deleteAstronaut(self):
        """Deletes astronaut from database after verifying no assigned missions exist."""
        connection = None
        cursor = None
        try:
            connection = cc()
            if connection is not None:
                cursor = connection.cursor()

                # First check foreign key constraint: check associated missions
                check_query = "SELECT COUNT(*) FROM Mission WHERE AstronautId = %s"
                cursor.execute(check_query, (self.astronaut_id,))
                mission_count = cursor.fetchone()[0]

                if mission_count > 0:
                    print(f"\nCannot delete Astronaut {self.astronaut_id}.")
                    print(f"Reason: Astronaut is currently assigned to {mission_count} mission(s).")
                    logger.warning(f"Deletion blocked for Astronaut {self.astronaut_id}: Assigned to {mission_count} mission(s).")
                    return False

                # Proceed with deletion
                delete_query = "DELETE FROM Astronaut WHERE AstronautId = %s"
                cursor.execute(delete_query, (self.astronaut_id,))
                connection.commit()

                logger.info(f"Astronaut {self.astronaut_id} Deleted Successfully.")
                print(f"Astronaut {self.astronaut_id} deleted successfully.")
                return True
            else:
                print("Connection Failed: Ensure your MySQL server is running.")
                return False

        except Exception as error:
            logger.error(f"Failed to Delete Astronaut {self.astronaut_id}: {error}")
            print(f"Failed to Delete Astronaut: {error}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
