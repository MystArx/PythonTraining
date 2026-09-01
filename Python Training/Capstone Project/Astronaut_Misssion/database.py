import mysql.connector as ms
from mysql.connector import Error
from logger_config import logger

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "password"
DB_NAME = "SpaceMissionDB"


def create_connection():
    """Returns a connection to SpaceMissionDB database."""
    try:
        connection = ms.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return connection
    except Error as e:
        logger.error(f"Database Connection Error: {e}")
        print(f"Database Connection Error: Unable to connect to MySQL database '{DB_NAME}'.")
        print(f"Details: {e}")
        return None


def init_db():
    """Initializes SpaceMissionDB database and required tables if they do not exist."""
    connection = None
    cursor = None
    try:
        # Step 1: Connect to server to create DB if needed
        connection = ms.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        logger.info(f"Database Connected/Initialized Successfully ({DB_NAME})")

    except Error as e:
        logger.error(f"Failed to initialize database '{DB_NAME}': {e}")
        print(f"Database Initialization Error: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    # Step 2: Create tables in SpaceMissionDB
    try:
        connection = create_connection()
        if connection is None:
            return False

        cursor = connection.cursor()

        # Astronaut Table
        create_astronaut_table = """
        CREATE TABLE IF NOT EXISTS Astronaut (
            AstronautId INT PRIMARY KEY,
            AstronautName VARCHAR(100) NOT NULL,
            Age INT NOT NULL,
            Country VARCHAR(50) NOT NULL,
            ExperienceYears INT NOT NULL,
            Specialization VARCHAR(100) NOT NULL,
            Status VARCHAR(30) NOT NULL
        );
        """

        # Mission Table
        create_mission_table = """
        CREATE TABLE IF NOT EXISTS Mission (
            MissionId INT PRIMARY KEY,
            MissionName VARCHAR(100) NOT NULL,
            Destination VARCHAR(100) NOT NULL,
            LaunchDate DATE NOT NULL,
            DurationDays INT NOT NULL,
            MissionStatus VARCHAR(30) NOT NULL,
            AstronautId INT NOT NULL,
            FOREIGN KEY (AstronautId) REFERENCES Astronaut(AstronautId) ON DELETE RESTRICT
        );
        """

        cursor.execute(create_astronaut_table)
        cursor.execute(create_mission_table)
        connection.commit()
        logger.info("Tables 'Astronaut' and 'Mission' checked/created successfully.")
        return True

    except Error as e:
        logger.error(f"Failed to create tables: {e}")
        print(f"Table Creation Error: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    if init_db():
        print("Database and tables initialized successfully!")
