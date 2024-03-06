import os
import configparser
from typing import Optional
import logging
from utils import get_access_code, get_access_token

# Configure logging
LOGS_DIR = '../logs'
os.makedirs(LOGS_DIR, exist_ok=True)  # Create logs directory if it doesn't exist
LOG_FILE = os.path.join(LOGS_DIR, 'auth.log')

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def auth() -> Optional[str]:
    access_code = get_access_code()
    access_token = get_access_token(access_code)

    try:        
        # Store the access token and code in the keys.ini file
        config = configparser.ConfigParser()
        config.read('../keys.ini')  
        config['UPSTOX']['access_code'] = access_code  
        config['UPSTOX']['access_token'] = access_token  

        with open('../keys.ini', 'w') as configfile:
            config.write(configfile)

        logger.info("Access code and access token successfully stored in keys.ini.")


        return access_token
    
    except Exception as e:
        print(f"An error occurred in auth pipeline: {e}")
        logger.error(f"Failed to store access code and access token in keys.ini. Error: {e}")
        return None

