import datetime
import logging
import re
from utility.Paths import Paths

LOG_DIR = "logs"
date_time = re.sub(r'-|:| ', '_', str(datetime.datetime.now().replace(microsecond=0)))

LOG_FILE = list(Paths.get_folder_path('reports'))[0].joinpath(LOG_DIR, f'test_logs_{date_time}.log')

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger