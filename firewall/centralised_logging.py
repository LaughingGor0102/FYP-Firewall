import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Set up a rotating file handler
    handler = RotatingFileHandler(
        "firewall.log",  # Log file name
        maxBytes=5 * 1024 * 1024,  # Maximum file size: 5 MB
        backupCount=3  # Keep 3 backup files
    )
    # Configure logging with the rotating handler
    logging.basicConfig(
        handlers=[handler],
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )
    logger = logging.getLogger()
    logger.info("Logging setup complete with log rotation.")
    return logger