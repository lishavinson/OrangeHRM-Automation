import logging
from pathlib import Path


# Create logs folder
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

# Log file
log_file = log_folder / "automation.log"


def get_logger(name):

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if not logger.handlers:

        logger.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8"
        )

        # Console handler
        console_handler = logging.StreamHandler()

        # Log format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger