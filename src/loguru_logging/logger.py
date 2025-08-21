from loguru import logger
import sys
from pathlib import Path

logger.remove()  # Remove the default logger

NUMBER_OF_DIR_UP = 2
LOG_DIR = Path(__file__).parents[NUMBER_OF_DIR_UP] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FORMAT = (
    "time:{time:YYYY-MM-DD at HH:mm:ss} | "
    "level:<level>{level: <8}</level> | "
    "{name}:{function}:{line} | "
    "message:{message} "
)

logger.add(
    sink=LOG_DIR / "DEBUG.log", 
    format=LOG_FORMAT,
    filter=lambda record: record["level"].no <= logger.level("WARNING").no,
    level="DEBUG",
    rotation="1 MB",
    compression="zip",
    retention="30 days",
)

logger.add(
    sink=LOG_DIR / "ERROR.log",
    format=LOG_FORMAT,
    level="ERROR",
    rotation="1 MB",
    compression="zip",
    retention="30 days",
    backtrace=True,
    diagnose=True
)

logger.add(
    sink=sys.stderr,
    format=LOG_FORMAT,
    level="DEBUG",
    colorize=True,
)

# logger.debug("This is a debug message for testing purposes.")
# logger.info("Logger initialized with custom format.")
# logger.warning("This is a warning message for testing purposes.")
# logger.critical("This is a critical message for testing purposes.")
# logger.error("This is an error message for testing purposes.")

def get_logger():
    return logger