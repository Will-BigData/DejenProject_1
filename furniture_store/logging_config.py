
import logging
import sys

logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO, can be changed to DEBUG for more verbosity
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        #logging.StreamHandler(sys.stdout)  # Also log to the console
    ]
)

# Export the logger so it can be imported elsewhere
logger = logging.getLogger(__name__)
