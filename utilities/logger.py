from loguru import logger
import os
from datetime import datetime

def setup_logger(level="INFO"):
    """
    Method Name: Setup Logger
    Author: Such Thadani
    Description: Sets up the logger object using loguru library
    Return Type: Logger object
    Parameters: None
    """
    base_dir = r'C:\Users\10835482\Desktop\CodingChallenges\Gladiator'
    log_dir = os.path.join(base_dir, 'logs')
    os.makedirs(log_dir, exist_ok=True)

    # Remove all existing handlers to release file locks
    logger.remove()

    # Delete all existing log files safely
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except FileNotFoundError:
                print(f"Log file {file_path} was not found.")
            except PermissionError:
                print(f"Could not delete {file_path} because it is in use.")
            except Exception as e:
                print(f"Unexpected error while deleting {file_path}: {e}")

    # Create a new timestamped log file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"log_{timestamp}.log"
    log_path = os.path.join(log_dir, log_file)

    # Add file handler
    logger.add(
        log_path,
        level=level,
        format="[ {time:YYYY-MM-DD HH:mm:ss} ] | {level:<8} | {name} | {function} | {message}",
        rotation="10 MB",
        retention="10 days",
        compression="zip"
    )

    # Add console handler with color
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=level,
        format="<green>[ {time:YYYY-MM-DD HH:mm:ss} ]</green> | "
               "<level>{level:<8}</level> | "
               "<cyan>{name}</cyan> | "
               "<magenta>{function}</magenta> | "
               "<white>{message}</white>\n"
    )

    return logger
