import os
import logging
from datetime import datetime

# ----------------------------
# Configuration
# ----------------------------
LOG_LEVEL = logging.DEBUG  # Change to INFO, WARNING, ERROR, CRITICAL as needed
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# ----------------------------
# Logging setup
# ----------------------------
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - Line:%(lineno)d - %(message)s",
    filemode="w"  # Overwrite each run; use 'a' to append
)

# Create a named logger
logger = logging.getLogger("MLPipelineLogger")

# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("Pipeline logging setup complete!")
    logger.warning("This is a warning!")
    logger.error("This is an error!")
    logger.critical("Critical error!")
