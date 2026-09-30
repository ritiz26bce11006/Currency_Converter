# logger_setup.py
# Sets up logging so that errors and events are saved in a file

import logging
from config import LOG_FILE


def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("currency_converter")
