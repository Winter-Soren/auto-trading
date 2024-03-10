import json
import requests
import configparser
import logging
import os

# Get the directory of the current script
CURRENT_DIR = os.path.dirname(__file__)

# Configure logging
LOGS_DIR = os.path.join(CURRENT_DIR, "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # Create logs directory if it doesn't exist
LOG_FILE = os.path.join(LOGS_DIR, "get_option_contracts.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def get_option_contracts(element_str:str) -> None:
    config = configparser.ConfigParser()
    config.read('../keys.ini')

    try:
        access_token = config['UPSTOX']['access_token']
    except KeyError:
        logger.error("Access token not found in keys.ini")
        print("Access token not found in keys.ini")
        return

    url = "https://api.upstox.com/v2/option/contract"

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    params = {
        'instrument_key': f'NSE_INDEX|{element_str}'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for non-200 status codes
    except requests.RequestException as e:
        logger.error(f"Error fetching option contracts: {e}")
        print(f"Error fetching option contracts: {e}")
        return

    try:
        data = response.json()
        with open(f"response_{element_str}.json", "w") as json_file:
            json.dump(data, json_file)
        logger.info(f"Response saved to response_{element_str}.json")
        print(f"Response saved to response_{element_str}.json")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response: {e}")
        print(f"Error decoding JSON response: {e}")

if __name__ == "__main__":
    element_str = 'Nifty 50'
    get_option_contracts(element_str)
