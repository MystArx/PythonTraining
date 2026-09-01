import logging
import os
from datetime import datetime

folder="logs"
if not os.path.exists(folder):
    os.mkdir(folder)

today=datetime.now().strftime("%Y-%m-%d")
log_file=f"student_log_{today}.log"
file_path=os.path.join(folder,log_file)


logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

logger=logging.getLogger()