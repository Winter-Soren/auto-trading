import datetime
import json
import logging
import os
from typing import List, Dict, Any



CURRENT_DIR = os.path.dirname(__file__)

# Configure logging
LOGS_DIR = os.path.join(CURRENT_DIR, "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  
LOG_FILE = os.path.join(LOGS_DIR, "get_closer_expiry_instrument.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def get_closer_expiry_instrument(file_path: str, target_index: str, num_closer_expiry: int = 1) -> List[Dict[str, Any]]:
    try:
            # Load JSON data from file
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            # Get today's date
            today = datetime.date.today()
            logger.info(f"Today's date: {today}")

            # Filter instruments containing the target index in their trading symbol
            target_index = target_index.upper()
            filtered_instruments = [instrument for instrument in json_data['data'] if target_index in instrument['trading_symbol']]

            # Sort filtered instruments by expiry date
            sorted_instruments = sorted(filtered_instruments, key=lambda instrument: instrument['expiry'])

            # Get the sorted_instruments by num_closer_expiry steps
            closer_expiry_instruments = sorted_instruments[:num_closer_expiry]
            logger.info(f"Closer expiry instruments: {json.dumps(closer_expiry_instruments, indent=2)}")
            
            # print(closer_expiry_instruments[0]['instrument_key'])
            return closer_expiry_instruments

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None


# file_path =  "../data/response_Nifty 50.json"
# target_index = "Nifty 22350 CE "
# num_closer_expiry = 1
# get_closer_expiry_instrument(file_path, target_index, num_closer_expiry)