from loguru_logging.logger import get_logger

logger = get_logger()

logger.debug("This is a debug message for testing purposes.")

def keep_running():
    from time import sleep
    while True:
        sleep(10)


keep_running()