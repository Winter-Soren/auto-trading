
import asyncio
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import your modules
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE_NUMBER
from utils import TelegramMessageListener


async def main():
    api_id = TELEGRAM_API_ID
    api_hash = TELEGRAM_API_HASH
    user_input_channel =  'https://t.me/+8auXr4xpMnxhMWZl'
    phone_number = TELEGRAM_PHONE_NUMBER
    listener = TelegramMessageListener(api_id, api_hash, user_input_channel, phone_number)
    print("Starting listener")
    async with listener:
        await listener.start()
    print('inside the main: ',listener.global_event)
    
    # after this line the listener is listening and the line below will never be reached

    


if __name__ == "__main__":
    asyncio.run(main())
