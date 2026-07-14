import logging
import os


LOG_DIR = "logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

LOG_FILE = (
    f"{LOG_DIR}/pipeline.log"
)


def setup_logger():

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        ),
        handlers=[
            logging.FileHandler(
                LOG_FILE
            ),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger()
