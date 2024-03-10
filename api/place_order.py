import requests
import configparser
import json
import logging
import os
from paramtypes import PlaceOrderParamsType 
from typing import Union, Dict, TypedDict

CURRENT_DIR = os.path.dirname(__file__)

# Configure logging
LOGS_DIR = os.path.join(CURRENT_DIR, "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # Create logs directory if it doesn't exist
LOG_FILE = os.path.join(LOGS_DIR, "place_order.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# class PlaceOrderParamsType(TypedDict):
#     quantity: float
#     product: str
#     validity: str
#     price: float
#     tag: str
#     instrument_token: str
#     order_type: str
#     transaction_type: str
#     disclosed_quantity: int
#     trigger_price: float
#     is_amo: bool


def place_order(params: PlaceOrderParamsType) -> Union[None, Dict[str, Dict[str, str]]]:
    
    config = configparser.ConfigParser()
    config.read('./keys.ini')
    # print(config['UPSTOX']['access_token'])

    try:
        access_token = config['UPSTOX']['access_token']
    except KeyError:
        logger.error("Access token not found in keys.ini")
        print("Access token not found in keys.ini")
        return None

    url = 'https://api.upstox.com/v2/order/place'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }

    # print("url", url)
    try:
        response = requests.post(url, json=params, headers=headers)
        response.raise_for_status()  # Raise exception for non-200 status codes
    except requests.RequestException as e:
        logger.error(f"Error placing order: {e}, for the params: {params}")
        # print(f"Error placing order: {e}")
        return None
    
    try:
        data = response.json()
        logger.info(f"Order placed: {data} for the params: {params}")
        # print(f"Order placed: {data['data']['order_id']}")
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON response: {e}")
        print(f"Error decoding JSON response: {e}")
        return None
    
# if __name__ == "__main__":
#     params = {
#         "quantity": 1,
#         "product": "D",
#         "validity": "DAY",
#         "price": 0,
#         "tag": "string",
#         "instrument_token": "NSE_FO|43899",
#         "order_type": "MARKET",
#         "transaction_type": "BUY",
#         "disclosed_quantity": 0,
#         "trigger_price": 0,
#         "is_amo": False
#     }
#     response = place_order(params)
#     print(response)