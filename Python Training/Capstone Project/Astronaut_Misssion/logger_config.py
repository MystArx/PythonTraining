import logging
import os
from datetime import datetime

# Create logs directory if it does not exist
logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

today = datetime.now().strftime("%Y-%m-%d")
log_file_name = f"astronaut-log-{today}.txt"
log_file_path = os.path.join(logs_dir, log_file_name)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("AstronautMissionLogger")
