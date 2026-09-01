import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Configure logger simply
logging.basicConfig(
    filename="logs/employee_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()
