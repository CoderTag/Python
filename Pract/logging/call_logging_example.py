import logging
#import logging_example
from my_logger import get_logger

# logger = logging.getLogger(logging_example.he)
logger = get_logger(__name__)

logger.warning("Different")
